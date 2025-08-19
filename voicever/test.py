import torchaudio
torchaudio.set_audio_backend("soundfile")
print(torchaudio.list_audio_backends())