import requests


def get_session():
    req = requests.session()
    data = {"username": "test", "pwd": "123456"}
    req.post("http://127.0.0.1:8000/api/login", data, verify=False)
    return req


def get_api():
    req = get_session()
    res = req.get(url="http://127.0.0.1:8000/api/get_shop_list", params={"id": "1", "name": "2"})
    print("get_shop_list=%s" % res.text)
    res2 = req.post(url="http://127.0.0.1:8000/api/save_shop", data={"id": "3", "name": "4"})
    print("save_shop=%s" % res2.text)


if __name__ == "__main__":
    get_api()
