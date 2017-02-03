import requests
import json


app_url = 'http://localhost:8080/'

# get all
r = requests.get(app_url+'api/users')
print '------------------'
print r.url
print r.text
'''
# create new
r = requests.post(app_url+'api/users', data = json.dumps({'username':'djordje', 'password': '1234'}))
print '------------------'
print r.url
print r.text

start_time = time.time()
end_time = time.time()
print("Finished in: {0}".format(end_time-start_time))

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
