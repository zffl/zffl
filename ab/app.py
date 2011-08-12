import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        print web.input()
        return 'get'
    def POST(self):
        print web.data()
        return 'post'