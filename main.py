from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "Hello, World!"

app.run(host='0.0.0.0',port=8080)
