import os

def display_notification(title, message):
    system = os.name
    if system == 'nt':  # Windows
        os.system('powershell -Command "New-BurntToastNotification -Text \'{}\' -Title \'{}\'"'.format(message, title))
    elif system == 'posix':  # Linux/Mac
        os.system('notify-send "{}" "{}"'.format(title, message))

# Example usage:
display_notification("Warning", "You have been hacked")
