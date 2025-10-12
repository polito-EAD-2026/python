import numpy as np

def SNR(original, quantized):
  noise = quantized - original
  powS = np.sum(original**2)
  powN = np.sum(noise**2)
  return 10*np.log10(powS/powN)