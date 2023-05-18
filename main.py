import asyncio
from queue import Queue

coada = Queue()
async def gauss(queue: Queue):
    n = queue.get()
    rez = 0
    for i in range (1,n):
        await asyncio.sleep(1)
        rez = rez+i
    print("Rezultat suma Gauss pentru"+str(n)+": " +str(rez)+"\n")


async def main():
    for i in range(2,6):
        coada.put(i)

    await asyncio.gather(
        gauss(coada),
        gauss(coada),
        gauss(coada),
        gauss(coada)
        )


if __name__ == '__main__':
    asyncio.run(main())