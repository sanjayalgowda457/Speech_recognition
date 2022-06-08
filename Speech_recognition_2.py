import wave as w
import matplotlib.pyplot as plt
import numpy as np
object=w.open("output.wav","rb")
sample_frequency=object.getframerate()
n_samples=object.getnframes()
signal_wave = object.readframes(-1)

object.close()

t_audio = n_samples / sample_frequency
print((t_audio))

signal_array = np.frombuffer(signal_wave,dtype=np.int16)
times=np.linspace(0,t_audio,num=n_samples)
plt.figure(figsize=(10,5))
plt.plot(times,signal_array)
plt.title("audio signal")
plt.ylabel("signal wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
plt.show()