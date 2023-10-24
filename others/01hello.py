from flask import Flask
import random
# 告诉Python创建一个叫做app的应用程序实例
# __name__ 是一个特殊的名字，它告诉Python当前模块（也就是你的代码文件）的名字、函数的名字。
   # 如果你在主程序文件中运行这个代码，那么__name__将会被设置成__main__，表示这是主要的程序文件。
   # 如果你在一个被其他文件导入的模块中运行这个代码，__name__将会被设置成这个模块的名字。
app = Flask(__name__)
print(__name__)
print(random.__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper



# 用户访问 / 主页时就调用 hello_world();
@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a blue cat</p>")


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def say_bye():
    return"Bye!"

# 动态路由<>
# @app.route("/username/<name>/1")
# 保留 / 等后面所有的信息：比如 ann/1
# @app.route("/username/<path:name>")
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"



if __name__ == "__main__":
    # app.run()
    # debug: 打开（自动渲染）,并返回错误信息，P55_NO426
    app.run(debug=True)