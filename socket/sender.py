#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
author: gadfy
content: data exchange bridge
"""

import zlib
import struct
import json
import socket
from messager import Messager

class RobotSocket(object):
    def __init__(self, addr=('192.168.51.31',8888)):
        #创建客户端socket对象
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #服务端IP地址和端口号元组
        self.server_address = addr 
        #客户端连接指定的IP地址和端口号
        self.socket.connect(self.server_address)
        self.count = 0
        self.msg = Messager()

    def sendall(self, data_type, data):
        sdata = self.msg.pack(data_type, data)
        self.socket.sendall(sdata)

    def rev(self):
        pass

    def __del__(self):
        self.socket.close()


if __name__ == "__main__":
    data = {"key":"value","size":10}
    data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.289000004529953, 0.28499999642372131, 0.28099998831748962, 0.27799999713897705, 0.27399998903274536, 0.25, 0.24899999797344208, 0.24899999797344208, 0.24899999797344208, 0.2460000067949295, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.23800000548362732, 0.23899999260902405, 0.0, 0.23800000548362732, 0.23800000548362732, 0.2370000034570694, 0.23499999940395355, 0.23399999737739563, 0.23299999535083771, 0.23299999535083771, 0.2370000034570694, 0.23800000548362732, 0.23899999260902405, 0.23899999260902405, 0.24300000071525574, 0.23800000548362732, 0.22100000083446503, 0.21799999475479126, 0.21699999272823334, 0.21699999272823334, 0.22599999606609344, 0.0, 0.24699999392032623, 0.0, 0.25799998641014099, 0.25699999928474426, 0.25600001215934753, 0.25999999046325684, 0.28200000524520874, 0.28099998831748962, 0.28200000524520874, 0.28299999237060547, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9649999737739563, 0.95099997520446777, 0.95399999618530273, 0.95499998331069946, 0.95800000429153442, 0.96200001239776611, 0.96399998664855957, 0.9660000205039978, 0.96700000762939453, 0.97100001573562622, 0.97399997711181641, 0.0, 0.97600001096725464, 0.9779999852180481, 0.98199999332427979, 0.98500001430511475, 0.98600000143051147, 0.99000000953674316, 0.99400001764297485, 0.99800002574920654, 1.0019999742507935, 1.0049999952316284, 1.0069999694824219, 1.0119999647140503, 1.0169999599456787, 1.0219999551773071, 1.0260000228881836, 1.0290000438690186, 1.031000018119812, 1.0390000343322754, 1.0429999828338623, 1.0440000295639038, 1.0509999990463257, 1.0579999685287476, 1.062999963760376, 1.0679999589920044, 1.0720000267028809, 1.0800000429153442, 0.0, 4.0469999313354492, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.8570001125335693, 3.8159999847412109, 3.5769999027252197, 3.565000057220459, 3.5799999237060547, 0.0, 0.0, 1.5060000419616699, 1.5089999437332153, 1.4939999580383301, 1.4830000400543213, 1.5010000467300415, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.8460001945495605, 0.0, 4.4660000801086426, 0.0, 0.0, 4.434999942779541, 0.0, 0.0, 3.2679998874664307, 0.0, 0.0, 3.2569999694824219, 3.2679998874664307, 3.3340001106262207, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.41299998760223389, 0.3880000114440918, 0.38899999856948853, 0.37900000810623169, 0.37000000476837158, 0.3580000102519989, 0.34999999403953552, 0.34000000357627869, 0.33199998736381531, 0.32400000095367432, 0.31000000238418579, 0.30199998617172241, 0.29699999094009399, 0.29100000858306885, 0.27799999713897705, 0.27099999785423279, 0.26800000667572021, 0.26499998569488525, 0.26399999856948853, 0.26600000262260437, 0.0, 0.2669999897480011, 0.26800000667572021, 0.26899999380111694, 0.27000001072883606, 0.27099999785423279, 0.2720000147819519, 0.27399998903274536, 0.27399998903274536, 0.27599999308586121, 0.27700001001358032, 0.27799999713897705, 0.27900001406669617, 0.28099998831748962, 0.28200000524520874, 0.28400000929832458, 0.28499999642372131, 0.28700000047683716, 0.28799998760223389, 0.28999999165534973, 0.29199999570846558, 0.29300001263618469, 0.29499998688697815, 0.0, 0.29699999094009399, 0.29800000786781311, 0.30099999904632568, 0.30199998617172241, 0.30399999022483826, 0.30700001120567322, 0.30899998545646667, 0.31099998950958252, 0.31299999356269836, 0.31499999761581421, 0.31799998879432678, 0.31999999284744263, 0.32199999690055847, 0.32400000095367432, 0.32800000905990601, 0.33000001311302185, 0.33300000429153442, 0.335999995470047, 0.33899998664855957, 0.34200000762939453, 0.34400001168251038, 0.34799998998641968, 0.35100001096725464, 0.35499998927116394, 0.3580000102519989, 0.0, 0.3619999885559082, 0.36500000953674316, 0.36899998784065247, 0.37299999594688416, 0.37599998712539673, 0.38100001215934753, 0.38400000333786011, 0.38899999856948853, 0.39300000667572021, 0.39800000190734863, 0.40299999713897705, 0.40700000524520874, 0.41299998760223389, 0.41800001263618469, 0.42300000786781311, 0.0, 0.42899999022483826, 0.43399998545646667, 0.44100001454353333, 0.44600000977516174, 0.45300000905990601, 0.46000000834465027, 0.46700000762939453, 0.47400000691413879, 0.48100000619888306, 0.48800000548362732, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.49399998784065247, 0.49200001358985901, 0.50199997425079346, 0.51599997282028198, 0.5350000262260437, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.53899997472763062, 0.52300000190734863, 0.0, 0.52999997138977051, 0.52700001001358032, 0.51399999856948853, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.40000000596046448, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3049999475479126, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.37299999594688416, 0.0, 0.0, 0.0, 0.62900000810623169, 0.58300000429153442, 0.57400000095367432, 0.56400001049041748, 0.55099999904632568, 0.5429999828338623, 0.53799998760223389, 0.53200000524520874, 0.52899998426437378, 0.52100002765655518, 0.51599997282028198, 0.51099997758865356, 0.49900001287460327, 0.0, 0.0, 0.51099997758865356, 0.0, 0.0, 0.0, 2.7109999656677246, 2.6940000057220459, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.1410000324249268, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.3910000324249268, 1.3890000581741333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    sock = RobotSocket()
    sock.sendall(1, data)
    sock.socket.close()