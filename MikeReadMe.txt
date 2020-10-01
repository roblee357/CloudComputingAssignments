
**VM2 - with Kafka installed at /usr/bin/kafka_<version>
Connection String:
	sudo ssh -l cc -i /home/mike/.ssh/CloudComputingChameleonKeyPair-Programmer3591.pem 129.114.27.83

Read all messages from topic utilizations
	<kafka-version>/bin/kafka-console-consumer.sh --topic utilizations --from-beginning --bootstrap-server localhost:9092

Write Events To Utilizations topic: 
	<kafka-version>/bin/kafka-console-producer.sh --topic utilizations --bootstrap-server localhost:9092

Open Port 9092:
	sudo ufw enable
	sudo ufw allow 9092

Set Listener for Message Broker Server on /bin/cofig/server.properties:
	advertised.listeners=PLAINTEXT://129.114.27.83:9092


**VM2 Startup
Zookeeper
	<kafka-version>/bin/zookeeper-server-start.sh config/zookeeper.properties 

Message Broker
	<kafka-version>bin/kafka-server-start.sh config/server.properties


**Kafka commands VM2:
	View all of the topics: 
		bin/kafka-topics.sh --list --bootstrap-server localhost:9092
	Read all events of a specific topic:
		bin/kafka-console-consumer.sh --topic utilizations --from-beginning --bootstrap-server localhost:9092


## VM3 Connection string
	sudo ssh -l cc -i /home/mike/.ssh/Team3_VM3.pem 129.114.25.142


## VM1 Setup
INSTALL PIP3 ON VM1:
sudo apt-get install python3-pip
sudo python3 -m pip install kafka-python

INSTALL Kafka-python
pip3 install kafka-python

INSTALL Kafka
	Download the Kafka tar file:
		sudo apt install curl
		curl "https://downloads.apache.org/kafka/2.6.0/kafka_2.13-2.6.0.tgz" -o ~/Downloads/kafka_2.13-2.6.0.tgz
		
	Check the download SHA512 hash equals: (keys found at https://
		gpg --print-md SHA512 kafka_2.13-2.6.0.tgz
			kafka_2.13-2.6.0.tgz: D884E4DF 7D85B4FF F54CA9CD 987811C5 8506AD78 71B9ED71
                			      14BBAFA6 FEE2E79F 43D04C55 0EEA471F 508B08EA 34B4316E
			                      A1E52999 6066FD9B 93FCF912 F41F6165

	Move the file into the /usr/bin location:
		sudo mv kafka_2.13-2.6.0.tgz /usr/bin
		sudo tar -xvzf kafka_2.13-2.6.0.tgz kafka_2.13-2.6.0
		cd kafka_2.13-2.6.0/bin
		
		

## MISC
Network Adapters https://www.nakivo.com/blog/virtualbox-network-setting-guide/			



