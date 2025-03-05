import empty_room as er
import os
import course as c
import datetime
import time


def day_diff(day1, day2):
    time_array1 = time.strptime(day1, "%Y-%m-%d")
    timestamp_day1 = int(time.mktime(time_array1))
    time_array2 = time.strptime(day2, "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result


if __name__ == "__main__":
    # 获取当前日期和时间
    now = datetime.now()
    # 获取星期几，其中星期一到星期日对应的整数分别为0到6
    week = now.weekday()
    c.get_final_week("./课表/course.course.html")
    # 当天上课的课程
    l = c[week]
    # 获取当前是 第 几 周
    day1 = "2025-02-17"
    day2 = datetime.now().strftime("%Y-%m-%d") 
    diff_of_day = day_diff(day1, day2)
    week = diff_of_day // 7
    print(week)
    
    # 转room对象

