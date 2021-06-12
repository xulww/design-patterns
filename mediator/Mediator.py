import re

from ChatMediator import ChatMediator
from Bot import Bot


class Mediator(ChatMediator):

    _users = None
    _bot = None

    def __init__(self):
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def send_message(self, message, user):

        if message == "addBot":
            self._bot = Bot(user.get_chat_mediator(), "Bot")

            self._users.append(self._bot)

        for usr in self._users:
            if (usr != user):
                usr.receive(message)

        if re.compile(r'\bcat\b').findall(message) and self._bot is not None and user != self._bot:
            self._bot.send("cat is a forbidden word!")
            self._bot.remove_user(user)

    def get_users(self):
        return self._users
