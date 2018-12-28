import ast

import requests


def get_session():
    req = requests.session()
    data = {"username": "test", "pwd": "123456"}
    req.post("http://127.0.0.1:8080/api/login", data, verify=False)
    return req


def get_api():
    req = get_session()
    res = req.get(url="http://127.0.0.1:8080/api/get_shop_list", params={"id": "1", "name": "2"})
    print("get_shop_list=%s" % res.text)
    res2 = req.post(url="http://127.0.0.1:8080/api/save_shop", data={'data': '960487c8-0982-11e9-9752-bcee7b76a849', 'a2': '969d6ea6-0982-11e9-9a43-bcee7b76a849'})
    print("save_shop=%s" % res2.text)


if __name__ == "__main__":
    import json
    a = '{"data": "960487c8-0982-11e9-9752-bcee7b76a849", "aa": "97362e74-0982-11e9-a47a-bcee7b76a849"}'
    b = json.loads(a)
    # b = ast.literal_eval(a)
    print("====b=type=%s,value=%s===" % (b, type(b)))
