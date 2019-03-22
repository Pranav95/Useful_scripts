from time import sleep
import random 
from kafka import KafkaProducer

def connect_kafka():
	_producer = None
	try:
		_producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))

	except Exception as ex:
		print('Exception while connecting Kafka')
		print(str(ex))
	finally:
		return _producer



def produce_data():
	while True:

		count = 0
		key = bytes("key", encoding = 'utf-8')
		print("connecting")
		producer = connect_kafka()
		print("connected")



		if producer is None:
			return 
		while(count<20):
			x = random.randint(0,10)
			value_bytes = bytes(str(x), encoding = 'utf-8')
			#data = {'number' : value_bytes}
			#producer.send('stream_1',value = data)
			producer.send('stream_1',key = key, value= value_bytes )
			count = count + 1
		print("20 Values sent Kafka")
		producer.flush()
		sleep(20)







if __name__ == "__main__":
	produce_data()
		