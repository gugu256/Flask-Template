from flask import Flask
app = Flask('')

@app.route('/')
def home():
    return "AY0"

def run():
  app.run(host='0.0.0.0',port=8080)

run()