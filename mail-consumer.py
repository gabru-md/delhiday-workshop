import smtplib
import json
from kafka import KafkaConsumer
from config import *
from email_type import body

def send_email(receiver=None, message=None):
	if not receiver:
		return False

	with smtplib.SMTP_SSL(SMTP_GMAIL, PORT, context=SSL_CONTEXT) as server:
		try:
			server.login(EMAIL, PASSWORD)
			server.sendmail(
				EMAIL,
				receiver,
				message
				)
		except Exception as exp:
			print(exp)
			return False

	return True

def build_email_service_consumer():

	consumer = KafkaConsumer(
		KAFKA_TOPIC,
		bootstrap_servers=KAFKA_BROKERS,
		group_id=KAFKA_CONSUMER_GROUP,
		)

	return consumer


def deserialize_value(consumer_record):
	try:
		return json.loads(
		consumer_record.value.decode())
	except Exception as exp:
		print(exp)
		return None


def run_email_service():

	try:
		email_consumer = build_email_service_consumer()

		for consumer_record in email_consumer:
			notification = deserialize_value(consumer_record)
			
			if notification:

				if notification['type'] == 'confirm_email':
					username = notification['username']
					message_body = body('CE').format(username, notification['service'])

				if notification['type'] == 'new_user':
					username = notification['username']
					message_body = body('NU').format(username, notification['service'])

				print(message_body)

				if 'receiver' in notification:
					send_email(
						notification['receiver'],
						message_body,
						)
					print("Mail sent to {}".format(notification['receiver']))
			

	except Exception as exp:
		print(exp)
		return False


	return True


if __name__ == '__main__':
	print("running service")
	run_email_service()