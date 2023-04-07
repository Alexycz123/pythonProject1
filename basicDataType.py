a = True
b = False

print(2 < 3)
print(2 == 3)

print(a and b)
print(a or b)
print(not a)

print(int(a))
print(int(b))
print(float(b))
print(str(b) + str(a))

print("-------------------------------")

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
print("-------------------------------")
a = [1, 2, 3, 4, 5]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []
print(a)

print("-----------------------")


def reverseWork(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    input_words = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    input_words = input_words[-1::-1]
    # 重新组合字符串
    output = ' '.join(input_words)
    return output


print(reverseWork("I like"))

print("--------------元组-------------")
tuple = ('abcd', 876, 2.23, 'runoob', 70.2)
tiny_tuple = (123 , 'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tiny_tuple*2)
print(tuple + tiny_tuple)
