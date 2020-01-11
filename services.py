import json
from kafka import KafkaProducer
from config import *
from flask import (
	Flask,
	render_template,
	request,
	redirect,
	url_for)

class Producer:

	brokers = ''
	topic = ''
	producer = None

	def __init__(self, brokers, topic):

		self.brokers = brokers
		self.topic = topic

		self.producer = KafkaProducer(bootstrap_servers=brokers)


	def produce(self, message=None):

		if not message:
			return False

		try:
			self.producer.send(
				self.topic,
				str.encode(message))
			self.producer.flush()

		except Exception as exp:
			print(exp)
			return False

		return True


app = Flask(__name__)
notification_producer = Producer(KAFKA_BROKERS, KAFKA_TOPIC)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/simulate', methods=['GET','POST'])
def simulate():
	event = json.dumps(request.form)
	print(event)
	if not notification_producer.produce(event):
		print("mail not sent!")
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)