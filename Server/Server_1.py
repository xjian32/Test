#conding=utf-8

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    # 处理请求并返回页面

    # 返回的页面模板
    Page = '''\
        <html>
        <body>
        <p>Hello,Web!</p>
        </body>
        </html>
    '''

    # 处理一个GET请求
    def do_GET(self):
        self.send_response(200)         # 如果正确，返回200
        self.send_header("Content-Type", "text/html")       # 定义处理的文件类型
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()              # 结束处理,插入一个空白行
        # https://stackoverflow.com/questions/23264569/python-3-x-basehttpserver-or-http-server
        self.wfile.write(self.Page.encode('utf-8'))     # 通过wfile将下载的页面传给用户

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)          # 启动服务
    server.serve_forever()              # 一直运行

