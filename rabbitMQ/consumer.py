# -*- coding: UTF-8 -*-
# created by Long on 2022/7/20 13:06
# @Software : PyCharm
import pika
queue = 'queue_test'
hostname = 'localhost'
port = 5672

Credentials = pika.PlainCredentials('guest', 'guest')

ConnectionParam = pika.ConnectionParameters(host=hostname, port=port, credentials=Credentials)

Connection = pika.BlockingConnection(parameters=ConnectionParam)

# 连接建立成功后，建立通道
channel = Connection.channel()

# 创建exchange
channel.queue_declare(queue=queue, durable=True)


# 接受数据
def call_back(ch, method, properties, body):
    print(" [x] Received %r" % (body, ))
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送ack消息


# 告诉RabbitMQ使用call_back来接受数据
channel.basic_consume(queue=queue, on_message_callback=call_back, auto_ack=False)

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
