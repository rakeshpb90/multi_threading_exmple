#Python 3.7.7
import asyncio, aiohttp, time

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url)
        json_res = await response.json()
        print(json_res['uuid'])

async def main():
    task = [fetch(url) for _ in range(50)]
    await asyncio.gather(*task)

if __name__ ==  '__main__':
    url = 'https://httpbin.org/uuid'
    ts = time.time()
    asyncio.run(main())
    te = time.time()
    print(' Time taken: {} '.format(te-ts))
