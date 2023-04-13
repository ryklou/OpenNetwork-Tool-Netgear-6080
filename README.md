# OpenNetwork Tool (Netgear 6080)
# Dependencies

- **Tkinter**: For creating the graphical user interface (comes with standard Python distribution).
- **Requests**: To interact with your router's API (if available) or web interface for obtaining data and performing actions.
- **Matplotlib**: For creating the line chart to display bandwidth usage.
- **Playsound**: For playing audible alerts.
- **Google API Client Library**: To send email alerts through Gmail.
- **Win10toast**: For displaying Windows 11 toast notifications.

## Installation

You can install the required libraries using pip:

```bash
pip install requests matplotlib playsound google-api-python-client google-auth-httplib2 google-auth-oauthlib win10toast

Application Structure
We will still split the functionality into separate Python files:

main.py: The main file to run the application.
router_monitor.py: Contains functions to interact with the router (get device information, block devices, get and save logs, etc.).
bandwidth_chart.py: Handles the real-time bandwidth usage chart.
alerts.py: Manages audible, email, and toast notifications.
ui_builder.py: Handles the creation of the Tkinter-based user interface.