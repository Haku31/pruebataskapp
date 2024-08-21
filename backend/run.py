import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

import tornado.ioloop
import tornado.web
from app.main import make_app  

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()