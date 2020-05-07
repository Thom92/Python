import requests
import re

def get_url_name(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects = True)
filename = get_url_name(r.headers.get('content-disposition'))
open(filename, 'wb').write(r.content)
    







