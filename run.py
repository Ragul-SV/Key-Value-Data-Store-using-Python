
import threading 
from threading import Thread
import time
import application as app       #importing application.py code here
import json

class newThread(Thread):        #Thread Class
    def __init__(self,id,target,args):
        threading.Thread.__init__(self)
        self.threadID = id
        self.function = target
        self.args = args

    def run(self):
        print("---------------------Starting " + self.name+"------------------")
        
        threadLock.acquire()    # Acquire lock to synchronize thread

        if len(self.args)==1:
            self.function(self.args[0]);
        if len(self.args)==2:
            self.function(self.args[0],self.args[1]);
        if len(self.args)==3:
            self.function(self.args[0],self.args[1],self.args[2]);

        threadLock.release()    # Release lock 

        print("---------------------Exiting " + self.name+"-------------------")

threadLock = threading.Lock()   #Creating Thread Lock
threads = []

# Create new threads
thread1 = newThread(1,app.create, ["ComputerScience",95])
thread2 = newThread(2,app.create, ["Physics",85])
thread3 = newThread(3,app.read, ["Physics"])
thread4 = newThread(4,app.read, ["ComputerScience"])
thread5 = newThread(5,app.delete, ["Physics"])
thread6 = newThread(6,app.read, ["Physics"])
thread7 = newThread(7,app.create, ["English123$",88,5])
thread8 = newThread(8,app.create, ["Chemistry",92,10])
thread9 = newThread(8,app.create, ["Maths",89])

# Start new Threads
thread1.start()
time.sleep(1)
thread2.start()
time.sleep(1)
thread7.start()
time.sleep(3)
thread3.start()
time.sleep(1)
thread5.start()
time.sleep(1)
thread4.start()
time.sleep(1)
thread6.start()
time.sleep(1)
thread8.start()
time.sleep(1)
thread9.start()

    
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)
threads.append(thread6)
threads.append(thread7)
threads.append(thread8)
threads.append(thread9)

# Wait for all threads to complete
for t in threads:
    t.join()

with open("datastore.json", "w") as outfile:    #exporting the dictionary as a json file
    json.dump(app.d, outfile) 

print("Finished!!")
