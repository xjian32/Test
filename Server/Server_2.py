#conding=utf-8

'''
运行python server_2.py，浏览器中输入：http://127.0.0.1:8080/test.html
test.html页面不存在仍可正常访问
因为web服务器中没有找不到文件就返回404错误的功能
'''

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    # 处理请求并返回页面

    # 返回的页面模板
    Page = '''\
        <html>
            <body>
                <table>
                    <tr> <td>Header</td>			<td>Value</td>			</tr>
                    <tr> <td>Date and time</td>		<td>{date_time}</td>	</tr>
                    <tr> <td>Client host</td>		<td>{client_host}</td>	</tr>
                    <tr> <td>Client port</td>		<td>{client_port}</td>	</tr>
                    <tr> <td>Command</td>			<td>{command}</td>		</tr>
                    <tr> <td>Path</td>				<td>{path}</td>			</tr>
                </table>
            </body>
        </html>
        '''

    # 处理一个GET请求
    def do_GET(self):
        page = self.create_page()
        self.send_content(page)

    def create_page(self):
        values = {
            'date_time'     : self.date_time_string(),
            'client_host'   : self.client_address[0],
            'client_port'   : self.client_address[1],
            'command'       : self.command,
            'path'          : self.path
        }
        page = self.Page.format(**values)
        return page

    def send_content(self, page):
        self.send_response(200)         # 如果正确，返回200
        self.send_header("Content-Type", "text/html")       # 定义处理的文件类型
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()              # 结束处理,插入一个空白行
        # https://stackoverflow.com/questions/23264569/python-3-x-basehttpserver-or-http-server
        self.wfile.write(page.encode('utf-8'))     # 通过wfile将下载的页面传给用户

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)          # 启动服务
    server.serve_forever()              # 一直运行

