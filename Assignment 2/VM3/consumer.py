import json
import pycouchdb
from kafka import KafkaConsumer  # consumer of events

# We can make this more sophisticated/elegant but for now it is just
# hardcoded to the setup I have on my local VMs

# acquire the consumer
# (you will need to change this to your bootstrap server's IP addr)
consumer = KafkaConsumer (bootstrap_servers="129.114.27.83:9092")

# subscribe to topic
#consumer.subscribe (topics=["utilizations_nida","utilizations_mike","utilizations_rob","utilizations_rob"])
consumer.subscribe (topics=["utilizations_mike", "utilizations_rob", "utilizations_nida"])
print ('starting consumer')
MikesProdMsgs = list()
RobsProdMsgs = list()
NidasProdMsgs = list()
print ('starting connection to couchdb')
db = pycouchdb.Server("http://admin:Team3@127.0.0.1:5984/")
mikesCDB = db.database("utilizations_mike")
robsCDB = db.database("utilizations_rob")
nidasCDB = db.database("utilizations_nida")

mikesDocIDfile = open("MikesDatabaseDocIDs.txt", "w+")
robsDocIDfile = open("RobsDatabaseDocIDs.txt", "w+")
nidasDocIDfile = open("NidasDatabaseDocIDs.txt", "w+")

mikeCount = 0
robCount = 0
nidaCount = 0
print ('waiting for messages...')
# we keep reading and printing
for msg in consumer:
    print ('Recieving Message...')
    # what we get is a record. From this record, we are interested in printing
    # the contents of the value field. We are sure that we get only the
    # utilizations topic because that is the only topic we subscribed to.
    # Otherwise we will need to demultiplex the incoming data according to the
    # topic coming in.
    #
    # convert the value field into string (ASCII)
    #
    # Note that I am not showing code to obtain the incoming data as JSON
    # nor am I showing any code to connect to a backend database sink to
    # dump the incoming data. You will have to do that for the assignment.
#    print (str(msg.value, 'ascii'))
    msg_json_obj = json.loads(msg.value)

#    topicName = msg_json_obj['Topic']
#    timestamp = msg_json_obj['Timestamp']
#    topOutput = msg_json_obj['Top output']
    if msg_json_obj['Topic'] == 'utilizations_mike':
        doc1 = mikesCDB.save(msg_json_obj)
        mikesDocIDfile.write(str(doc1['_id'] + '\n' ))
        mikesDocIDfile.flush()
#        os.fsync(mikesDocIDfile.fileno())
        mikeCount += 1
    elif msg_json_obj['Topic'] == 'utilizations_rob':
        doc1 = robsCDB.save(msg_json_obj)
        robsDocIDfile.write(doc1['_id'] + '\n')
        robsDocIDfile.flush()
#        os.fsync(robsDocIDfile.fileno())
        robCount += 1
    elif msg_json_obj['Topic'] == 'utilizations_nida':
        doc1 = nidasCDB.save(msg_json_obj)
        nidasDocIDfile.write(doc1['_id'] + '\n')
        nidasDocIDfile.flush()
#        os.fsync(nidasDocIDfile.fileno())
        nidaCount += 1

    if mikeCount == 100:
        mikesDocIDfile.close()
    if robCount == 100:
        robsDocIDfile.close()
    if nidaCount == 100:
        nidasDocIDfile.close()

    #print("Topic: " + topicName)
    #print("Timestamp: " + timestamp)
    #print("Top output: " + topOutput)

# we are done. As such, we are not going to get here as the above loop
# is a forever loop.








