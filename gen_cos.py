import numpy as np

def gen_cos(dur=1, Fs=100, amp=1, freq=2, phase=0):
    num_samples = int(Fs * dur)
    t = np.arange(num_samples) / Fs
    x = amp * np.cos( (2*np.pi*freq*t) + phase)
    return x, t

def gen_cos_d(dur=1, Fs=100, amp=1, freq=2, delay=0):
    num_samples = int(Fs * dur)
    t = np.arange(-num_samples,num_samples) / Fs
    x = amp * np.cos(2*np.pi*freq*(t-delay))
    return x, t