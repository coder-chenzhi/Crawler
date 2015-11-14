__author__ = 'chenzhi'

import requests

if __name__ == "__main__":
    mogujie_url = "http://www.mogujie.com/shopping/"
    liwushuo_url = "http://www.liwushuo.com/"
    r = requests.get(liwushuo_url)
    page = r.content
    with open("liwushuo.html", "w") as f:
        f.write(page)
    print "Done."