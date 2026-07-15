from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps<br>2026-06-15：测试向网页中新增展示内容<br>2026-06-15：你好，DevOps!<br>2026-07-15 验证Jenkins流水线"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# 2026-06-15 22:43:41 test push to github and make sure the function of webhook
# 2026-06-15 23:43:13 几分钟前，我在上面的return语句中新增了两条，push app.py后，Jenkins并没有自动构建。所以我新增了这条句子
# ---想再次验证一下webhook功能是否正常生效！
