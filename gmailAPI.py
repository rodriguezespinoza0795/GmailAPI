from email.mime.text import MIMEText
from base64 import urlsafe_b64decode, urlsafe_b64encode

def build_message(destination, obj, body):
    message = MIMEText(body, 'html')
    message['to'] = destination
    message['from'] = 'example@gmail.com'
    message['subject'] = obj
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, destination, obj, body):
    return service.users().messages().send(userId="me",body=build_message(destination, obj, body)).execute()