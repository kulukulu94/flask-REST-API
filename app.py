from flask import Flask

app = Flask(__name__)

@app.route('/') #home page of the application
def home():        # name does not matter to home page it can be any name
    return "hello, world!"

app.run(port=7000)
