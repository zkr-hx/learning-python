import sys
import keyword
from platform import python_version

'''
测试输出语句
测试输出列表
测试数学运算
'''
"""
测试输出语句
测试输出列表
测试数学运算
"""
print("Hello Python", "zkr", "test")
list1 = ["a", "b", "c"]
print(list1)
rr = 1 // 2
print(-1 // 2)
print('Python', python_version())
# 打印Python中全部保留字
print(keyword.kwlist)

isTrue = False
if isTrue:
    print("True")
else:
    print("False")
    print("Error")

one = 1
two = 2
three = 3
total = one + \
        two + \
        three
print(total)

total = ['one', 'two', 'three',
         'four']
print(total)

num1: int = 1
bool1: bool = True
float1: float = 1.23
# 复数
complex1: complex = 1 + 2j
print(num1, bool1, float1, complex1)

word = '字符串'
sentence = "这是一个句子"
paragraph = """这是一个段落，
可以由多行组成"""
print(word, sentence, paragraph)

str1 = '123456789'
# 输出字符串
print(str1)
# 输出第一个到倒数第二个的所有字符
print(str1[0:-1])
# 输出字符串第一个字符
print(str1[0])
# 输出从第三个开始到第五个的所有字符
print(str1[2:5])
# 输出从第三个开始后的所有字符
print(str1[2:])
# 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str1[1:5:2])
# 输出字符串两次
print(str1 * 2)
# 连接字符串
print(str1 + '你好')

print('----------------------------------')

# 使用反斜杠（\）+n转义特殊字符
print('hello\nrun')
# 在字符串前面添加一个r，表示原始字符串，不会发生转义
print(r'hello\nrun')

# input("\n\n按下enter键后退出。")
print('---------------------------------')


x = 'run'
sys.stdout.write(x + '\n')

num2: int = 1
if 2 < num2 < 4:
    print("大于2小于4")
elif num2 >= 4:
    print("大于等于4")
else:
    print("小于等于2")

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print("-----------------------")
# 不换行输出
print(x, end=",")
print(y, end="")
print()

print("================Python import mode===========================")
print("命令行参数为：")
for i in sys.argv:
    print(i)
print("\npython 路劲为", sys.path)

print("======数据类型-整数======")
a = 10_000_000_000
b = 10000000000
print("十亿：", a, b)

print("======数据类型-浮点型======")
a = 1.23e9
b = 12.3e8
c = 0.000012
d = 1.2e-5
print(a, b)
print(a == b)
print(c, d)
print(c == d)

print("======数据类型-字符串======")
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
print('I\'m OK')
print('I\'m learning\npython')
print('\\\n\\')

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print("\\\t\\")
print(r"\\\t\\")
print('''
line1
line2
line3
''')

a = None
print(a)

