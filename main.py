import xml.etree.ElementTree as ET
import random

# 讀取XML配置
tree = ET.parse('config.xml')
root = tree.getroot()
x1 = int(root.find('x1').text)
x2 = int(root.find('x2').text)
n = int(root.find('n').text)

# 生成目標數字
target_number = random.randint(x1, x2)

# 遊戲開始
print("猜數字遊戲開始！目標數字在", x1, "和", x2, "之間。你有", n, "次猜測的機會。")

for i in range(n):
    guess = int(input("請猜一個數字: "))

    # 提供反饋
    if guess == target_number:
        print("恭喜你猜對了！")
        break
    elif guess < target_number:
        print("太低了，再試一次。")
    else:
        print("太高了，再試一次。")

    # 猜測次數用完
    if i == n - 1:
        print("很遺憾，你沒有在", n, "次內猜中。正確答案是", target_number)

