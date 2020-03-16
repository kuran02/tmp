def draw(fromx,fromy,toxx,toyy):
    global a,f,gcount,xcur,tox,ycur,toy,mark
    a.set_xticks([])
    a.set_yticks([])
    a.set_xlabel('x')
    a.set_ylabel('y',rotation=0)
    if gcount==0:
        for col in range(0,num_cols):
            for row in range(0,num_rows):
                cell_data = M[col,row]
                for i in range(10*col+2,10*col+8):
                    image[i,range(10*row+2,10*row+8)] = 255
                if cell_data[0] == 1: 
                    image[range(10*col+2,10*col+8),10*row] = 255
                    image[range(10*col+2,10*col+8),10*row+1] = 255
                if cell_data[1] == 1: 
                    image[10*col,range(10*row+2,10*row+8)] = 255
                    image[10*col+1,range(10*row+2,10*row+8)] = 255
                if cell_data[2] == 1: 
                    image[range(10*col+2,10*col+8),10*row+9] = 255
                    image[range(10*col+2,10*col+8),10*row+8] = 255
                if cell_data[3] == 1: 
                    image[10*col+9,range(10*row+2,10*row+8)] = 255
                    image[10*col+8,range(10*row+2,10*row+8)] = 255
                gcount=1   
    for j in range(3,7):
        for k in range(3,7):
            image[j+10*fromx,k+10*fromy]=imagepre[j,k]
    for j in range(3,7):
        for k in range(3,7):
            imagepre[j,k]=image[10*toxx+j,10*toyy+k]
            image[10*toxx+j,10*toyy+k]=200
         
#炸弹：深蓝，150；传送门： 78，蓝；角色：200，绿；地面，黄，255；墙，黑，0
    #f.clear()
    a.clear()
    a.set_xticks([])
    a.set_yticks([])
    a.set_xlabel('x')
    a.set_ylabel('y',rotation=0)
    a.imshow(image)        
    canvas.draw()    
    canvas.get_tk_widget().pack()
    #canvas.get_tk_widget().place(x=0,y=250)
    a.set_xticks([])
    a.set_yticks([])
    a.set_xlabel('x')
    a.set_ylabel('y',rotation=0)
    if mark==0:
        xcur=tox
        ycur=toy
#