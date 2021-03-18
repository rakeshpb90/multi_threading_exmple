#Python 3.7.7
from multiprocessing.pool import Pool
import requests, time

def fetch(url):
    with requests.session().get(url) as response:
        print(response.json()['uuid'])

if __name__ ==  '__main__':
    url = 'https://httpbin.org/uuid'
    ts = time.time()
    result = Pool().map(fetch, [url for _ in range(50)])
    te = time.time()
    print('Time taken: {} '.format(te-ts))

