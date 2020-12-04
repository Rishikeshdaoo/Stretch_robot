import pydub
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("../audios/Joy.wav")
sound.apply_gain(-6)
play(sound)
