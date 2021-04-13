from Observable import Observable


class Topic(Observable):
    _subscribers = []
    _topic = ""

    def subscribe(self, observer):
        self._subscribers.append(observer)
        observer.set_topic(self)

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)

    def notify_observers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def set_topic(self, topic):
        self._topic = topic
        self.notify_observers()

    def get_update(self):
        return self._topic
