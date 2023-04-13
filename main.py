import tkinter as tk
import time
import threading
from ui_builder import NetworkMonitorUI
from router_monitor import (get_connected_devices, get_bandwidth_usage,
                            get_open_ports, block_device, change_port_status,
                            get_router_logs, save_router_logs)
from alerts import (play_audible_alert, send_email, show_toast_notification)
from google.oauth2 import service_account

EMAIL_CREDENTIALS = service_account.Credentials.from_service_account_file(
    'path/to/credentials.json', scopes=['https://www.googleapis.com/auth/gmail.send'])

def update_bandwidth_chart(ui):
    while True:
        time.sleep(5)  # Adjust the update frequency as needed
        bandwidth_data = get_bandwidth_usage()
        if bandwidth_data:
            ui.bandwidth_chart.update_chart(bandwidth_data)

def check_new_devices(ui):
    known_devices = set()
    while True:
        time.sleep(10)  # Adjust the checking frequency as needed
        devices = get_connected_devices()
        if devices:
            for device in devices:
                if device['id'] not in known_devices:
                    known_devices.add(device['id'])
                    play_audible_alert('path/to/audio_file.wav')
                    send_email('recipient@example.com', 'New Device Connected',
                               f"New device connected: {device['name']}", EMAIL_CREDENTIALS)

if __name__ == '__main__':
    app = NetworkMonitorUI()
    bandwidth_thread = threading.Thread(target=update_bandwidth_chart, args=(app,))
    bandwidth_thread.daemon = True
    bandwidth_thread.start()

    new_devices_thread = threading.Thread(target=check_new_devices, args=(app,))
    new_devices_thread.daemon = True
    new_devices_thread.start()

    # Add threads for other events and alerts

    app.mainloop()
