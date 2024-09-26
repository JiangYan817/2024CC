# ⽂本编辑器GUI。要求：
# 添加“另存为”功能
# 底部添加状态栏，显示当前⽂本总⾏数


from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog, messagebox

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))

def update_status_bar():
    lines = contents.get('1.0', END).count('\n') + 1
    status_bar.config(text=f"文本总行数：{lines}")

# 主窗口
top = Tk()
top.title('文本编辑器GUI')
# label = Label(top, text = "文本总行数：1", anchor='s')
# label.pack(side = BOTTOM)
# 文字编辑窗口
contents = ScrolledText(top)
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
contents.bind("<<Modified>>", update_status_bar)
# 输入文件名窗口
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)
# 读取、保存窗口
Button(text='打开', command=load).pack(side=LEFT)
Button(text="保存", command=save).pack(side=LEFT)
#状态栏
status_bar = Label(top, text="文本总行数：0", anchor='s')
status_bar.pack(side=BOTTOM)

mainloop()




#
# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
# from tkinter import filedialog, messagebox
#
#
# def load():
#     filepath = filedialog.askopenfilename()
#     if filepath:
#         with open(filepath, 'r', encoding='utf-8') as file:
#             contents.delete('1.0', END)
#             contents.insert(INSERT, file.read())
#         filename_entry.delete(0, END)
#         filename_entry.insert(0, filepath)
#         update_status_bar()
#
#
# def save():
#     filepath = filename_entry.get()
#     if not filepath:
#         filepath = filedialog.asksaveasfilename(defaultextension=".txt",
#                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#     if filepath:
#         with open(filepath, 'w', encoding='utf-8') as file:
#             file.write(contents.get('1.0', END))
#         messagebox.showinfo("保存成功", "文件已成功保存至 " + filepath)
#
#
# def update_status_bar():
#     lines = contents.get('1.0', END).count('\n') + 1
#     # lines = int(self.text_area.index('end-1c').split('.')[0])
#     status_bar.config(text=f"文本总行数：{lines}")
#
#
# # 主窗口
# top = Tk()
# top.title('文本编辑器GUI')
#
# # 文字编辑窗口
# contents = ScrolledText(top)
# contents.pack(side=BOTTOM, expand=True, fill=BOTH)
#
# # 输入文件名窗口
# filename_entry = Entry(top)
# filename_entry.pack(side=LEFT, expand=True, fill=X)
#
# # 读取、保存按钮
# Button(top, text='打开', command=load).pack(side=LEFT)
# Button(top, text="保存", command=save).pack(side=LEFT)
#
# # 状态栏
# status_bar = Label(top, text="文本总行数：0", anchor='s')
# status_bar.pack(side=BOTTOM)
#
# # 绑定事件以更新状态栏
# # contents.bind("<<Modified>>", update_status_bar)
#
# contents.bind("<KeyRelease>", update_status_bar)
#
#
# mainloop()


