import pyaudio as pau
import wave as w
#FPB= frame per buffer
FPB=3200
FORMAT=pau.paInt16
CHANNELS=1
RATE=16000

P = pau.PyAudio()
stream=P.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FPB
)
print("start Recording : SHOUT SOMETHING")
s=15
#frames are get listed
frames=[]
for i in range(0,int(RATE/FPB * s)):
    data= stream.read(FPB)
    frames.append(data)
stream.stop_stream()
stream.close()
P.terminate()

#to save the  output in wave form

object=w.open("Microphone_recordings.wav","wb")
object.setnchannels(CHANNELS)
object.setsampwidth(P.get_sample_size(FORMAT))
object.setframerate(RATE)
object.writeframes(b"".join(frames))
object.close()