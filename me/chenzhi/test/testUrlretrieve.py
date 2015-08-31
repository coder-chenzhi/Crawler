__author__ = 'chenzhi'

import urllib
def cbk(a, b, c):
    '''callback
    @a: blocks already downloaded
    @b: size of block
    @c: size of file
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '%.2f%%' % per

url = 'http://www.cs.zju.edu.cn/wescms/sys/filebrowser/file.php?cmd=download&id=143002'
local = 'd://sina.xls'
urllib.urlretrieve(url, local, cbk)