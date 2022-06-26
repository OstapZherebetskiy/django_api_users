
import requests
import json

# tok = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU2MTgyOTEwLCJpYXQiOjE2NTYxODI2MTAsImp0aSI6ImExMGJlOGUwMzc5YTRhMmZiMzU0ODczOGI5Y2I5ZTA5IiwidXNlcl9pZCI6MX0.RoxnV56lWmhMyQ-asNbEAyg79fp_z-zEZvBb9IVdHaQ'
ref_tok = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NjI2OTE4MiwiaWF0IjoxNjU2MTgyNzgyLCJqdGkiOiIxYWUwZWZlOTcxZTQ0Zjk5YmM3NGIyZTQzMDNjZmUwOSIsInVzZXJfaWQiOjF9.dUueXBnOiN26ohgamaV9WW7oXZ2ZyoGrYURJHlOGKk0'
# # data = {'refresh': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NjI2OTE4MiwiaWF0IjoxNjU2MTgyNzgyLCJqdGkiOiIxYWUwZWZlOTcxZTQ0Zjk5YmM3NGIyZTQzMDNjZmUwOSIsInVzZXJfaWQiOjF9.dUueXBnOiN26ohgamaV9WW7oXZ2ZyoGrYURJHlOGKk0'}

# ref = requests.post('http://127.0.0.1:8000/api/token/refresh/', data={'refresh': ref_tok})
# print(ref.content)



log = requests.post('http://127.0.0.1:8000/log/login/', data={"username":'taras',"password":"123wsx123"})
print(log.content)




# my_json = log.content.decode('utf8').replace("'", '"')


# # Load the JSON to a Python list & dump it back out as formatted JSON
# data = json.loads(my_json)
# s = json.dumps(data, indent=4, sort_keys=True)
# # print(data['access'])

# toke = 'Bearer ' + data['access']





# r = requests.get('http://127.0.0.1:8000/api/v1/userlist/', headers={'Authorization': toke})
# print(r)

# my_json = r.content.decode('utf8').replace("'", '"')
# print('- ' * 20)

# # Load the JSON to a Python list & dump it back out as formatted JSON
# data = json.loads(my_json)
# s = json.dumps(data, indent=4, sort_keys=True)
# print(s)


# z = requests.post('http://127.0.0.1:8000/api/v1/womanlist/create/', data={"title": 'jopa',  "content": 'qqqqqqqqq', "user_id": '2'})

# print(z)
# print(z.content)