import sounddevice as sd
def input_audio():
    sampling_frequency = 44100
    time_period = 7
    recording = sd.rec(
        int(sampling_frequency*time_period),
        samplerate=sampling_frequency,
        channels=1
    )
    sd.wait()
    return [sampling_frequency,time_period,recording]
