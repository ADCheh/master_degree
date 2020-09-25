"""Описание классов"""
import math as m

class Edge():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2



class Path():
    def __init__(self,id,sp,fp,steps):
        self.points = []
        self.id = id
        self.gen = 1
        c = m.pow(m.pow(sp[0]-fp[0],2)+m.pow(sp[1]-fp[1],2),0.5)/steps
        phi = m.atan2(fp[1] - sp[1], fp[0] - sp[0])
        x1 = sp[0]
        y1 = sp[1]
        self.points.append([x1,y1])
        for i in range(1,steps):
            x2 = x1+m.cos(phi)*c
            y2 = y1+m.sin(phi)*c
            self.points.append([x2,y2])
            x1 = x2
            y1 = y2
        self.points.append([fp[0],fp[1]])



class Robot():
    def __init__(self, id, x, y, v, sp, fp):
        self.id = id
        self.x = x
        self.y = y
        self.speed = v
        self.start = sp
        self.finish = fp
        self.angle = 0
        self.path = None
        self.next_x = 0
        self.next_y = 0
        self.last_x = sp[0]
        self.last_y = sp[1]
        self.step = 1
        self.get = False


    def get_path(self,path):
        self.path = path
        self.next_x = self.path.points[self.step][0]
        self.next_y = self.path.points[self.step][1]

    def move(self):
        if not self.get:
            if m.fabs(self.x - self.next_x) <= 5 and m.fabs(self.y - self.next_y) <= 5:
                if self.step == len(self.path.points) - 1:
                    self.get = True
                    print("Агент №" + str(self.id) + " прибыл")
                    return
                self.step += 1
                self.last_x = self.next_x
                self.last_y = self.next_y
                self.next_x = self.path.points[self.step][0]
                self.next_y = self.path.points[self.step][1]
                print("Следующая точка № " + str(self.step))

            alpha = -m.atan2(self.next_y - self.last_y, self.next_x - self.last_x) * 180 / m.pi
            c = m.pow(m.pow(self.next_x-self.last_x,2)+m.pow(self.next_y-self.last_y,2),0.5)
            alpha = -alpha

            if m.fabs(self.angle-alpha) >= 3:
                if self.angle - alpha > 0:
                    self.angle -= 1
                else:
                    self.angle += 1
            else:
                self.x += self.speed * (self.next_x-self.last_x) / c
                self.y += self.speed * (self.next_y - self.last_y) / c


class Obstacle():
    def __init__(self,x,y,h,w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.p1 = [x-w/2,y-h/2]
        self.p2 = [x+w/2,y-h/2]
        self.p3 = [x+w/2,y+h/2]
        self.p4 = [x-w/2,y+h/2]
        self.points = []
        self.points.append(self.p1)
        self.points.append(self.p2)
        self.points.append(self.p3)
        self.points.append(self.p4)
        self.points.append(self.p1)



