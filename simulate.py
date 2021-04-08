import numpy as np
import matplotlib.pyplot as plt
import random
import copy

import matplotlib as mpl

class Modal:
    def __init__ (self):
        self.mapsize = (50,50)
        self.map = np.zeros(self.mapsize,int)
        self.map_temp = copy.deepcopy(self.map)
        self.time=0.001

        self.people_direct = copy.deepcopy(self.map)

        self.direction = [(0,1),(1,0),(0,-1),(-1,0)]
        self.search = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]   #8个方向遍历
        

        self.turn = 1#回合数目

        self.people_rate = 0.15    #产生人的概率
        self.people_move_rate = 1.0#人们流动比例

        self.cure_rate = 0.1#治愈概率

        self.ismask = 0  #是否带口罩
        self.isseparate = 1   #隔离
        self.create_sick_rate = 0.01#新增病人

        self.people_getsick_unmask = 0.4#未戴口罩患病概率
        self.people_getsick_mask = 0.1  #戴口罩患病的概率
        self.people_getsick_cure = 0.02 #感染后恢复的患病概率

        self.rec = 1
        self.rec_sick = 1
        self.rec_infect_cnt = 0

    def possibility(self,p):
        k = random.random()
        return k < p

    def rand_make(self):
        start=(random.randint(0,self.mapsize[0]-1),random.randint(0,self.mapsize[1]-1))   #随机产生X Y
        for x in range(self.mapsize[0]):
            for y in range(self.mapsize[1]):
                if x==start[0] and y==start[1]:         #初始化赋值
                    self.map_temp[x][y] = 2             #感染
                    self.people_direct[x][y] = random.randint(0,3) #即将移动的方向
                    continue
                if self.possibility(self.people_rate):  #判断是否产生人
                    self.map_temp[x][y] = 1
                    self.people_direct[x][y] = random.randint(0,3)
                    self.rec += 1
                else:
                    self.people_direct[x] = -1       #没有人
        return

    def infect(self,x,y):
        if self.ismask == 1:
            people_getsick = self.people_getsick_mask
        else:
            people_getsick = self.people_getsick_unmask

        for id in self.search:  #对周围8个方向进行遍历
            new_x = x+id[0]
            new_y = y+id[1]
            if new_x<0 or new_x>=self.mapsize[0] or new_y<0 or new_y>=self.mapsize[1]: #边界判断
                continue
            if self.map_temp[new_x][new_y] == 1 and self.possibility(people_getsick):  #如果是普通人且患病概率
               
                self.map_temp[new_x][new_y] = 2  #感染
                self.rec_sick += 1
                self.rec_infect_cnt += 1
            if self.map_temp[new_x][new_y] == 3 and self.possibility(self.people_getsick_cure): #恢复后的患病
                self.map_temp[new_x][new_y] = 2  #感染
                self.rec_sick += 1
                self.rec_infect_cnt += 1
        
        return

    def cure(self,x,y):
        if self.possibility(self.cure_rate):#治愈
            self.map_temp[x][y] = 3   #变成恢复者
            self.rec_sick -= 1

    def move_people(self,x,y):#012 空地 平民 患者   #进行人员流动
        if not self.possibility(self.people_move_rate):
            return
        dir = self.people_direct[x][y]  #上下左右四个方向      
        dir += random.randint(0, 3)
        dir %= 4

        new_x = x + self.direction[dir][0]
        new_y = y + self.direction[dir][1]
        if new_x<0 or new_x>=self.mapsize[0] or new_y<0 or new_y>=self.mapsize[1]:
            return
        if self.map_temp[new_x][new_y] != 0:  #被选中的必须是空地
            return

        if self.isseparate == 1:            #开启社交距离限制
            for id in self.direction:
                new_x2 = new_x+id[0]
                new_y2 = new_y+id[1]
                if new_x2<0 or new_x2>=self.mapsize[0] or new_y2<0 or new_y2>=self.mapsize[1]: #边界判断
                    continue
                if not self.map_temp[new_x2][new_y2] == 0:  #若新去的地方四周有人的话就不去
                    return

        self.people_direct[x][y],self.people_direct[new_x][new_y] = self.people_direct[new_x][new_y],self.people_direct[x][y]

        self.map_temp[x][y],self.map_temp[new_x][new_y] = self.map_temp[new_x][new_y],self.map_temp[x][y]
        return

    def show(self):

        colors = ['white', 'black', 'red', 'green'] 
        cmap = mpl.colors.ListedColormap(colors)

        self.map = copy.deepcopy(self.map_temp)  #将副本复制过来
        plt.imshow(self.map,cmap= cmap)
        plt.pause(self.time)
        
        # print("人数：",rec)
        # print("患病人数：",self.rec_sick)

        print(self.turn,"\t",self.rec,"\t",self.rec_sick)
        self.turn+=1
        #if not self.rec_infect_cnt == 0:
         #   print("预估R0：",self.rec_sick/self.rec_infect_cnt)
        return

    def create_sick(self,x,y):
        if self.possibility(self.create_sick_rate):
            self.map_temp[x][y] = 2
            self.rec_sick += 1

    def go(self):
        self.rand_make()

        while(self.turn < 50):
            matrix = [0,0,0,0]
            #self.cure_rate += self.cure_rate_increase
            self.show()
            for i in range (self.mapsize[0]):
                for j in range (self.mapsize[1]):
                    if not self.map[i][j] == 0:
                        self.move_people(i,j)   #人群流动
                        matrix[self.map[i][j]] += 1

            print(matrix[0],"\t",matrix[1],"\t",matrix[2],"\t",matrix[3])

            for i in range(self.mapsize[0]):
                for j in range (self.mapsize[1]):
                    if self.map_temp[i][j] == 2:
                        self.infect(i,j)
                        self.cure(i,j)
                    elif self.map_temp[i][j] == 1:
                        self.create_sick(i,j)

if __name__ == '__main__':
    modal = Modal()
    modal.go()
