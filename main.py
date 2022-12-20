from flask import Flask
from threading import Thread
from flask import render_template

app = Flask('')

@app.route('/')
def hello():
    return render_template('index.html')

def run_script():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target = run_script)
  t.start()

if __name__ == '__main__':
  keep_alive()