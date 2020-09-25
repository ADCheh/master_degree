from gui import *
from classes import *
import math as m
from PyQt5 import QtCore, QtWidgets
import sys
import copy
import random as rnd
import pickle
from socket import *
from array import *

host = "localhost"
host1 = "192.168.88.23"
host2 = "192.168.88.25"
port = 50000
port1 = 50001
port2 = 50002
buf = 4096
addr = (host, port)
addr1 = (host1, port1)
addr2 = (host2, port2)

agents_count = 0
steps = 0
mutation = 0
population = 0
speed = 0
start_points = []
finish_points = []
agents = []
pathes = []
default_pathes = []
obstacles = []
stop_check = []
main_time = 0
done = False


def init():
    global agents_count
    global steps
    global mutation
    global population
    global speed
    global robots
    global start_points
    global stop_check

    agents_count = ui.agents_spinBox.value()
    steps = ui.steps_spinBox.value()
    mutation = ui.mutation_doubleSpinBox.value()
    population = ui.population_spinBox.value()
    speed = ui.speed_doubleSpinBox.value()

    if ui.obstacle_checkBox.isChecked() == True:
        obstacles.append(Obstacle(220, 220, 90, 90))
        print(obstacles[0].points)

    """Инициализация стартовых точек"""
    for i in range(agents_count):
        x = 50
        y = (450 / agents_count) / 2 + i * (450 / agents_count)
        start_points.append([x, y])
    """инициализация финишных точек точек"""
    for i in range(agents_count):
        x = 400
        y = (450 / agents_count) / 2 + i * (450 / agents_count)
        finish_points.append([x, y])

    """Установка финишных точек в нужные позиции для каждого агента"""
    if ui.random_checkBox.isChecked() == True:
        rnd.shuffle(finish_points)
    else:
        if agents_count == 2:
            finish_points.reverse()
        elif 2 < agents_count < 5:
            temp_point = finish_points.pop(2)
            finish_points.insert(0, temp_point)
        elif agents_count == 5:
            temp_point = finish_points.pop(2)
            finish_points.insert(0, temp_point)
            temp_point = finish_points.pop(4)
            finish_points.insert(3, temp_point)
        elif agents_count <= 7:
            temp_point = finish_points.pop(2)
            finish_points.insert(0, temp_point)
            temp_point = finish_points.pop(5)
            finish_points.insert(3, temp_point)
            temp_point = finish_points.pop(4)
            finish_points.insert(5, temp_point)
        elif agents_count < 9:
            temp_point = finish_points.pop(2)
            finish_points.insert(0, temp_point)
            temp_point = finish_points.pop(5)
            finish_points.insert(3, temp_point)
            temp_point = finish_points.pop(4)
            finish_points.insert(5, temp_point)
            temp_point = finish_points.pop(6)
            finish_points.insert(8, temp_point)
        elif agents_count < 11:
            temp_point = finish_points.pop(2)
            finish_points.insert(0, temp_point)
            temp_point = finish_points.pop(5)
            finish_points.insert(3, temp_point)
            temp_point = finish_points.pop(4)
            finish_points.insert(5, temp_point)
            temp_point = finish_points.pop(6)
            finish_points.insert(8, temp_point)
            temp_point = finish_points.pop(6)
            finish_points.insert(9, temp_point)

    """Инициализация агентов"""
    for i in range(0, agents_count):
        agents.append(Robot(i, start_points[i][0], start_points[i][1], speed, start_points[i], finish_points[i]))

    """Инициализация путей"""
    for i in range(len(start_points)):
        pathes.append(Path(i, start_points[i], finish_points[i], steps))
        default_pathes.append(Path(i, start_points[i], finish_points[i], steps))

    for i in range(len(agents)):
        agents[i].get_path(pathes[i])

    for i in range(len(pathes)):
        stop_check.append(False)
    stop_check[0] = True

