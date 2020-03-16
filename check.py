def check():
    global xcur,ycur,xtar,ytar,doorx1,doorx2,tox,toy,curl
    if (tox,toy) in doorx1:
        mark=1
        draw(xcur,ycur,tox,toy)
        mark=0
        time.sleep(0.15)
        tmp1=doorx2.index((tox,toy))
        tox,toy=doorx1[tmp1]#
    draw(xcur,ycur,tox,toy)
    if tox==xtar and toy==ytar and mapp[xcur][ycur]!=2 :#not bomb
        if curl==layer:
            #print(curl,layer)
            m1=messagebox.showinfo(title='提示',message='您已通过，游戏结束')
            game_in=0
        elif curl!=layer:
            #print(curl,layer)
            curl+=1
            randprim()
    elif mapp[tox][toy]==3:#
        m2=messagebox.showinfo(title='提示',message='碰到炸弹，游戏结束')
        game_in=0
#