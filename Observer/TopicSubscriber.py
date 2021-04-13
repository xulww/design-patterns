from Observer import Observer


class TopicSubscriber(Observer):
    _name = ""
    _subscribed_to = []

    def __init__(self, name):
        self._name = name

    def update(self):
        if self._subscribed_to == None:
            print(self.get_name() + " has no topic")
            return

        new_topic = self._subscribed_to.get_update()
        print(self.get_name() + " received an update: " + new_topic)

    def set_topic(self, topic):
        self._subscribed_to = topic

    def get_name(self):
        return self._name
