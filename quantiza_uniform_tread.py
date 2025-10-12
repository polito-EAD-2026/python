import numpy as np

def quantize_uniform_tread(x, N=8):
  qmin, qmax, qlevel = -1, +1, 2**N-1 # defaults
  qstep = (qmax-qmin) / qlevel
  xnorm = (x-qmin) * qlevel / (qmax-qmin)
  xnorm[xnorm > qlevel] = qlevel
  xnorm[xnorm < 0] = 0
  xnorm_quant = np.floor(xnorm)
  xquant = xnorm_quant * (qmax-qmin) / qlevel
  xquant = xquant + qmin + qstep/2
  return xquant