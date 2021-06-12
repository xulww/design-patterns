class User:
    _chat_mediator = None
    _name = None

    def __init__(self, chat_mediator, name):
        self._chat_mediator = chat_mediator
        self._name = name

    def send(self, message):
        pass

    def receive(self, message):
        pass

    def get_chat_mediator(self):
        return self._chat_mediator

    def get_name(self):
        return self._name
