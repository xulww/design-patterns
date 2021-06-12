from User import User


class ChatUser(User):

    def __init__(self, chat_mediator, name):
        super().__init__(chat_mediator, name)

    def send(self, message):
        print(self.get_name() + " SENT message: " + message)
        self.get_chat_mediator().send_message(message, self)

    def receive(self, message):
        print(self.get_name() + " RECEIVED message: " + message)
