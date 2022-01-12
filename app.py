# Flaskをインポート
from flask import Flask, request, render_template

#アプリのインスタンスを生成
app = Flask(__name__)

#トップページにアクセスされた時の挙動
@app.route("/")
def index():
  return "Hello from flask"

@app.route("/top")
def mypage():
  return render_template(
    "index.html",
    title="Dear G's members",
    message="Congratulation!!!"
  )

@app.route("/api/hello")
def api_hello():
  return "api_hello"

@app.route("/api/items/<int:item_id>")
def api2(item_id):
  return "item_id is %d" % item_id

# リクエストをgetで受け取る場合
@app.route("/api/users", methods=["GET"])
def api_users_get():
  search_key = request.args.get("user_id")
  return "user_id is %s" % search_key

# リクエストをpostで受け取る場合
@app.route("/api/users", methods=["POST"])
def api_users_update():
  user_name = request.form.get("user_name")
  return "user_name=%s" % (user_name)


# __main__ pythonコマンドから直接実行されたかどうかの確認
if __name__ == "__main__":
  app.run() # =>サーバーが起動する