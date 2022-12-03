# 1. 提示用户输入两个数字  input--> str
num1 = int(input('请输入数字:'))
num2 = int(input('请输入数字:'))

# 2. 使用获取到的数据进行加法运算
num = num1 + num2

# 3. 在控制台输出计算结果，格式要求:xx + xx = xx
print(f"{num1} + {num2} = {num}")
