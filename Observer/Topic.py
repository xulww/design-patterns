from Observable import Observable


class Topic(Observable):
    _subscribers = []
    _topic = ""

    def subscribe(self, observer):
        self._subscribers.append(observer)
        observer.setTopic(self)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def notifyObservers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def setTopic(self, topic):
        self._topic = topic
        self.notifyObservers()

    def getUpdate(self):
        return self._topic
