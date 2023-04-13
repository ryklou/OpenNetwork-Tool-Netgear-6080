import tkinter as tk
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")


class BandwidthChart(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_chart(self, data):
        self.ax.clear()

        for device, bandwidth_data in data.items():
            x = np.arange(len(bandwidth_data))
            self.ax.plot(x, bandwidth_data, label=device)

        self.ax.legend()
        self.ax.set_title("Bandwidth Usage")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Bandwidth (Mbps)")

        self.canvas.draw()
