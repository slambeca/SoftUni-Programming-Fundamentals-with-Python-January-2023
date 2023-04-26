class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()

    if command == "Stop":
        break

    command_args = command.split()
    sender = command_args[0]    # ['Peter', 'John', 'Hi,John']
    receiver = command_args[1]
    message = command_args[2]

    email = Email(sender, receiver, message)
    emails.append(email)

send_emails = [int(x) for x in input().split(", ")]    # [0, 2]
# send_emails = [emails[int(x)].send for x in input().split(", ")]

for email in send_emails:
    emails[email].send()

for email in emails:
    print(email.get_info())