#!/usr/bin/env python
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
        <html>
          <title>Hello, World!</title>
          <body>
            <h2>Hello, World!</h2>
            <b>Host:</b> {host}
            <br/>
          </body>
        </html>
    """.format(host=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
