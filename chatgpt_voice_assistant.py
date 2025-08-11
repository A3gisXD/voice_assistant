import io, queue, sys, time, numpy as np
import sounddevice as sd, soundfile as sf
USE_CLOUD_STT = True  

# Recording params
RATE = 16000
CHANNELS = 1
BLOCK = 1024
silence_ms = 700

def record_utterance():
    q = queue.Queue()
    def cb(indata, frames, t, status):
        q.put(indata.copy())
    with sd.InputStream(samplerate=RATE, channels=CHANNELS, callback=cb):
        audio, silent_for = [], 0
        start = time.time()
        while True:
            chunk = q.get()
            audio.append(chunk)
            # simple VAD-ish: if RMS is low, count as silence
            rms = np.sqrt(np.mean(chunk**2))
            if rms < 0.01:
                silent_for += (BLOCK/RATE)*1000
            else:
                silent_for = 0
            if len(audio)*BLOCK/RATE > 1.0 and silent_for > silence_ms:
                break
        data = np.concatenate(audio, axis=0)
        buf = io.BytesIO()
        sf.write(buf, data, RATE, format='WAV')
        return buf.getvalue()

def tts_play(text, client):
    # OpenAI TTS -> WAV bytes
    speech = client.audio.speech.create(model="gpt-4o-mini-tts", voice="alloy", input=text)
    audio = io.BytesIO(speech.read())
    audio.seek(0)
    data, sr = sf.read(audio, dtype='float32')
    sd.play(data, sr); sd.wait()

def think_n_say(text, client):
    # Simple chat call
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":text}])
    answer = resp.choices[0].message.content
    tts_play(answer, client)

if __name__ == "__main__":
    if USE_CLOUD_STT:
        from openai import OpenAI
        client = OpenAI()
        print("🎙️ Speak after the beep… Ctrl+C to quit.")
        while True:
            audio_wav = record_utterance()
            # Send wav to transcription
            tr = client.audio.transcriptions.create(model="whisper-1", file=("speech.wav", audio_wav))
            user_text = tr.text
            print("You:", user_text)
            think_n_say(user_text, client)
    else:
        from faster_whisper import WhisperModel
        model = WhisperModel("base")  # try "tiny" if laggy
        from openai import OpenAI
        client = OpenAI()
        print("🎙️ Speak after the beep… Ctrl+C to quit.")
        while True:
            audio_wav = record_utterance()
            # Local transcription
            import tempfile
            with tempfile.NamedTemporaryFile(suffix=".wav") as f:
                f.write(audio_wav); f.flush()
                segments, _ = model.transcribe(f.name)
                user_text = "".join(s.text for s in segments).strip()
            print("You:", user_text)
            think_n_say(user_text, client)
