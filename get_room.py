import empty_room as er
import course as c
import datetime
import time

class Class_Room(er.Empty_Room):
    def __init__(self, name, num, first_time):
        super().__init__(name, num)
        self.first_time = first_time
    def __str__(self):
        return f"上课教室: {self.name}{self.num}, 开始上课时间{self.first_time // 2 + 1}节"

def day_diff(day1, day2):
    time_array1 = time.strptime(day1, "%Y-%m-%d")
    timestamp_day1 = int(time.mktime(time_array1))
    time_array2 = time.strptime(day2, "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result
   
class time_of_class:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __str__(self):
        return f"{self.start} - {self.end}"
    def __repr__(self):
        return f"{self.start} - {self.end}"

def main():
    # 获取当前日期和时间
    now = datetime.datetime.now()
    # 获取星期几，其中星期一到星期日对应的整数分别为0到6
    day = now.weekday()
    map =  c.get_final_week("./课表/course.html")
    # 当天上课的课程
    today_course = map[day]
    # 获取当前是 第 几 周
    day1 = "2025-02-17"
    day2 = datetime.datetime.now().strftime("%Y-%m-%d") 
    diff_of_day = day_diff(day1, day2)
    week = diff_of_day // 7 + 1
    # 找到当前周的课程
    week_course = []
    for i in today_course:
        if (week in range(int(i.split("-")[0]), int(i[i.find("-") + 1:i.find(",")]) + 1)):
            week_course.append(i)
    rooms = []
    for i in week_course:
        arr = i.split(",")[1:]
        index_of_first_num = -3
        room = Class_Room(arr[0][:index_of_first_num], int(arr[0][index_of_first_num:]), int(arr[1]))
        rooms.append(room)
    for i in rooms:
        print(i)
        print("空闲教室: ")
        for j in er.get_final_room(f"./空闲教室/空闲教室{day + 1}.htm", i):
            print('\t', j[0], "得分为 : ",j[1])
        print()

