from inspect import Traceback
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
""" res = requests.get('https://inventwithpython.com/page_that_does_not_exist') """

try:
    res.raise_for_status()
    playFile = open("RomeoAndJuliet.txt", "wb")
    for chunk in res.iter_content(100000):
        playFile.write(chunk)

except Exception as exc:
    print('There was a problem: %s' % (exc))

type(res)

""" class testClass:
    'requests.models.Response'
    res.status_code == requests.codes.ok
True  """ 
len('res.txt')
100000
78981
playFile.close()
""" print(res.text[:250]) """
