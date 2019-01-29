import random
import time
import os
import uuid
import threading

dataMarts = ['HELLOWORLD', 'VPNDATA', 'RANGERFOR', 'WEBEXTRACK', 'WORLDABCD']
dataSourceLocation = '../dumpOld'

startTime = time.time()


def nfilescreationextension(n, s):
    print("thread name is : ", threading.current_thread().getName())
    for i in range(n):
        filename = random.choice(dataMarts)+"_"+str(random.randint(100000000, 999999999))
        os.mknod(dataSourceLocation + "/" + filename)
        time.sleep(s)


def nfilecreationuuid(n, s):
    print("thread name is : ", threading.current_thread().getName())
    for i in range(n):
        open(str(dataSourceLocation + "/" + str(uuid.uuid4())), 'a').close()
        time.sleep(s)


print("thread name is : ", threading.current_thread().getName())

t1 = threading.Thread(target=nfilescreationextension, args=(10,2,))
t1.start()

t2 = threading.Thread(target=nfilecreationuuid, args=(5, 2,))
t2.start()
print("thread name is : ", threading.current_thread().getName())

t1.join()
t2.join()
endTime = time.time()

print("Total time for source to store dump : ", endTime - startTime)
