from Topic import Topic
from Observer import Observer
from TopicSubscriber import TopicSubscriber


def main():
    topic = Topic()

    observerOne = TopicSubscriber("Topic subscriber 1")
    observerTwo = TopicSubscriber("Topic subscriber 2")
    observerThree = TopicSubscriber("Topic subscriber 3")

    topic.subscribe(observerOne)
    topic.subscribe(observerTwo)
    topic.subscribe(observerThree)

    topic.setTopic("Programming is fun!")


if __name__ == "__main__":
    main()
