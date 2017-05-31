#conding=utf-8

'''
添加访问不存在页面时报错
添加handle_file() 函数，处理文件
添加handle_error() 函数
'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import os, sys

class RequestHandler(BaseHTTPRequestHandler):

    Error_Page = '''\
        <html>
	    <body>
		<h1>Error accessing {path}</h1>
		<p>{msg}</p>
	    </body>
        </html>
    '''


    # 处理一个GET请求
    def do_GET(self):
        try:
            # 文件完整路径
            # os.getcwd() 是当前的工作目录
            # self.path 保存了请求的相对路径
            full_path = os.getcwd() + self.path

            # 判断路径是否存在
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            # 如果路径是一个文件
            elif os.path.isfile(full_path):
                # 调用 handle_file 处理该文件
                self.handle_file(full_path)

            # 如果该路径不是一个文件
            else:
                # 抛出异常
                raise ServerException("Undown object '{0}'".format(self.path))

        except Exception as msg:
            self.handle_error(msg)

    # 文件处理函数
    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:       #以二进制打开文件
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = ("'{0}' connot be read: {1}".format(self.path, msg))
            self.handle_error(msg)


    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)


    def send_content(self, content, status=200):
        self.send_response(status)         # 如果正确，返回200
        self.send_header("Content-Type", "text/html")       # 定义处理的文件类型
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()              # 结束处理,插入一个空白行
        # https://stackoverflow.com/questions/23264569/python-3-x-basehttpserver-or-http-server
        self.wfile.write(content.encode('utf-8'))     # 通过wfile将下载的页面传给用户

class ServerException(Exception):
    '''服务器内部错误类'''
    pass

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)          # 启动服务
    server.serve_forever()              # 一直运行