def draw():
    global obstacles
    ui.scene.clear()

    if ui.obstacle_checkBox.isChecked() == True:
        obst_rect = QRectF(obstacles[0].x-(obstacles[0].w/2)+5,obstacles[0].y-(obstacles[0].h/2-15),obstacles[0].w-25,obstacles[0].h-25)
        ui.scene.addRect(obst_rect, ui.pens[9], ui.brushes[9])
    """Отрисовка путей и вершин ребер в пути"""
    for i in range(len(pathes)):
        for j in range(1, len(pathes[i].points)):
            ui.scene.addLine(pathes[i].points[j - 1][0], pathes[i].points[j - 1][1], pathes[i].points[j][0],
                             pathes[i].points[j][1], ui.pens[i])
            ui.scene.addEllipse(pathes[i].points[j][0] - 2, pathes[i].points[j][1] - 2, 4, 4, ui.pens[9], ui.brushes[9])

    """Отрисовка стартовых точек"""
    for i in range(len(start_points)):
        ui.scene.addEllipse(start_points[i][0] - 5, start_points[i][1] - 5, 10, 10, ui.pens[9], ui.brushes[i])

    """Отрисовка финишных точек"""
    for i in range(len(finish_points)):
        ui.scene.addEllipse(finish_points[i][0] - 5, finish_points[i][1] - 5, 10, 10, ui.pens[9], ui.brushes[i])
    """Отрисовка агентов"""
    for i in range(len(agents)):
        if len(agents)==10:
            rect = QRectF(agents[i].x - 18, agents[i].y - 10, 36, 20)
            pol = QtGui.QPolygonF(rect)
            p = ui.scene.addPolygon(pol, ui.pens[9], ui.brushes[i])
            transform = QtGui.QTransform()
            transform.translate(agents[i].x, agents[i].y)
            transform.rotate(agents[i].angle)
            transform.translate(-agents[i].x, -agents[i].y)
            p.setTransform(transform)
        elif len(agents)==6:
            rect = QRectF(agents[i].x - 21, agents[i].y - 14, 42, 28)
            pol = QtGui.QPolygonF(rect)
            p = ui.scene.addPolygon(pol, ui.pens[9], ui.brushes[i])
            transform = QtGui.QTransform()
            transform.translate(agents[i].x, agents[i].y)
            transform.rotate(agents[i].angle)
            transform.translate(-agents[i].x, -agents[i].y)
            p.setTransform(transform)
        elif len(agents)==5:
            rect = QRectF(agents[i].x - 24, agents[i].y - 16, 48, 32)
            pol = QtGui.QPolygonF(rect)
            p = ui.scene.addPolygon(pol, ui.pens[9], ui.brushes[i])
            transform = QtGui.QTransform()
            transform.translate(agents[i].x, agents[i].y)
            transform.rotate(agents[i].angle)
            transform.translate(-agents[i].x, -agents[i].y)
            p.setTransform(transform)
        else:
            rect = QRectF(agents[i].x - 29, agents[i].y - 19, 58, 38)
            pol = QtGui.QPolygonF(rect)
            p = ui.scene.addPolygon(pol, ui.pens[9], ui.brushes[i])
            transform = QtGui.QTransform()
            transform.translate(agents[i].x, agents[i].y)
            transform.rotate(agents[i].angle)
            transform.translate(-agents[i].x, -agents[i].y)
            p.setTransform(transform)

def line_cross(t1, t2, i, j):
    x = 0
    y = 0

    zn = ((t2[j][1] - t2[j - 1][1]) * (t1[i][0] - t1[i - 1][0]) - (t2[j][0] - t2[j - 1][0]) * (
            t1[i][1] - t1[i - 1][1]))
    ch1 = (t2[j][0] - t2[j - 1][0]) * (t1[i - 1][1] - t2[j - 1][1]) - (t2[j][1] - t2[j - 1][1]) * (
            t1[i - 1][0] - t2[j - 1][0])
    ch2 = (t1[i][0] - t1[i - 1][0]) * (t1[i - 1][1] - t2[j - 1][1]) - (t1[i][1] - t1[i - 1][1]) * (
            t1[i - 1][0] - t2[j - 1][0])

    if zn == 0:
        return [False, x, y]
    else:

        u1 = ch1 / zn
        u2 = ch2 / zn

        if (0 <= u1 <= 1) and (0 <= u2 <= 1):
            x = t1[i - 1][0] + u1 * (t1[i][0] - t1[i - 1][0])
            y = t1[i - 1][1] + u1 * (t1[i][1] - t1[i - 1][1])
            return [True, x, y]
        else:
            return [False, x, y]

