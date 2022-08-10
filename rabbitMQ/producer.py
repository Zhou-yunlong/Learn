# -*- coding: UTF-8 -*-
# created by Long on 2022/7/20 13:06
# @Software : PyCharm
import json
import time
import pika

# 队列名称
queue = 'queue_test'
# 路由关键字
routing_key = 'hello'
# 消息交换机名称
exchange = 'exchange_test'

# 建立连接
hostname = '127.0.0.1'
port = 5672

Credentials = pika.PlainCredentials('guest', 'guest')

Connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname,
        port=port,
        virtual_host='/',
        credentials=Credentials
    )
)

# 连接建立成功后，建立通道
channel = Connection.channel()

# 创建exchange
channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)

# 声明队列，生产者和消费者都要声明同一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
channel.queue_declare(queue=queue, durable=True)

# 把队列和消息交换机绑定
channel.queue_bind(queue=queue, exchange=exchange, routing_key=routing_key)
# 交换机：队列名，写明将消息发往哪个队列；消息内容
# routing_key在使用匿名交换机的时候才需要指定，表示发送到哪个队列，注意当未定义exchange时，routing_key需和queue的值保持一致
for i in range(20):
    data = f'hello word{i}'
    time.sleep(2)
    # 将properties参数设置好即可让队列中的消息持久化
    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=data, properties=pika.BasicProperties(delivery_mode=2))
    print(f'发送。。。。{i}')

Connection.close()