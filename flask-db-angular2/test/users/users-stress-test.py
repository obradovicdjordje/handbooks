import requests
import time, threading
from random import randint
from time import sleep


app_url = 'http://localhost:8080/'

def process_block():
    for i in range(100):
        r = requests.get(app_url+'users')
        sleep(0.05)

Pool = []
    
def start_threads(amount=5):
	for i in range(amount):
		 thread = threading.Thread(target=process_block)
		 thread.start()
		 Pool.append(thread)


start_time = time.time()
start_threads(10)
for t in Pool:
	t.join()
		
end_time = time.time()
print("Finished in: {0}".format(end_time-start_time))

'''
# get all
r = requests.get(app_url+'users')
print '------------------'
print r.url
print r.text

# create new
r = requests.post(app_url+'users', data = {'username':'djordje', 'passwd': '1234'})
print '------------------'
print r.url
print r.text

# get by id
r = requests.get(app_url+'users/%i'%(3))
print '------------------'
print r.url
print r.text


# update by id
r = requests.put(app_url+'users/%i'%(3), data = {'username':'nesto', 'passwd': '4321'})
print '------------------'
print r.url
print r.text

# delete by id
r = requests.delete(app_url+'users/%i'%(3))
print '------------------'
print r.url
print r.text

# user login
r = requests.get(app_url+'users/login/?username=%s&passwd=%s'%('djordje', '1234'))
print '------------------'
print r.url
print r.text
'''
