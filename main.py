import wave as w
object=w.open("cartoon-laser.wav","rb")
print("No of channels",object.getnchannels())
print("sample width",object.getsampwidth())
print("frame_rate",object.getframerate())
print("frames",object.getnframes())
print("parameters",object.getparams())
t_object= object.getnframes()/object.getframerate()
print(t_object)
frames=object.readframes(-1)
print(len(frames))
print(len(frames)/4)
object.close()

## To create a new channels

object_new= w.open("new.wav","wb")
object_new.setnchannels(1)
object_new.setsampwidth(2)
object_new.setframerate(44100.0)
object_new.writeframes(frames)
object_new.close()