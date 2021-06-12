from topic import Topic
from observer import Observer
from topic_subscriber import TopicSubscriber


def main():
    topic = Topic()

    observer_one = TopicSubscriber("Topic subscriber 1")
    observer_two = TopicSubscriber("Topic subscriber 2")
    observer_three = TopicSubscriber("Topic subscriber 3")

    topic.subscribe(observer_one)
    topic.subscribe(observer_two)
    topic.subscribe(observer_three)

    topic.set_topic("Programming is fun!")


if __name__ == "__main__":
    main()
