import tornado.ioloop
import tornado.web
from handlers.task_handler import TaskHandler


class CORSHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

def make_app():
    return tornado.web.Application([
        (r"/tasks", TaskHandler),
        (r"/tasks/([0-9a-fA-F\-]+)", TaskHandler),
    ], default_handler_class=CORSHandler)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
