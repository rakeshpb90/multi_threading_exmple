#Python 3.7.7
import requests, time

def fetch(url):

    with requests.session().get(url) as response:
        print(response.json()['uuid'])

if __name__ ==  '__main__':
    url = 'https://httpbin.org/uuid'
    ts = time.time()
    for _ in range(50):
        fetch(url)
    te = time.time()
    print(' Time taken: {} '.format(te-ts))

