from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# 2026-06-15 22:43:41 test push to github and make sure the function of webhook
