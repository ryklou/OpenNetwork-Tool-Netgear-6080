import tkinter as tk
import tkinter.ttk as ttk
from bandwidth_chart import BandwidthChart

class NetworkMonitorUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Window settings
        self.title("OpenNetwork Tool")
        self.geometry("800x600")

        # Create notebook for organizing tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        # Connected devices tab
        self.devices_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.devices_tab, text="Connected Devices")

        # Bandwidth usage tab
        self.bandwidth_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.bandwidth_tab, text="Bandwidth Usage")
        self.bandwidth_chart = BandwidthChart(self.bandwidth_tab)
        self.bandwidth_chart.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Ports tab
        self.ports_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.ports_tab, text="Ports")

        # Router logs tab
        self.logs_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.logs_tab, text="Router Logs")

