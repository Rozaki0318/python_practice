import http.server


Handler = http.server.CGIHTTPRequestHandler
# socketserverでCGIHTTPRequestHandler使うとエラーでcgi実行に失敗した。

with http.server.HTTPServer(('127.0.0.1', 8001), Handler) as httpd:
    print("serving at port", 8001)
    httpd.serve_forever()