age = input('请输入你的年龄:')

print(type(age), age)   # <class 'str'> 18

# 需求,将字符串的 18 转换为 int 类型的 18
new_age = int(age)  # 数据类型转换不会改变 age 的类型, 生成一个新的数据保存到 new_age
print(type(age), age)   # <class 'str'> 18
print(type(new_age), new_age)  # <class 'int'> 18
