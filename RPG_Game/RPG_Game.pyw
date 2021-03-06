import time
import sys
import pygame
import _thread
import easygui as gui
import os
from pygame.locals import *
jd=0
p=True
down_bool=True
sleep_timer=False
Temp=True
lock=_thread.allocate_lock()
lock.acquire()
text=""
index=0
stop=False
answer={'answer':0.0,'que':False}
def question(quenum):
     if quenum == 0:
        answer['answer'] = float(gui.enterbox(msg='你遇到了新手怪,已知新手怪最大能承受的压强是1000kPa,你身旁有一个东西,这个东西的最小接触面积是100mm^2,你现在没啥力气必须使出一个刚好的力才能保证不死,你需要用多少力?', title='question', default='0', strip=True, image=None, root=None))
        answer['que'] = True
def dtext(txt,ts):
    global text
    for t in txt:
        text=text + t
        if stop:
            return
        time.sleep(ts)
        if stop:
            return
def sleep(s):
    global sleep_timer
    sleep_timer=False
    time.sleep(s)
    sleep_timer=True
pygame.init()
size=width,height=670,370
screen=pygame.display.set_mode(size)
color=(0,0,0)
before_1=pygame.image.load("一段公路.png")
before_2=pygame.image.load("楼房.png")
before_3=pygame.image.load("草地.png")
sp_1=pygame.image.load("角色1.png")
sp_2=pygame.image.load("jo护车.png")
p_1=pygame.image.load("对话框.png")
p_2=pygame.image.load("继续.png")
sp_3=pygame.image.load("新手怪.png")
sp_1=pygame.transform.scale(sp_1,(int(sp_1.get_rect()[2]/3),int(sp_1.get_rect()[3]/3)))
p_1=pygame.transform.scale(p_1,(int(p_1.get_rect()[2]/1.25),int(p_1.get_rect()[3]/1.25)))
_l=0
x=0
y=210
i=0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            lock.release()
            pygame.quit()
            sys.exit("0")
        if jd==0:
            if (event.type == MOUSEMOTION)or(event.type == MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (mouse_x>(x+22))and(mouse_x<(x+562)):
                    if (mouse_y>(y-106))and(mouse_y<(y+44)):
                       try:
                           if (event.buttons)[0]:
                               print(event)
                               i+=1
                       except:
                           if event.button==1:
                               print(event)
                               i+=1
        if jd==1:
            if down_bool:
                if (event.type == MOUSEMOTION)or(event.type == MOUSEBUTTONDOWN):
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (mouse_x>(x-140))and(mouse_x<(x+562-140)):
                        if (mouse_y>(y-106+50))and(mouse_y<(y+50)):
                            try:
                                if (event.buttons)[0]:
                                    print(event)
                                    _l+=1
                                    _thread.start_new_thread(sleep,(2,))
                                    x=335
                                    y=185
                                    Temp=True
                                    stop=True
                            except:
                                if event.button==1:
                                    print(event)
                                    _l+=1
                                    _thread.start_new_thread(sleep,(2,))
                                    x=335
                                    y=185
                                    Temp=True
                                    stop=True
    screen.fill(color)
    if jd==0:
        if Temp:
            _thread.start_new_thread(sleep,(1,))
            Temp=False
        screen.fill(color)
        screen.blit(before_1,(0,206))
        screen.blit(before_2,(0,0))
        screen.blit(before_2,(135,0))
        screen.blit(before_2,(270,0))
        screen.blit(before_2,(405,0))
        screen.blit(before_2,(540,0))
        screen.blit(sp_1,(x,y))
        if sleep_timer:
            if p:
                screen.blit(p_1,(x+22,y-106))
                screen.blit(p_2,(x+390,y-40))
                font=pygame.font.Font("方正像素12.TTF",20)
                distext=font.render(text,1,(0,0,0))
                screen.blit(distext,(x+35,y-90))
            if _l==0:
                if i == 0:
                    _thread.start_new_thread(dtext,("那天，我只是受不了阿妈啰嗦，谁知道……",0.1))
                    i+=1
                if i == 2:
                    _l+=1
            if _l==1:
                text=""
                p=False
                screen.blit(sp_2,(675-index,y-40))
                index+=1
                if (675-index-20)<=x:
                    kt=False
                    i=0
                    _l=0
                    Temp=True
                    jd+=1
                    _thread.start_new_thread(sleep,(1,))
                sleep(0.0001)
    if jd == 1:
        if (_l == 1)or(_l <= 3):
            screen.blit(before_3,(0,0))
        if sleep_timer:
            if _l == 0:
                screen.blit(p_1,(x+22,y-106))
                screen.blit(p_2,(x+390,y-40))
                font=pygame.font.Font("方正像素12.TTF",20)
                distext=font.render(text,1,(0,0,0))
                screen.blit(distext,(x+35,y-90))
                if Temp:
                    _thread.start_new_thread(dtext,("11区的卡车司机终于也来这里开JO护车了吗……",0.1))
                    Temp=False
            if _l == 1:
                screen.blit(sp_1,(x,y))
                screen.blit(p_1,(x-118,y-106))
                screen.blit(p_2,(x+250,y-40))
                font=pygame.font.Font("方正像素12.TTF",20)
                distext=font.render(text,1,(0,0,0))
                screen.blit(distext,(x+35-118,y-90))
                if Temp:
                    text=""
                    sleep(0.5)
                    stop=False
                    _thread.start_new_thread(dtext,("ここわだこ？",0.1))
                    Temp=False
            if _l == 2:
                if Temp:
                    sp_1=pygame.transform.scale(sp_1,(int(sp_1.get_rect()[2]*3/1.5),int(sp_1.get_rect()[3]*3/1.5)))
                screen.blit(sp_1,(x+250,y-200))
                screen.blit(p_1,(x-118,y-106))
                screen.blit(p_2,(x+250,y-40))
                screen.blit(sp_3,(x+250,y-40))
                font=pygame.font.Font("方正像素12.TTF",20)
                distext=font.render(text,1,(0,0,0))
                screen.blit(distext,(x+35-118,y-90))
                if Temp:
                    text=""
                    _thread.start_new_thread(sleep,(1,))
                    stop=False
                    _thread.start_new_thread(dtext,("等等!那是什么!",0.1))
                    Temp=False
            if _l == 3:
                if Temp:
                    sp_1=pygame.transform.scale(sp_1,(int(sp_1.get_rect()[2]*3/1.5),int(sp_1.get_rect()[3]*3/1.5)))
                screen.fill(color)
                screen.blit(sp_1,(x-250,y+200))
                screen.blit(p_1,(x-118,y-106))
                screen.blit(p_2,(x+250,y-40))
                screen.blit(sp_3,(x+250,y-40))
                font=pygame.font.Font("方正像素12.TTF",20)
                distext=font.render(text,1,(0,0,0))
                screen.blit(distext,(x+35-118,y-90))
                if answer['que']:
                    if answer['answer']==1000.0:
                        _l+=1
                        down_bool=True
                    else:
                        _l+=3
                if Temp:
                    text=""
                    _thread.start_new_thread(sleep,(1,))
                    _thread.start_new_thread(question,(0,))
                    stop=False
                    _thread.start_new_thread(dtext,("开发者:我美术不好,所以请见谅",0.1))
                    down_bool=False
                    Temp=False
            if _l == 4:
                if Temp:
                    sp_1=pygame.transform.scale(sp_1,(int(sp_1.get_rect()[2]*3/1.5),int(sp_1.get_rect()[3]*3/1.5)))
                screen.fill(color)
                screen.blit(sp_1,(x+250,y-200))
                screen.blit(p_1,(x-118,y-106))
                screen.blit(p_2,(x+250,y-40))
                screen.blit(sp_3,(x+250,y-40))
                font=pygame.font.Font("方正像素12.TTF",20)
                distext=font.render(text,1,(0,0,0))
                screen.blit(distext,(x+35-118,y-90))
                if Temp:
                    down_bool=True
                    text=""
                    _thread.start_new_thread(sleep,(1,))
                    stop=False
                    _thread.start_new_thread(dtext,("开发者:新手关结束了",0.1))
                    Temp=False
            if _l == 5:
                break
            if _l == 6:
                text=""
                _thread.start_new_thread(dtext,("蔡",0.1))
                font=pygame.font.Font("方正像素12.TTF",70)
                distext=font.render(text,1,(255,0,0))
                screen.blit(distext,(335,185))
    pygame.display.flip()
pygame.quit()
os.system('python _1.py')