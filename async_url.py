#Python 3.7.7
import threading, requests, time

def fetch(url):
    with requests.session().get(url) as response:
        print(response.json()['uuid'])

def main():
		iter_no = 2
    for _ in range(iter_no):
        fetch(url)

if __name__ ==  '__main__':
    url = 'https://httpbin.org/uuid'
    ts = time.time()
    thread_list = []
		thread_count = 25
    for i in range(thread_count):
        thread_list.append(threading.Thread(target=main))
        thread_list[i].start()
    for t in thread_list:
        t.join()
    te = time.time()
    print(' Time taken: {} '.format(te-ts))
