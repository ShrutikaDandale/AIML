# Mini Project – OOP Chat System
# Letʼs create a Chat System using OOPs concepts. 
# We have to create classes:
# •User
# •Message
# •ChatRoom
# And we have to implement functions:
# •sending messages
# •viewing chat history
# •user joining and leaving the chatroom

class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text


class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join_user(self, user):
        self.users.append(user)

    def leave_user(self, user):
        self.users.remove(user)

    def send_message(self, sender, text):
        msg = Message(sender, text)
        self.messages.append(msg)

    def view_chat_history(self):
        for msg in self.messages:
            print(msg.sender.username, ":", msg.text)


# Create users
u1 = User("kookie", 1)
u2 = User("tae", 2)

# Create chat room
chat = ChatRoom()

# Users join
chat.join_user(u1)
chat.join_user(u2)

# Send messages
chat.send_message(u1, "Hello everyone!")
chat.send_message(u2, "Hi Kookie!")

# View chat history
chat.view_chat_history()

# User leaves
chat.leave_user(u2)