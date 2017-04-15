#! /usr/bin/env python3
# coding = utf-8

# srv_legacy1.py - 基于标准库 SocketServer 的服务的实现

from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
import zen_utils


class ZenHandle(BaseRequestHandler):

    def handle(self):
        zen_utils.handle_conversation(self.request, self.client_address)


class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1

if __name__ == '__main__':
    address = zen_utils.parse_command_line('legacy "SocketServer" server')
    zenServer = ZenServer(address, ZenHandle)
    zenServer.serve_forever()
