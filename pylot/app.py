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
    
app = web.application(urls,globals())

if __name__ == '__main__':
    app.run()