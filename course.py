from bs4 import BeautifulSoup

def get_class_time(fileName) -> list: 
    with open(fileName, "r", encoding="utf-8") as f:
        html = f.read()
        soup = BeautifulSoup(html,'html.parser')
        table = soup.find("table", {"id": "manualArrangeCourseTable"})
        rows = table.find_all("tr")
        table_data = []
        for row in rows:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            if cols:
                table_data.append(cols)
    return table_data
def get_map_of_week(l) -> dict:
    # 填补空缺
    for i in range(len(l)):
        for j in range(len(l[0])):
            if i > 0 and l[i - 1][j] != '' and j > 0:
                l[i].insert(j, '')
    # dic = {0 : [], 1 : []}
    dict = {i : [] for i in range(len(l[0]) - 1)} # len(l[0]) - 1 去掉第一列
    for i in range(len(l)):
        for j in range(1, len(l[0])):
                dict[j - 1].append(l[i][j])
    return dict

def get_final_week(fileName) -> dict:
    map = get_map_of_week(get_class_time(fileName))
    get_important_info(map)
    return map


# '''
# 获取第count个正括号的位置
# '''
# def get_index_of_third_bracket(s, count):
#     for i in range(len(s)):
#         if s[i] == '(':
#             count -= 1
#         if count == 0:
#             return i
#     return -1
# '''
# 获取第count个反括号位置
# '''
# def get_index_of_third_back_bracket(s, count):
#     for i in range(len(s)):
#         if s[i] == ')':
#             count -= 1
#         if count == 0:
#             return i
#     return -1

# '''
# 获取课程 括号 列表 [(num), (name), (time, room_location room_num), ....]
# '''
# def get_list_of_course(s):
#     res = []
#     while '(' in s:
#         start = s.find('(')
#         end = s.find(')')
#         res.append(s[start + 1: end])
#         s = s[end + 1:]
#     return res
'''
index 为教室名字的位置
返回 教室名字外层括号的位置
'''
def get_index_of_start_and_end(s, index) -> tuple:
    left = right = index 
    while (s[left] != '(' or s[right] != ')'):
        if (s[left] != '('):
            left -= 1
        if (s[right] != ')'):
            right += 1
    return (left, right)
'''
获取map中重要信息 第三个括号内的内容
mute , 直接修改 map
'''
def get_important_info(map) -> None:
    for i in map:
        next_list = []
        index_of_class = -1
        for j in map[i]: # single string of list
            index_of_class += 1
            if (len(j) == 0):
                continue
            index_of_room_name = j.find("明理") if j.find("天工") == -1 else j.find("天工")
            while (index_of_room_name != -1):
                start, end = get_index_of_start_and_end(j, index_of_room_name)
                next_list.append(j[start + 1: end] + "," + str(index_of_class + 1))
                j = j[end + 1:]
                index_of_room_name = j.find("明理") if j.find("天工") == -1 else j.find("天工")
        map[i] = next_list

map = get_final_week("./课表/course.html")
# for i in map:
#     print(i, map[i])
# get_important_info(map)
