import numpy as np
import matplotlib.pyplot as plt
import librosa

# Local imports
from quantiza_uniform_tread import quantize_uniform_tread
from snr import SNR
from util import RMS, dBFS, normalize
from pltot_vs_time import plot_vs_time

#!wget "https://github.com/polito-EAD-2026/media/raw/refs/heads/dev/potter.wav"

def main():
    ###### ESERCIZIO: QUANTIZATION SNR vs RMS
    #
    # Compilare il GSheet a questo link: https://docs.google.com/spreadsheets/d/1Mvx-SDGy89HaODUmuyzAGZ8RjGiq1igECk1gVaEOIb8/edit?usp=sharing
    # Inserire il valore di RMS nella colonna A
    # Inserire il valore di SNR (con N=8 bit) nella colonna B
    #
    # n.b. selezionata la cella, inserire il valore nella barra delle formule così da incollare solo il valore
    #

    A = 1.5 # TODO: Variare il seguente valore di ampiezza per ottenere diverse coppie di valori

    # Caricamento file audio
    in_filename = "../media/potter.wav"
    x, sr = librosa.load(in_filename, sr=None)
    t = np.arange(x.shape[0]) / sr

    # Numero di bit da utilizzare
    N = 8

    # Variazione intensità del segnale
    xA = A * x
    xAq = quantize_uniform_tread(xA, N)

    # Calcolo RMS ed SNR
    rms = RMS(xA)
    snr = SNR(xA, xAq)

    # visualizzazione
    fig, ax = plt.subplots(figsize=(12,4))
    plot_vs_time(xA,t, fig=(fig,ax))
    ax.axhline(y=rms, color='r', linestyle='--', label='RMS')
    ax.axhline(y=-rms, color='r', linestyle='--', label='RMS')

    print(f"Riportare nel foglio di calcolo i seguenti valori")
    print(f"RMS (colonna A): {rms}")
    print(f"SNR (colonna B): {snr}")

    print()
    print(f'Ascoltare l\'audio quantizzato.\nQuanto è "buono" un SNR di: {snr:.0f} dB?')
    # IPython.display.display(IPython.display.Audio(xAq,rate=sr) )

    plt.show()

if __name__ == "__main__":
  main()

print(__name__)