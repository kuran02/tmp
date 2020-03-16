#
def bomb():
    global cnt,node,edge,gcount
    if gcount==0:
        return 
    t1_b=Toplevel()
    v1_b=StringVar()
    v2_b=StringVar()
    def d1_b():
        global xs_b,ys_b
        xs_b=int(v1_b.get())
        ys_b=int(v2_b.get())
        mapp[ys_b][xs_b]=3
        for i in range(10*xs_b+3,10*xs_b+7):
            for j in range(10*ys_b+3,10*ys_b+7):
                image[j,i]=150
        draw(xcur,ycur,xcur,ycur)
        temp1=node[ys_b][xs_b]
        for i in range(num_cols):
            for j in range(num_rows):
                edge[temp1][node[i][j]]=65
                edge[node[i][j]][temp1]=65           
        check()
        t1_b.destroy()
    l1_b=Label(t1_b,text="放置位置(x):0-x",width=20,height=2)
    e1_b=Entry(t1_b,textvariable=v1_b)
    l2_b=Label(t1_b,text="放置位置(y):0-y",width=20,height=2)
    e2_b=Entry(t1_b,textvariable=v2_b)
    b1_b=Button(t1_b,text="OK",command=d1_b)
    l1_b.pack(),e1_b.pack(),l2_b.pack(),e2_b.pack(),b1_b.pack()
def gate():
    global t1_g,v1_g,v2_g,v3_g,v4_g,doorx1,doorx2,gcount
    if gcount==0:
        return
    t1_g=Toplevel()
    v1_g=StringVar()
    v2_g=StringVar()
    v3_g=StringVar()
    v4_g=StringVar()
    def d1_g():        
        xs=int(v1_g.get())
        ys=int(v2_g.get())
        xe=int(v3_g.get())
        ye=int(v4_g.get()) 
        edge[node[ys][xs]][node[ye][xe]]=0 ##
        edge[node[ye][xe]][node[ys][xs]]=0
        for i in range(10*xs+3,10*xs+7):
            for j in range(10*ys+3,10*ys+7):
                image[j,i]=80#imagepre=...
        for i in range(10*xe+3,10*xe+7):
            for j in range(10*ye+3,10*ye+7):
                image[j,i]=80
        if xcur==xe and ycur==ye or xcur==xs and ycur==ys:
            for j in range(3,7):###     
                for k in range(3,7):
                    imagepre[j,k]=image[10*xcur+j,10*ycur+k]
                    image[10*xcur+j,10*ycur+k]=200###
        doorx1.append((ys,xs))
        doorx2.append((ye,xe))
        doorx1.append((ye,xe))
        doorx2.append((ys,xs))
        check()
        t1_g.destroy()
    l1_g=Label(t1_g,text="起始位置(x):0-x",width=20,height=2)
    e1_g=Entry(t1_g,textvariable=v1_g)
    l2_g=Label(t1_g,text="起始位置(y):0-y",width=20,height=2)
    e2_g=Entry(t1_g,textvariable=v2_g)
    l3_g=Label(t1_g,text="结束位置(x):0-x",width=20,height=2)
    e3_g=Entry(t1_g,textvariable=v3_g)
    l4_g=Label(t1_g,text="结束位置(y):0-y",width=20,height=2)
    e4_g=Entry(t1_g,textvariable=v4_g)
    b1_g=Button(t1_g,text="OK",command=d1_g)
    l1_g.pack(),e1_g.pack(),l2_g.pack(),e2_g.pack(),l3_g.pack(),e3_g.pack(),l4_g.pack(),e4_g.pack()
    b1_g.pack()
#
def move(event): 
    global edge,node,xcur,ycur,tox,toy
    k=repr(event.char)[1]#
    if k=='a'and ycur!=0 and edge[node[xcur][ycur]][node[xcur][ycur-1]]!=65536:
        toy=ycur-1
        check()
    elif k=='w'and xcur!=0 and edge[node[xcur][ycur]][node[xcur-1][ycur]]!=65536:
        tox=xcur-1
        check()
    elif k=='d'and ycur!=num_rows-1 and edge[node[xcur][ycur]][node[xcur][ycur+1]]!=65536:
        toy=ycur+1
        check()
    elif k=='s'and xcur!=num_cols-1 and edge[node[xcur][ycur]][node[xcur+1][ycur]]!=65536:
        tox=xcur+1
        check()