def find_cross(path1,path2):
    """Поиск координат пересечения и проверка по времени"""
    global speed
    global agents

    time_check = 950
    if len(agents) == 10:
        time_check = 600
    dist1 = 0
    dist2 = 0

    for i in range(1, len(path1.points)):
        for j in range(1, len(path2.points)):

            check = line_cross(path1.points, path2.points, i, j)
            if check[0]:

                dist1 += m.pow(
                    m.pow(check[1] - path1.points[i - 1][0], 2) + m.pow(check[2] - path1.points[i - 1][1], 2), 0.5)
                dist2 += m.pow(
                    m.pow(check[1] - path2.points[j - 1][0], 2) + m.pow(check[2] - path2.points[j - 1][1], 2), 0.5)
                t1 = dist1 / speed
                t2 = dist2 / speed

                if abs(t1 - t2) < time_check:
                    return [True, j, i, t2]
                else:
                    return [False, j, i, t2]
            else:
                dist2 += m.pow(m.pow(path2.points[j][0] - path2.points[j - 1][0], 2) + m.pow(
                    path2.points[j][1] - path2.points[j - 1][1], 2), 0.5)
        dist1 += m.pow(m.pow(path1.points[i][0] - path1.points[i - 1][0], 2) + m.pow(
            path1.points[i][1] - path1.points[i - 1][1], 2), 0.5)
        dist2 = 0

    return [False, 135, 135, 1]

def get_score(path, t):
    global default_pathes
    global finish_points
    global pathes
    global obstacles

    score = 0
    def_mult = 5  # 0.1
    fin_mult = 0.01 # 0.01
    kobst = 1

    if ui.obstacle_checkBox.isChecked():
        if check_obstacle(path):
            kobst = 2

    for i in range(1, len(path.points) - 1):

        if ui.obstacle_checkBox.isChecked():
            oc = m.pow(m.pow(path.points[i][0] - obstacles[0].x, 2) + m.pow(path.points[i][1] - obstacles[0].y, 2),
                       0.5)

        deflection = m.pow(m.pow(path.points[i][0] - default_pathes[path.id].points[i][0], 2) + m.pow(
            path.points[i][1] - default_pathes[path.id].points[i][1], 2), 0.5) * def_mult
        to_finish = m.pow(m.pow(path.points[i][0] - finish_points[path.id][0], 2) + m.pow(
            path.points[i][1] - finish_points[path.id][1], 2), 0.5) * fin_mult

        c = m.pow(m.pow(path.points[i][0] - path.points[i - 1][0], 2) + m.pow(
            path.points[i][1] - path.points[i - 1][1], 2), 0.5)

        bet = m.pow(m.pow(path.points[i][0] - pathes[path.id - 1].points[i][0], 2) + m.pow(
            path.points[i][1] - pathes[path.id - 1].points[i][1], 2), 0.5)

        A1 = [path.points[i - 1][0] - path.points[i][0], path.points[i - 1][1] - path.points[i][1]]
        A2 = [path.points[i + 1][0] - path.points[i][0], path.points[i + 1][1] - path.points[i][1]]
        ch = A1[0] * A2[0] + A1[1] * A2[1]
        zn = m.pow(m.pow(A1[0], 2) + m.pow(A1[1], 2), 0.5) * m.pow(m.pow(A2[0], 2) + m.pow(A2[1], 2), 0.5)
        cos = ch / zn

        a = m.acos(cos) * 180 / m.pi

        if ui.obstacle_checkBox.isChecked():
            if check_obstacle(path)[0]:
                score += ((1 / (deflection + to_finish)) + (a / 120) + bet / 40 + oc / 100)
            else:
                score += ((1 / (deflection + to_finish)) + (a / 120) + bet / 40 + oc / 10)
        else:
            score += ((1 / (deflection + to_finish)) + (a / 120) + bet / 40)
            if ui.obstacle_checkBox.isChecked():
                if check_obstacle(path)[0]:
                    score += ((1 / (deflection + to_finish)) + (a / 120) + bet / 40 + oc / 100)
                else:
                    score += ((1 / (deflection + to_finish)) + (a / 120) + bet / 40 + oc / 10)
            else:
                score += ((1 / (deflection + to_finish)) + (a / 120) + bet / 40)

    return score


def check_obstacle(path):
    global obstacles

    for i in range(1, len(path.points)):
        for j in range(1, len(obstacles[0].points)):

            cross = line_cross(path.points, obstacles[0].points, i, j)
            if cross[0]:
                return [True, i]

    return [False,135]


