#创新点：最短路以可视化方式实现，参数可自行设置，增加了层数的设定
from tkinter import *
from tkinter import messagebox
import time
import sys
import matplotlib
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#初始环境
global num_rows,num_cols,xtar,ytar,gcount,xcur,ycur,tox,toy,doorx1,doorx2,layer
tox=0
toy=0
gcount=0
game_in=0
mark=0
layer=1
curl=1#当前层
imagepre=np.zeros((5*10,5*10), dtype=np.uint8)
for i in range(50):
    for j in range(50):
        imagepre[i,j]=255
t1=Tk()
t1.title("Nonsense Maze")
f=Figure(figsize=(8,4.5),dpi=100)
f.set_facecolor('Beige')
a=f.add_subplot(1,1,1)
canvas=FigureCanvasTkAgg(f,master=t1)
frame=Frame(t1,width=1,height=1)

## randprim
def init():
    global num_rows,num_cols,M,xtar,ytar,image,doorx1,doorx2,layer,curl
    global gcount,xcur,ycur,imagepre,tox,toy
    for i in range(50):
        for j in range(50):
            imagepre[i,j]=255            
    t1_i=Toplevel()
    v1_i=StringVar()
    v2_i=StringVar()
    v3_i=StringVar()
    curl=1
    xcur=0
    ycur=0
    tox=0
    toy=0
    #layer=1
    gcount=0
    def d1_i():
        global num_rows,num_cols,M,xtar,ytar,image,doorx1,doorx2,layer
        num_rows=int(v1_i.get())
        num_cols=int(v2_i.get())
        tmp=v3_i.get()
        if tmp!='':
            layer=int(tmp)
            #print(layer)
        randprim()
        t1_i.destroy()
    l1_i=Label(t1_i,text="Rows(x):",width=10,height=2)
    e1_i=Entry(t1_i,textvariable=v1_i)
    l2_i=Label(t1_i,text="Columns(y):",width=10,height=2)
    e2_i=Entry(t1_i,textvariable=v2_i)
    l3_i=Label(t1_i,text="Layer:(默认为1)",width=15,height=2)
    e3_i=Entry(t1_i,textvariable=v3_i)
    b1_i=Button(t1_i,text="OK",command=d1_i)
    l1_i.pack(),e1_i.pack(),l2_i.pack(),e2_i.pack(),l3_i.pack(),e3_i.pack(),b1_i.pack()

def hint():
    global prex,prey,vis,gcount
    if gcount==0:
        return 
    xtar=num_rows-1
    ytar=num_cols-1
    dij(xcur,ycur)
    if vis[cnt-1]==0:
        m3=messagebox.showinfo(title='提示',message='当前迷宫无解')#无解
        return 
def quit1():
    t1.destroy()
#gui
xcur=0
ycur=0
tox=0
toy=0
#t1.geometry("800x700")
b1=Button(t1,text='开始/重新开始',command=init)
b2=Button(t1,text="提示(演示)",command=hint)
b3=Button(t1,text="添加传送门",command=gate)
b5=Button(t1,text='添加炸弹',command=bomb)
label1=Label(t1,text='Nonsense Maze',font=("Calibri",20),width=40,height=2,background='Beige')
label2=Label(t1,text='操作:wasd',font=("Calibri",12),width=40,height=2,background='Beige')
b4=Button(t1,text="退出",command=quit1)

#label1.pack()
label1.place(x=126,y=10)
label2.place(x=240,y=60)
b1.place(x=360,y=100)
b2.place(x=370,y=140)
b3.place(x=369,y=180)
b4.place(x=386,y=260)
b5.place(x=372,y=220)

label1.pack(),label2.pack(),b1.pack(),b2.pack(),b3.pack(),b4.pack(),b5.pack()
#

frame.bind("<Key>",move)
frame.focus_set()
t1.configure(background='Beige')
t1.mainloop()
#
