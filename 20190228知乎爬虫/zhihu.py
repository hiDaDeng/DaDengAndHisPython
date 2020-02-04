import requests
from settings import BASE_URL, HEADERS, COOKIES, answers_clean_json
import jsonlines


class Zhihu(object):
    def __init__(self, quesionid):
        self.quesionid = quesionid
        self.url = BASE_URL.format(question_id=quesionid)


    def answers(self):
        req = requests.get(self.url, headers=HEADERS, cookies=COOKIES)
        jsondata = req.json()
        try:
            self.url = jsondata['paging']['next']
            self.save(jsondata['data'])
            return self.answers()
        except:
            print('程序运行终止')
            return

    def save(self, jsondata):
        with jsonlines.open('data/{0}.json'.format(self.quesionid), mode='a') as writer:
            for jsonl in jsondata:
                rowjson = answers_clean_json(jsonl)
                print(rowjson)
                writer.write(rowjson)


Zhihu(quesionid=27182640).answers()
