from os import *
from io import *
import requests
import json

MY_GITHUB_URL = "https://github.com/isayaksh/Algorithm/blob/main/BaekJoon/"
BOJ_URL = "https://www.acmicpc.net/problem/"
LEVEL_DIC = {0: 'Unrated', 1: 'Bronze V', 2: 'Bronze IV', 3: 'Bronze III', 4: 'Bronze II', 5: 'Bronze I', 
             6: 'Silver V', 7: 'Silver IV', 8: 'Silver III', 9: 'Silver II', 10: 'Silver I', 
             11: 'Gold V', 12: 'Gold IV', 13: 'Gold III', 14: 'Gold II', 15: 'Gold I', 
             16: 'Platinum V', 17: 'Platinum IV', 18: 'Platinum III', 19: 'Platinum II', 20: 'Platinum I', 
             21: 'Diamond V', 22: 'Diamond IV', 23: 'Diamond III', 24: 'Diamond II', 25: 'Diamond I', 
             26: 'Ruby V', 27: 'Ruby IV', 28: 'Ruby III', 29: 'Ruby II', 30: 'Ruby I'}

README_HEADER = "# 알고리즘 공부\n> 알고리즘 학습을 위한 Repository\n## 🧷 [Baekjoon Online Judge](https://www.acmicpc.net/)\n|번호|tag|태그|레벨|문제|코드|\n|:-:|:-:|:-:|:-:|:-:|:-:|\n"

def createRow(problemId, tagEn, tagKo, level, title):
    return f"|{problemId}|{tagEn}|{tagKo}|{LEVEL_DIC[level]}|[{title}]({BOJ_URL+problemId})|[{problemId}.py]({MY_GITHUB_URL+problemId}.py)|\n"

def get_problem_info(problemId):
    url = 'https://solved.ac/api/v3/problem/show'
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    param = {'problemId': problemId}
    try:
        response = requests.get(url, headers=headers, params=param)
        json_object = json.loads(response.text)
        title = json_object['titleKo']
        level = json_object['level']
        for obj in json_object["tags"]:
            for ob in obj['displayNames']:
                if ob['language'] == 'ko':
                    tagKo = ob['name']
                else:
                    tagEn = ob['name']
        print(problemId, tagEn, tagKo, level, title)
        return createRow(problemId, tagEn, tagKo, level, title)
    except Exception as ex:
        print(f"[updateReadme.get_problem_info][ERROR] : [{problemId}] {ex.with_traceback}")


def updateAll():
    #remote
    file_list = listdir("/home/runner/work/Algorithm/Algorithm/BaekJoon");

    # local
    # file_list = listdir("/Users/ksh/Documents/GitHub/Algorithm/BaekJoon")

    file_list = list(map(lambda x : x.replace('.py', ''), file_list))
    file_list.sort(key=lambda x : int(x))

    # remote
    f = open('/home/runner/work/Algorithm/Algorithm/README.md', 'w', encoding='utf8')

    # local
    # f = open('/Users/ksh/Documents/GitHub/Algorithm/README.md', 'w', encoding='utf8')

    f.write(README_HEADER)
    for problemId in file_list:
        data = get_problem_info(problemId)
        if data != None:
            f.write(data)
    f.close()

updateAll()