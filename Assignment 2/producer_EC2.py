#
#
# Author: Aniruddha Gokhale
# CS4287-5287: Principles of Cloud Computing, Vanderbilt University
#
# Created: Sept 6, 2020
#
# Purpose:
#
#    Demonstrate the use of Kafka Python streaming APIs.
#    In this example, we use the "top" command and use it as producer of events for
#    Kafka. The consumer can be another Python program that reads and dumps the
#    information into a database OR just keeps displaying the incoming events on the
#    command line consumer (or consumers)
#

import os   # need this for popen
import time # for sleep
import json
import datetime
from kafka import KafkaProducer  # producer of events


# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the producer
# (you will need to change this to your bootstrap server's IP addr)
print("Starting Connection to Bootstrap server")
#producer = KafkaProducer (bootstrap_servers="129.114.27.83:9092", 
#                                          acks=1)  # wait for leader to write to log

producer = KafkaProducer (bootstrap_servers="ec2-34-196-187-2.compute-1.amazonaws.com:9092", 
                                          value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                          acks=1)  # wait for leader to write to log

#producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
print("Connected to bootstrap server ")
# say we send the contents 100 times after a sleep of 1 sec in between
for i in range (100):
    # get the output of the top command
    process = os.popen ("top -n 1 -b")

    # read the contents that we wish to send as topic content
    contents = process.read ()

    # send the contents under topic utilizations. Note that it expects
    # the contents in bytes so we convert it to bytes.
    #
    # Note that here I am not serializing the contents into JSON or anything
    # as such but just taking the output as received and sending it as bytes
    # You will need to modify it to send a JSON structure, say something
    # like <timestamp, contents of top>
    #
    #producer.send ("utilizations", value=bytes (contents, 'ascii'))
    currentDatetime = datetime.datetime.now()

    

    # print(contents)
    #Send in JSON format .send('<topic>', {'key':'value})

    #producer.send('utilizations_mike', {str(currentDatetime): {"utilizations_mike", "This as a test message from Mike's VM1: message#"+ str(i)}})
    topic ='utilizations_rob'
    #producer.send(topic, {'Timestamp':str(currentDatetime),'Top output':contents})
    producer.send(topic, {'Timestamp':str(currentDatetime),'Top output':contents, 'Topic':topic })

    print('Json Datetime string: ' + str(currentDatetime) + ' Sent Message...' + contents)
    #print("This as a test message from Mike's VM1: message#"+ str(i))
#    producer.send('utilizations', {'foo' : 'bar')
#    producer.send('utilizations', b'somemessagehere')
    producer.flush ()   # try to empty the sending buffer
    # sleep a second
    time.sleep (1)

# we are done
producer.close ()
