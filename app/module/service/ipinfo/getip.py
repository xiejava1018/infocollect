# -*- coding: utf-8 -*-
"""
    :author: XieJava
    :url: http://ishareread.com
    :copyright: © 2019 XieJava <xiejava@ishareread.com>
    :license: MIT, see LICENSE for more details.
"""
import socket

import IPy

def checkip(address):
    try:
        version = IPy.IP(address).version()
        if version == 4 or version == 6:
            return True
        else:
            return False
    except Exception as e:
        return False


def getIPbyDomain(domain):
    addr=''
    try:
        myaddr = socket.getaddrinfo(domain, 'http')
        addr=myaddr[0][4][0]
    except Exception as e:
        print(e)
    return addr


if __name__=='__main__':
    ipinfo=getIPbyDomain('sohu.com')
    print(checkip('0.0.0.0'))
    print(ipinfo)