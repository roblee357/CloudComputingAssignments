# CloudComputingAssignments


1. Start VM2 ZooKeeper
	a. usr/bin/kafka_2.13-2.6.0$ bin/zookeeper-server-start.sh config/zookeeper.properties
	b. If this doesn't start remove logs in/tmp/zookeeper directory and /tmp/kafka-logs directory. 
		i. cc@team3-vm2:/tmp$ sudo rm -r zookeeper
	       ii. cc@team3-vm2:/tmp$ sudo rm -r zookeeper
2. Start VM2 Message Broker
	a. usr/bin/kafka_2.13-2.6.0$ bin/kafka-server-start.sh config/server.properties
3. Start VM3 Message Broker
	a. home/kafka_2.13-2.6.0$ sudo bin/kafka-server-start.sh config/server.properties
4. Start couchDB on VM3
	a. ??
5. Start VM3 consumer.py
	a. home$ python3 consumer.py
6. Start VM1 producer.py
	a. home$ producter.py