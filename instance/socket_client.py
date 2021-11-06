import socket
from datetime import datetime
import time


def timer(n):
    while True:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 获取本地主机名
        host = socket.gethostname()
        port = 8888
        print(host, port)
        c.connect((host, port))
        msg = c.recv(1024)
        c.close()
        print(msg.decode("utf-8"))
        time.sleep(n)


timer(2)
