from Mediator import Mediator
from ChatUser import ChatUser


def main():
    chat_mediator = Mediator()
    user_one = ChatUser(chat_mediator, "User #1")
    user_two = ChatUser(chat_mediator, "User #2")
    user_three = ChatUser(chat_mediator, "User #3")

    chat_mediator.add_user(user_one)
    chat_mediator.add_user(user_two)
    chat_mediator.add_user(user_three)

    user_one.send("addBot")
    user_three.send("Hello everyone!")
    user_two.send("cat")
    user_one.send("That was awkward...")


if __name__ == "__main__":
    main()
