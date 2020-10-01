#### Follow from line 1 to end line to start up the kafak system.
There are instructions on how to setup online commands to log into VM2 and VM3
Anywords enclosed in <any-word> you must make work with your file/directory names.
If someone else is already running a service it will error when you try to start it, but you should see it is running already.


###Startup order: VM2 kafka zookeeper, VM2 kafka message broker, VM3 kafka message broker, VM3 consumer.py, VM1 producer.py


##Setup alias command in VM1 to connect to VM2 and VM3 (optional)

#Create a new bash source file using your favorite Ubuntu text editor I used nano but emac works to:

Run the following command: 
	$ nano ~/.bash_aliases

Add the following to the the file: NOTICE: Replace <user-name> with your VM1 user name
	alias vm2camcloud='sudo ssh -l cc -i /home/<user-name>/.ssh/<VM2-public-key>.pem 129.114.27.83'
	alias vm3camcloud='sudo ssh -l cc -i /home/<user-name>/.ssh/<VM3-public-key>.pem 129.114.25.142'>

Save and exit then reload the bash source to gain access to these commands:
	$ source ~/.bash_aliases

NOTICE: To manually connect to the VM2 and VM3 using the following command in your command terminal:
	VM2:
		$ sudo ssh -l cc -i /home/<user-name>/.ssh/Team3_VM2.pem 129.114.27.83
	VM3:
		$ sudo ssh -l cc -i /home/<user-name>/.ssh/Team3_VM3.pem 129.114.25.142

### Connect to VM2 using two terminals (requried)
	$ sudo ssh -l cc -i /home/<user-name>/.ssh/Team3_VM2.pem 129.114.27.83
			OR
	$ vm2camcloud

# Start Up Zookeeper on VM2 in one terminal
	$ start-kafka-zookeeper
# Start Up Message Broker on VM2 in the other terminal
	$ start-kafka-msg-broker
	NOTICE: use Ctrl+C to exit close the running process in the terminal

### Connect to VM3 using 3 Terminals (requried)
	sudo ssh -l cc -i /home/<user-name>/.ssh/Team3_VM3.pem 129.114.25.142
		OR
	$ vm3camcloud

# Start up Message Broker on VM3 in one terminal
	$ start-kafka-msg-broker
# Start up CouchDB on VM3 in the second terminal
	$ sudo service couchdb start
# Start the kafka-python-consumer on VM3 in the thrid terminal
	$ start-kafka-python-consumer

### Go back to VM1 and run the kafka-python-producer and watch the messages being recieved on VM3 (requried)
# in VM1 run team3_producer.py code
	$ python3 producer.py

## Check the Database for your document # to increase
http://129.114.25.142:5984/_utils/


