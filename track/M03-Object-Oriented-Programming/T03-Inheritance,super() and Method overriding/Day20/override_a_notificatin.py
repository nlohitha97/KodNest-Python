class Notification:
    def send(self,message):
        print(f"General Notification: {message}")

class EmailNotification(Notification):
    # Override send()
    def send(self,message):
        super().__init__()
        print(f"Email Notification: {message}")
message = input().strip()
# Create both objects and call send()
m=Notification()
n= EmailNotification()

m.send(message)
n.send(message)
