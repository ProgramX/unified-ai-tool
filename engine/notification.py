
# Author: Mujtaba
# Date: July 13, 2023

# Handles notifications such as file operations, etc. If there is a notification, other modules
# capable of handling it will perform the desired action. - Its not like that notifications that we see
# in notification bar of our mobile phones.

# How notifs look like: 'rename_file', '/path/to/file'
class Notification:
    notifications = []

    def __init__(self, command: str, data: str):
        self.command = command
        self.data = data

    def __str__(self):
        return self.command + " " + self.data
