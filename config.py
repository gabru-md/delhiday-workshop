import ssl

PORT = 465
PASSWORD = 'thisisatestpassword'
EMAIL = 'trythisoutyay@gmail.com'
SSL_CONTEXT = ssl.create_default_context()
SMTP_GMAIL = 'smtp.gmail.com'


# SENDERS_EMAIL = {
# 	'EVENTYAY': 'donotreply.eventyay@fossasia.org',
# 	'BADGEYAY': 'donotreply.badgeyay@fossasia.org'
# }


KAFKA_BROKERS = 'localhost:9092'
KAFKA_TOPIC = 'event_notifications'
KAFKA_CONSUMER_GROUP = 'email_service_kcg'