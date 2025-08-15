import sounddevice as sd
from scipy.io.wavfile import write
def create_audio_file():
    sampling_frequency = 48000
    time_period = 5
    recording = sd.rec(
        int(sampling_frequency*time_period),
        samplerate=sampling_frequency,
        channels=1
    )
    sd.wait()
    write("sample.wav",sampling_frequency,recording)
create_audio_file()