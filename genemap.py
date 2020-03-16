
def genemap():#node,edge
    global node,edge,num_cols,num_rows,M,cnt,mapp,gcount
    mapp=[[0 for i in range(num_rows)]for j in range(num_cols)]#传送、正常地图状态值
    cnt=0#node:0~cnt-1
    node=[[0 for i in range(num_rows) ]for j in range(num_cols)]
    for i in range(num_cols):
        for j in range(num_rows):
            node[i][j]=cnt
            cnt=cnt+1
    edge=[[1<<16 for i in range(cnt)] for j in range(cnt)]
    for i in range(num_cols):
        for j in range(num_rows):#0123:左上右下
            if M[i,j,0]==1 and j!=0:
                edge[node[i][j]][node[i][j-1]]=1
                edge[node[i][j-1]][node[i][j]]=1
            if M[i,j,1]==1 and i!=0:
                edge[node[i-1][j]][node[i][j]]=1
                edge[node[i][j]][node[i-1][j]]=1
            if M[i,j,2]==1 and j!=num_rows-1:
                edge[node[i][j+1]][node[i][j]]=1
                edge[node[i][j]][node[i][j+1]]=1
            if M[i,j,3]==1 and i!=num_cols-1:
                edge[node[i+1][j]][node[i][j]]=1
                edge[node[i][j]][node[i+1][j]]=1
###   
### 
def randprim():
    global num_rows,num_cols,M,xtar,ytar,image,doorx1,doorx2,layer
    global gcount,xcur,ycur,imagepre,tox,toy
    for i in range(50):
        for j in range(50):
            imagepre[i,j]=255  
    doorx1=[] 
    doorx2=[]
    xcur=0
    ycur=0
    tox=0
    toy=0
    gcount=0
    M = np.zeros((num_cols,num_rows,5), dtype=np.uint8)
    image = np.zeros((num_cols*10,num_rows*10), dtype=np.uint8)
    r = 0
    c = 0
    his = [(c,r)]
    while his: 
        c,r = random.choice(his)
        M[c,r,4] = 1
        his.remove((c,r))
        check = []
        if r > 0:#
            if M[c,r-1,4] == 1:
                check.append('L')
            elif M[c,r-1,4] == 0:
                his.append((c,r-1))
                M[c,r-1,4] = 2
        if c > 0:
            if M[c-1,r,4] == 1: 
                check.append('U') 
            elif M[c-1,r,4] == 0:
                his.append((c-1,r))
                M[c-1,r,4] = 2
        if r < num_rows-1:
            if M[c,r+1,4] == 1: 
                check.append('R')
            elif M[c,r+1,4] == 0:
                his.append((c,r+1))
                M[c,r+1,4] = 2 
        if c < num_cols-1:
            if M[c+1,r,4] == 1: 
                check.append('D') 
            elif  M[c+1,r,4] == 0:
                his.append((c+1,r))
                M[c+1,r,4] = 2
        if len(check):
            move_direction = random.choice(check)
            if move_direction == 'L':
                M[c,r,0] = 1
                r = r-1
                M[c,r,2] = 1
            if move_direction == 'U':
                M[c,r,1] = 1
                c = c-1
                M[c,r,3] = 1
            if move_direction == 'R':
                M[c,r,2] = 1
                r = r+1
                M[c,r,0] = 1
            if move_direction == 'D':
                M[c,r,3] = 1
                c = c+1
                M[c,r,1] = 1       
    M[0,0,0] = 1
    M[num_cols-1,num_rows-1,2] = 1 
    xtar=num_cols-1
    ytar=num_rows-1
    genemap()
    draw(0,0,0,0)
    frame.focus_set()
    frame.pack()
    doorx1=[] 
    doorx2=[]
    a.set_xticks([])
    a.set_yticks([])
##             
def dij(x,y):
    global cnt,path,dis,vis,p,node,edge,xcur,ycur,mapp,imagepre
    maxx=1<<16
    path=[-1]*cnt
    pathx=[]
    pathy=[]
    vis=[0]*cnt
    dis=[maxx]*cnt
    for i in range(cnt):
        dis[i]=edge[node[x][y]][i]
    vis[node[x][y]]=1#init
    for i in range(cnt):
        minn=maxx
        p=-1
        for j in range(cnt):
            if vis[j]==0 and dis[j]<minn:
                p=j
                minn=dis[j]
        if p>=0:
            vis[p]=1
        for j in range(cnt):
            if vis[j]==0 and p!=-1 and dis[p]+edge[p][j]<dis[j]:
                dis[j]=dis[p]+edge[p][j]
                path[j]=p
    p=node[num_cols-1][num_rows-1]
    cunt=0
    while p!=-1:
        xtmp=int(p/num_rows)
        ytmp=p%num_rows
        #print(xtmp,ytmp,p)
        cunt+=1
        if mapp[xtmp][ytmp]==3:
            vis[cnt-1]=0
            break
        pathx.append(xtmp)
        pathy.append(ytmp)
        p=path[p]
    pathx.reverse()
    pathy.reverse()
    xc=xcur
    yc=ycur
    tempimage=imagepre
    if vis[cnt-1]==0:
        return
    summ=1/cunt
    draw(xc,yc,pathx[0],pathy[0])
    time.sleep(summ)#0.15
    for k in range(len(pathx)-1):
        
        draw(pathx[k],pathy[k],pathx[k+1],pathy[k+1])
        time.sleep(summ)
    imagepre=tempimage
    draw(pathx[len(pathx)-1],pathy[len(pathx)-1],xc,yc)
    xcur=xc
    ycur=yc
##