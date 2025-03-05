from bs4 import BeautifulSoup, Comment
import re

class Empty_Room:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def __str__(self):
        return self.name + str(self.num)

'''
获取教室的使用情况
'''
def getRoomUsage(fileName) -> list: 
    with open(fileName, "r", encoding="utf-8") as f:
        html = f.read()
        soup = BeautifulSoup(html,'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    # 执行匹配
    # 打印注释内容
    l = []
    for comment in comments:
        s = str(comment)
        s = s[s.find(":") + 1:][1: len("1,1,1,1,1,1,0,0,0,0,0,0") + 3][1:-1]
        if s.startswith("0") or s.startswith("1"):
            l.append(s)
    l = l[2:]
    return l

'''
获取教室映射, key为Room对象, value为一个长度为12的数组, 0表示空闲, 1表示占用
'''
def getMap(l) -> dict:
    dic = {}
    index = 0
    layer = 100
    i = 0
    # for (int i = 0; i < l.length(); i++)
    while (i < len(l)):
        index += 1
        if index == 11 or index == 13 or index == 15:
            continue
        r = Empty_Room("天工南", layer + index)
        dic[r] = [int(i) for i in l[i].split(",")]
        if ((index == 12 and layer == 100) or index == 16):
            layer += 100 
            index = 0
        i += 1
    return dic
'''
获取某个时间段的空闲教室
dic 表示教室中的使用情况
class_time 表示第几节课
返回 list of Room
'''
def getEmpty(dic, class_time) -> list:
    res = []
    for key in dic.keys():
        if dic[key][class_time - 1] == 0 and dic[key][class_time] == 0:
            res.append(key)
    return res

'''
评分函数, 评分规则如下:
1. 如果教室和课程所在楼层相差3层以上, 不考虑
2. 如果教室和课程所在楼层相差1层, 评分加5
3. 如果教室和课程所在楼层相差2层, 评分加7
4. 评分基础为教室和课程的编号差
5. 评分越小, 优先级越高
l 为 空闲教室list
class_room 为 课程所在教室
返回一个list, 元素为(教室, 评分)
'''
def score(l, class_room) -> list:
    res = []
    for i in l:
        room_num = int(i.num)
        class_num = int(class_room.num)
        if (abs(room_num // 100 - class_num // 100) >= 3):
            continue 
        base = abs(class_num % 100 - room_num % 100)
        if (abs(room_num // 100 - class_num // 100)) == 1:
            additional = 5
        elif (abs(room_num // 100 - class_num // 100)) == 2:
            additional = 7 
        else:
            additional = 0
        res.append((i, base + additional))
    res.sort(key=lambda x: x[1])
    return res

# for i in getEmpty(getMap(getRoomUsage()), 7):
#     print(i)

def get_final_room(fileName, room):
    return score(getEmpty(getMap(getRoomUsage(fileName)), room.first_time), room)