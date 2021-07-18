from sanic import Sanic, text, json, html
from tools.cors import add_cors_headers
from api import api
from response.Response import success
from sanic_cors import CORS
# 注册中间件，虽然导入没用，但是必须导入。相当于初始化
import db.server
import exceptions.exceotionHandle

# 实例化一个Sanic对象
app = Sanic.get_app("secondhand", force_create=True)
# 解决跨域问题
cors = CORS(app, resources={r"/*": {"origins": "*"}}, automatic_options=True)
# token密钥
app.config.SECRET = "secondhand"
# token半小时有效
# app.config.EXISTTIME = 60 * 30 * 4
app.blueprint(api)
app.static("/", "./static")


@app.route('html/game/<game>', strict_slashes=True)
async def index(request, game):
    with open('./static/index.html', 'r') as f:
        response = html(f.read())
    return response


# app.register_middleware(add_cors_headers, "response")

if __name__ == "__main__":
    # 让服务运行在80端口上
    app.run(host="0.0.0.0", port=80, debug=False)
