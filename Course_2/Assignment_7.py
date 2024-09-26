# 图⽚展示GUI。要求：
# 点击选择图⽚并展示
# 点击Run按钮，进⾏图⽚翻转
# 展示在右侧


import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("图片展示GUI")
root.geometry('1200x600')

# 加载图片
image_in = Image.open("C:\\Users\\jiang\\Desktop\\grad0\\CatDogSmall\\test\\cats\\cat.1500.jpg")
photo = ImageTk.PhotoImage(image_in)

# 第一个Label用于显示原始图片
label_original = Label(root, image=photo)
label_original.place(x=100, y=50, width=400, height=400)

# 初始时，翻转后的图片Label不显示（或显示为空图片）
photo_flipped = None
label_flipped = Label(root)  # 初始时不设置图片
label_flipped.place(x=550, y=50, width=400, height=400)


def turnover():
     # 翻转图片
     change = image_in.transpose(Image.FLIP_LEFT_RIGHT)
     # 创建一个新的PhotoImage对象
     newphoto = ImageTk.PhotoImage(change)
     # 更新翻转图片Label的图片
     label_flipped.config(image=newphoto)
     # 必须保持对PhotoImage对象的引用，否则图片会消失
     global photo_flipped
     photo_flipped = newphoto

# 创建一个按钮，点击时调用turnover函数
Button(text='Run', command=turnover).place(x=550, y=500, width=100, height=40)  # 调整按钮位置以便不遮挡图片

root.mainloop()