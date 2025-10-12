import scipy

def band_pass_filter(audio, sr, low_freq, high_freq):
    nyquist = sr / 2
    low = low_freq / nyquist
    high = high_freq / nyquist
    b, a = scipy.signal.butter(2, [low, high], btype='band')
    return scipy.signal.filtfilt(b, a, audio)