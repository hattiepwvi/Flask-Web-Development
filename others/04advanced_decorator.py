## Advanced Python Decorator Functions（能传参）
   # 向被装饰的函数传递参数、在调用函数前添加条件（对比初级的直接调用函数）
   # *args 任意数量的参数（元组），**kwargs 任意数量的关键字参数（字典）

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("angela")
new_user.is_logged_in = True
create_blog_post(new_user)