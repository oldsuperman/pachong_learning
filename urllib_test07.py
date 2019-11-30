from urllib import request
from urllib import error
# HTTPError示例
if __name__ == "__main__":

    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)

    try:
        response = request.urlopen(req)

    except error.HTTPError as e:
        print(e.code)
        print(e.reason)