def gen(path,point_id, t):
    global population
    global mutation
    global steps

    population_stack = []
    population_score = []
    best_score = get_score(path,300)
    best_id = 0

    r=5
    if path.id == 0 :
        r=7
    min = point_id - r
    max = point_id + r

    if point_id+r>=len(path.points):
        max = len(path.points)-1
    if point_id-r<=1:
        min = 1

    if path.id!=0:
        min=1

    for i in range(population):
        temp = copy.deepcopy(path)
        try:
            for j in range(min, max):
                kx = rnd.uniform(-mutation, mutation)
                ky = rnd.uniform(-mutation, mutation)
                try:
                    temp.points[j][0] += kx
                    temp.points[j][1] += ky
                except:
                    print("plus")
        except:
            print("mmmuuuttt")
        population_stack.append(temp)
        population_score.append(get_score(temp, t))
        if population_score[i] > best_score:
            best_score = population_score[i]
            best_id = i

    s = "Траектория №" + str(population_stack[best_id].id + 1) + ", f = " + str(best_score) + "\n"
    ui.add_text(s)
    return population_stack[best_id]

def end():
    global pathes
    global done

    for i in range(len(pathes)):
        for j in range(i+1,len(pathes)):
            check = find_cross(pathes[i], pathes[j])
            if check[0]:
                return

    for i in range(len(pathes)):
        if check_obstacle(pathes[i])[0]:
            return

    done = True


def evo():
    global mutation
    global population
    global pathes
    global done
    global agents
    global stop_check

    for i in range(len(pathes)):

        if ui.obstacle_checkBox.isChecked():
            obst = check_obstacle(pathes[i])
            if obst[0]:
                new_i = gen(pathes[i], obst[1], 300)
                pathes[i] = new_i
                agents[i].get_path(pathes[i])

            else:
                for j in range(i + 1, len(pathes)):
                    check = find_cross(pathes[i], pathes[j])  # True только если пересечение ведет к столкновению
                    if check[0]:
                        print(str(check[2]) + " из " + str(i) + "_И_" + str(check[1]) + " из " + str(j))
                        new_j = gen(pathes[j], check[1], check[3])
                        pathes[j] = new_j
                        agents[j].get_path(pathes[j])
                        print(find_cross(pathes[i], pathes[j])[0])
                    else:
                        stop_check[j] = True

        else:
            for j in range(i + 1, len(pathes)):
                check = find_cross(pathes[i], pathes[j])  # True только если пересечение ведет к столкновению
                if check[0]:
                    print(str(check[2]) + " из " + str(i) + "_И_" + str(check[1]) + " из " + str(j))
                    new_j = gen(pathes[j], check[1], check[3])
                    pathes[j] = new_j
                    agents[j].get_path(pathes[j])
                    print(find_cross(pathes[i], pathes[j])[0])
                else:
                    stop_check[j] = True

def check_data(Statement,x,y):
    Statement = not Statement
    x+=rnd.uniform(-10,10)
    y+=rnd.uniform(-10,10)

    return [Statement,x,y]

def start():

    init()
    draw()
    ui.clock.start(100)
    ui.timer.start(1)

def waiting(ind):
    global agents
    agents[ind].speed = 0


def cycle():
    global agents
    global speed
    draw()

    if not done:
        evo()
        end()
    else:
        ui.clock.stop()
        for i in range(len(agents)):
            agents[i].move()
            print("угол у " + str(i) + "равен " + str(agents[i].angle))


def clock():
    global main_time
    main_time +=100
    ui.show_time(str(main_time/1000) + "секунд")


def stop():
    print("stop")
    ui.timer.stop()

def send_tr():
    UDPSock = socket(AF_INET, SOCK_DGRAM)

    def_msg = "===Enter message to send to server===";
    print("\n", def_msg)
    a = [path_green, path_red, path_blue, v]
    while (1):
        if (UDPSock.sendto(pickle.dumps(a, protocol=2), addr)):
            print("Sending message")
        if (UDPSock.sendto(pickle.dumps(a, protocol=2), addr1)):
            print("Sending message")
        if (UDPSock.sendto(pickle.dumps(a, protocol=2), addr2)):
            print("Sending message")
    UDPSock.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.startButton.clicked.connect(start)
    ui.stopButton.clicked.connect(stop)
    ui.timer.timeout.connect(cycle)
    ui.clock.timeout.connect(clock)

    MainWindow.show()
    sys.exit(app.exec_())