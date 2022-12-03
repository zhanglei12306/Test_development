class Cat:
    def eat(self):  # self  暂时不管
        """吃鱼的方法"""
        print('小猫爱吃鱼...')

    def drink(self):
        """喝水的方法"""
        print('小猫要喝水')


# 创建对象
tom = Cat()
# 通过对象 调用类中的方法
tom.eat()
tom.drink()




class LoginPage:

    def __init__(self, username, password, code):
        self.username = username # ⽤户名
        self.password = password # 密码
        self.verify_code = code # 验证码
    def login(self):
        print(f"1. 输⼊⽤户名: {self.username}")
        print(f"2. 输⼊密码: {self.password}")
        print(f"3. 输⼊验证码: {self.verify_code}")
        print(f"4. 点击登录")
if __name__ == '__main__':
    admin = LoginPage('admin', '123456', '8888')
    admin.login()