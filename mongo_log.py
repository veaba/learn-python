import re
import sys
from datetime import datetime

# ip_list
ip_list = []
port_list = []


# 静态解析行文件
def parser_line(line):
    pattern_ip_port = re.compile(r'^.*from (.+?) \(\d .*$')  # ['1.202.68.84:40992 #6238']
    ip_port = pattern_ip_port.findall(line)
    str_ip_port = ''.join(ip_port)
    ip = re.sub(r':.*$', "", str_ip_port)  # 1.202.68.84
    port = re.sub(r'^.*:(.+?) #', '', str_ip_port)  # 40992
    ip_list.append(ip)
    port_list.append(port)


#  封装解析函数为一个类
class DataVAIMongoLog:

    # log_path mongodb的log文件路径
    # dataV_obj 表示需要加载的对象值，一般为list结构
    def __init__(self, argv):
        self.argv = argv
        try:
            argv[1]
        except IndexError as err:
            print("===", err, " ===")
            print("=== 请为python脚本传入路径参数 ===")
            exit(1)
        self.mongo_log_path = argv[1]
        try:
            path_name_list = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.yml'
            with open(self.mongo_log_path, "r", errors="ignore") as f:
                for line in f:
                    parser_line(line)
                # 判断是否需要去重
                self.is_all()
                # 去重文件
                set_ip_list = list(set(ip_list))
                set_port_list = list(set(port_list))

                # 写出ip列表yml文件
                with open(self.mongo_log_path + '-ip--list--' + path_name_list, 'w') as ip_f:
                    for ip in set_ip_list:
                        if len(ip) != 0:
                            ip_f.write(ip + '\n')
                print("=== " + self.mongo_log_path + '-port--list--' + " export Successful  ===")
                # 写出port列表yml文件
                with open(self.mongo_log_path + '-port--list--' + path_name_list, 'w') as port_f:
                    for port in set_port_list:
                        if len(port) != 0:
                            port_f.write(port + '\n')
                print("=== " + self.mongo_log_path + '-port--list--' + " export Successful ===")
                exit(1)
        # 文件没发现错误
        except FileNotFoundError as err:
            print("解析的文件路径不存在：", err)

    # 如果参数带有 --all，则不去重，默认去重
    def is_all(self):

        pass
        try:
            has_set = "--all" in self.argv
            if not has_set:
                # 导出所有数据
                path_name_all = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.yml'
                with open(self.mongo_log_path + '-ip--all--' + path_name_all, "w") as all_ip_f:
                    for all_ip in ip_list:
                        if len(all_ip):
                            all_ip_f.write(all_ip + '\n')
                print("=== " + self.mongo_log_path + '-ip--all--' + " export Successful  ===")
                with open(self.mongo_log_path + '-port--all--' + path_name_all, "w") as all_port_f:
                    for all_port in port_list:
                        if len(all_port):
                            all_port_f.write(all_port + '\n')
                print("=== " + self.mongo_log_path + '-port--all--' + " export Successful  ===")
                exit(1)
        except ValueError:
            print("has_set_err:", ValueError)


dataV_ai_init_log = DataVAIMongoLog(sys.argv)
