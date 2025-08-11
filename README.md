The voice assistant is going to be a Raspberry Pi 4B that will run and output audio through a speaker whenever I ask it a question. The Raspberry Pi will run ChatGPT locally, and I plan on making it run offline, meaning it doesn't need to rely on the Internet.
I made the project because I saw TikToks of a voice assistant that was running by itself, and it had a fish that modeled the voice assistant speaking. I also plan on using this experience to learn CAD because the best way to learn is to put work into it.


| Item | Description | Example/Link | Quantity | Unit Price (USD) | Total Price (USD) | Notes |
|------|-------------|--------------|----------|------------------|-------------------|-------|
| Raspberry Pi 4 | Model B, 4GB or 8GB RAM | [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) | 1 | $55.00 | $55.00 | Main single-board computer; I already have a Raspberry Pi|
| MicroSD Card | 16GB or larger, Class 10/UHS-1 | [SanDisk Ultra 16GB microSDHC](https://www.sandisk.com/home/memory-cards/microsd-cards/ultra-microsd) | 1 | $6.00 | $6.00 | Holds OS and files |
| USB Microphone | Plug-and-play USB mic | [FIFINE K669B USB Microphone](https://fifinemicrophone.com/) | 1 | $30.00 | $30.00 | For voice input |
| Speaker | 3.5mm aux or Bluetooth | [Creative Pebble 2.0](https://www.creative.com/p/speakers/creative-pebble) | 1 | $25.00 | $25.00 | Audio output |
| Carrying Case | Custom-designed enclosure | N/A (planned 3D print) | 1 | $10.00 | $10.00 | Designed for portability and protection |
**Estimated Total Cost:** **$71.00**

Step-by-Step: 
1. To run this voice assistant, you have to be on your Raspberry Pi's terminal and check if your audio devices are connected to the device.
2. Download the necessary packages/libraries; these two are system packages: sudo apt install -y python3-venv python3-dev build-essential \
  portaudio19-dev libasound2-dev ffmpeg
This one is a library: pip install --upgrade openai sounddevice soundfile numpy
4. The code interferes with the system, so the best practice is to run the code in a virtual environment: mkdir -p ~/voice_assistant && cd ~/voice_assistant
python3 -m venv .venv
source .venv/bin/activate
5. You must then create an environment variable because this is going to be run on the cloud; around this part is the time to find your API key: nano .env, OPENAI_API_KEY=sk-..., export $(grep -v '^#' .env | xargs)
6. Then run the code in terminal: source .venv/bin/activate
python app.py

Troubleshooting I've had:
ALSA “No default device” / “Device busy”
Re-check arecord -l / aplay -l, make sure your ~/.asoundrc card numbers match, and kill anything holding the device (PulseAudio/Bluetooth). The “set USB as default” guides walk through card ordering and defaults.
