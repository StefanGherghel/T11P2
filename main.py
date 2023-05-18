import threading


def stage1PIPELINE(ADT: list):
    alfa: int = 4
    size = len(ADT)
    for i in range(size):
        element = ADT[0]
        ADT.remove(element)
        ADT.append(element*alfa)

def stage2PIPELINE(ADT: list):
    ADT.sort()

def stage3PIPELINE(ADT: list):
    print(ADT)

if __name__=='__main__':

    ADT = [5,7,1,4,9,3,2]

    thread_1 = threading.Thread(target=stage1PIPELINE(ADT))
    thread_2 = threading.Thread(target=stage2PIPELINE(ADT))
    thread_3 = threading.Thread(target=stage3PIPELINE(ADT))


    thread_3.start()
    thread_3.join()

    thread_1.start()
    thread_2.start()

    thread_2.join()
    thread_1.join()