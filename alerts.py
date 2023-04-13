
from playsound import playsound
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import os
from email.mime.text import MIMEText
from win10toast import ToastNotifier

def play_audible_alert(audio_file):
    try:
        playsound(audio_file)
    except Exception as e:
        print(f"Error playing audible alert: {e}")

def send_email(to, subject, body, credentials):
    try:
        service = build('gmail', 'v1', credentials=credentials)
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'Email was sent to "{to}" with Email Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message

def show_toast_notification(title, message, duration=5, icon=None):
    toaster = ToastNotifier()
    toaster.show_toast(title, message, icon_path=icon, duration=duration)

