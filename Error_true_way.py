from urllib import request
from urllib import error

if __name__ == "__main__":

    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
    #将HTTP放在URL的前面，因为HTTPError为URLError的子类
    except error.HTTPError as e:
        print("HTTPError")
        print(e.code)
    except error.URLError as e:
        print("URLError")
        print(e.reason)
