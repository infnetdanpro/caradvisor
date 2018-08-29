import requests
from lxml import etree
from datetime import datetime, timedelta

predict_stat = {
        0: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
        1: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
        2: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
        3: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
        4: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
        5: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:2, 9:3, 10:3, 11:4, 12:5, 13:6, 14:5, 15:6, 16:7, 17:6, 18:7, 19:6, 20:5, 21:4, 22:2, 23:0},
        6: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:2, 9:3, 10:3, 11:4, 12:5, 13:6, 14:5, 15:6, 16:7, 17:6, 18:7, 19:6, 20:5, 21:4, 22:2, 23:0}
        }

TRAFFIC_URL = 'https://export.yandex.ru/bar/reginfo.xml?region=213'


def get_traffic_url():
    try:
        result = requests.get(TRAFFIC_URL)
    except requests.exceptions.RequestException as e:
        print('Exception happend: ', e)

    if result.status_code == 200:
        return result
    else:
        print('Something is wrong with server response')


def predict_function(predict_list, predict_start, predict_end, predict_step):
    predict_traff_stats = predict_list
    curr_weekday = datetime.now().weekday()
    curr_weekday = int(curr_weekday)
    curr_hours = datetime.now().hour

    hour_list = []
    for hours in range(predict_start, predict_end, predict_step):
        append_hour = datetime.now() + timedelta(hours=hours)
        hour_list.append(append_hour.hour)

    predict_list = []
    for predict in hour_list:
        predict_list.append(predict_traff_stats[curr_weekday][predict])
    return 'Предстоящие пробки на ближайшие 6 часов: ' + str(predict_list)


def get_jams():
    result = get_traffic_url()
    tree = etree.fromstring(result.content)
    xpath_tree = tree.xpath('/info/traffic/region/hint/text()')
    return xpath_tree[0]


def get_jam_level():
    result = get_traffic_url()
    tree = etree.fromstring(result.content)
    xpath_tree = tree.xpath('/info/traffic/region/level/text()')
    return xpath_tree[0]


def get_jams_icon_color():
    result = get_traffic_url()
    tree = etree.fromstring(result.content)
    xpath_tree = tree.xpath('/info/traffic/region/icon/text()')
    return xpath_tree[0]


def day_type():
    today = datetime.now().weekday()
    """weekdays = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}"""
    if today < 5:
        return 'Сегодня будний день. Пробки обычно с 7 до 11 и 17 до 21'
    else:
        return 'Сегодня выходной день. Пробки обычно с 11 до 13 и с 17 до 20'

#if __name__ == "__main__":
    # jams_now = get_jams() + ': ' + get_jam_level() + ' (' + get_jams_icon_color() + ') '
    # day_type = day_type()

    # predict_start, predict_end, predict_step = 3, 12, 3
    # predict_stat = {
    #     0: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
    #     1: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
    #     2: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
    #     3: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
    #     4: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:2, 8:5, 9:7, 10:8, 11:7, 12:5, 13:4, 14:4, 15:5, 16:5, 17:6, 18:7, 19:7, 20:5, 21:4, 22:2, 23:0},
    #     5: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:2, 9:3, 10:3, 11:4, 12:5, 13:6, 14:5, 15:6, 16:7, 17:6, 18:7, 19:6, 20:5, 21:4, 22:2, 23:0},
    #     6: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:2, 9:3, 10:3, 11:4, 12:5, 13:6, 14:5, 15:6, 16:7, 17:6, 18:7, 19:6, 20:5, 21:4, 22:2, 23:0}
    #     }
    # view_predict = predict_function(predict_stat, predict_start, predict_end, predict_step)
    # traffic_predict = 'Предстоящие пробки: ' + str(view_predict)

    # print(day_type)
    # print(jams_now)
    # print(traffic_predict)
