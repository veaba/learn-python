import socket
# 建立socket 对象
s = socket.socket(
    # 这几个参数是干嘛的？TODO
    socket.AF_INET, socket.SOCK_STREAM
)
host = socket.gethostname()  # 获取本地主机名

port = 8888

s.bind((host, port))

# 设置最大连接数，超过后排队
s.listen(5)

while True:
    # 被动接受TCP客户端连接，阻塞式，等待连接的到来
    c, addr = s.accept()  # 返回的参数 ('10.0.75.1', 59939)
    print(addr)
    print("连接地址:%s" % str(addr))
    msg = "环境访问socket 服务+" + "\r\n"
    c.send(msg.encode("utf-8"))
    c.close()
