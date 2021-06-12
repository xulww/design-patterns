from User import User


def singleton(self):
    _instances = {}

    def get_instance(*args, **kwargs):
        if self not in _instances:
            _instances[self] = self(*args, **kwargs)

        return _instances[self]

    return get_instance


@singleton
class Bot(User):

    def __init__(self, chat_mediator, name):
        super().__init__(chat_mediator, name)

    def send(self, message):
        print(self.get_name() + " SENT message: " + message)
        self.get_chat_mediator().send_message(message, self)

    def remove_user(self, user):
        print(user.get_name() + " was kicked out of the chat!")
        self.get_chat_mediator().get_users().remove(user)
