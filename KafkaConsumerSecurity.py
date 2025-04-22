from confluent_kafka import Consumer, KafkaError

config = {
    "security.protocol": "SASL_PLAINTEXT",
    "ssl.mechanism": "GSSAPI",
    "sasl.jaas.config": "org.apache.kafka.common.security.kerberos.KerberosLoginModule required" 
    "serviceName='kafka'"
    "principal='kafka/my-broker@REALM'"
    "keyTab='/path/keyTab';"
}

consumer = Consumer(config)
consumer.subscribe(['test_topic'])

while True:
    msg = consumer.poll(2)
    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print(f"End of Partition reached {msg.topic()/msg.partition()}")
        else:
            print(msg.error())
            break
    else:
        print("Consumed message : ", msg.value().decode("utf-8"))

consumer.close()