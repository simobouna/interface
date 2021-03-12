import requests, json

res1 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
res2 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v0/auditlog/messages?offset=0&limit=1000&sort=desc',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)

# names = dict()
# for i in range(len(res1)):
#         res3 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices/'+res1[i]['id'],headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
#         names.update({ res1[i]['name'] : res3['interfaces'][0]['definition']['devEUI']})


# payloads = []
# for i in range(len(res2)):
#      if 'payload' in res2[i]['content'] and res2[i]['content']['payload'][0:2] == 'F3':
#         payloads.append(res2[i]['content']['payload'])

print(res2[0]['source']['nodeId'])
