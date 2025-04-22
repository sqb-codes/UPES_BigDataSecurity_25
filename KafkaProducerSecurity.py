# Kafka Producer with kerberos authentication

# pip install confluent-kafka
from confluent_kafka import Producer

config = {
    "security.protocol": "SASL_PLAINTEXT",
    "ssl.mechanism": "GSSAPI",
    "sasl.jaas.config": "org.apache.kafka.common.security.kerberos.KerberosLoginModule required" 
    "serviceName='kafka'"
    "principal='kafka/my-broker@REALM'"
    "keyTab='/path/keyTab';",
    'bootstrap.servers' : "kafka.server:9092"
}

# "security.protocol": "SASL_PLAINTEXT"
# settings to define security protocol to use for communication b/w kafka client and broker
# SASL_PLAINTEXT - Simple Authentication and Security Layer
# Communication will be in plain text, but authentication is still done securely

# "ssl.mechanism": "GSSAPI"
# It specifies the SASL mechanism to be used for authentication
# GSSAPI - Generic Security Service Application Programming Interface


# "sasl.jaas.config"
# JAAS - Java Authentication and Authorization Service

producer = Producer(config)

def delivery_report(error, msg):
    if error is not None:
        print(f"Failed to deliver message : {error}")
    else:
        print(f"Message delivered : {msg.topic()}, {msg.partition()}")

producer.produce('test_topic', key='key', value='value', callback=delivery_report)
producer.flush()