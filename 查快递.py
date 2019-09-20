import requests

name = input('Name:')
id = input('Id:')
url = 'https://www.kuaidi100.com/query'
params = {
    'phone':'',
    'type':name,
    'postid':id,
    'temp':'0.048482591051014046'
}
res = requests.get(url,params= params)
json = res.json()
print(json['data'][0]['context'])