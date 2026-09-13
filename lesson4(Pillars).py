#Polymorphism
class Notification:
    def send(self):
        print("Notification Sent")

class EmailNotification(Notification):
    def send(self):
        print("Email Sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS Sent")
        
        