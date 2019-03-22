import time 
from kafka import KafkaConsumer 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql.functions import *
from pyspark.streaming.kafka import KafkaUtils
import json
import os
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'



if __name__ == '__main__':

	sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
	sc.setLogLevel("WARN")
	ssc = StreamingContext(sc, 20)

	#kafkaStream = KafkaUtils.createStream(ssc, 'localhost:9092', 'spark-streaming', topics = {'stream_1':1})

	kafkaStream = KafkaUtils.createDirectStream(ssc, ['stream_1'], {"bootstrap.servers": 'localhost:9092'})
	lines = kafkaStream.map(lambda x : int(x[1]))

	lines = lines.map(lambda x : x*2)
	
	

	lines.pprint()

	print(type(lines))
	
	ssc.start()
	ssc.awaitTermination()
	print("DONE")