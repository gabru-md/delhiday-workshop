## Delhi Day Open Tech Summit Kafka Workshop

This repository contains the code for the Workshop on **Event Driven systems using Apache Kafka by Manish Devgan**.

### Requirements

You need to have Python3 installed as well as flask, kafka-python, smtplib and ssl.

### Installation

* Clone the repository
`git clone https://github.com/gabru-md/delhiday-workshop`.

* Change the gmail username and password in the config file.

* Download and extract Apache Kafka from `kafka.apache.org`.

* Try running the quickstart examples on Apache Kafka Website.

* Create a topic on Kafka named `event_notifications` using `bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic event_notifications`

* Run your instance of Zookeeper and Apache Kafka. Ensure thath you run Apache Kafka after you run Zookeeper.

* In the first terminal run `python3 services.py`

* In the second terminal run `python3 mail-consumer.py`


### Using the Application

* Open your browser and head over to `localhost:5000` and choose the event-type and the service-type.

* Enter the name of receiver and the email address to send the mail to.

* Wait for the email to be received.


### Thanks
