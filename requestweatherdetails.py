import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=ahmedabad&appid=33b721f3521e821493f88be4f8e3799f')
print(r)
# print(r.text)
#returns html of page we requested

print(r.content)

with open('details.txt','wb') as f:
  f.write(r.content)



