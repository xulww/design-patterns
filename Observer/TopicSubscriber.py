from Observer import Observer


class TopicSubscriber(Observer):
    _name = ""
    _subscribedTo = []

    def __init__(self, name):
        self._name = name

    def update(self):
        if self._subscribedTo == None:
            print(self.getName() + " has no topic")
            return

        newTopic = self._subscribedTo.getUpdate()
        print(self.getName() + " received an update: " + newTopic)

    def setTopic(self, topic):
        self._subscribedTo = topic

    def getName(self):
        return self._name
