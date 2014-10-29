import requests

tolken = ('b5e76a8058b4977727fa4f9703da9601b7b2acc8', '')
r = requests.get('https://api.github.com/users/syndbg/followers',  auth=tolken)
for x in r.json():
    #j = requests.get('https://api.github.com/users/{}/followers'.format(x['login']),  auth=tolken)
    #for l in j.json():
    print(x['login'])



#tolken = b5e76a8058b4977727fa4f9703da9601b7b2acc8
