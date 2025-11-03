import matplotlib.pyplot as plt

"""
Example of usage:
import numpy as np
N, Fs, A, f = 10, 10, 0.5, 2
t = np.arange(N) / Fs
s = A * np.cos(2 * np.pi * f * t)
plot_vs_time(s,t, fmt='-*')
"""

def plot_vs_time(w, t, xlim=None, ylim=[-1, +1], fig=None, fmt='-'):
    """
    Plots a waveform versus time using matplotlib.
    Parameters:
        w (array-like): The waveform data to plot (y-axis values).
        t (array-like): The time values corresponding to the waveform (x-axis values).
        xlim (tuple, optional): Limits for the x-axis as (min, max). If None, uses the range of t.
        ylim (list or tuple, optional): Limits for the y-axis as [min, max]. Defaults to [-1, +1].
        fig (matplotlib.figure.Figure, optional): Existing figure to plot on. If None, creates a new figure.
        fmt (str, optional): Format string for the plot line (e.g., '-', '--', 'o'). Defaults to '-'.
    Returns:
        tuple: (fig, ax) where fig is the matplotlib Figure object and ax is the Axes object.
    Notes:
        - The function sets axis labels, grid, and tight layout for better appearance.
        - If no figure is provided, a new figure with size (12, 3) is created.
    """
    fig, ax = plt.subplots(figsize=(12,3)) if fig is None else fig
    ax.plot(t,w,fmt)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_xlim(xlim) if xlim is not None else plt.xlim(t[0],t[-1])
    ax.set_ylim(ylim) if ylim is not None else None
    fig.tight_layout()
    ax.grid(visible=True)