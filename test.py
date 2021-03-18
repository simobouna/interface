import requests, json

# res1 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)


# names = dict()
# for i in range(len(res1)):
#     names.update({ res1[i]['name'] : res1[i]['id']})

# print(names['NRGYBOX_0000111'])
# res2 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v0/auditlog/messages?offset=0&limit=100&sort=desc&filters=' + names['NRGYBOX_0000111'],headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)

# payloads = []
# for i in range(len(res2)):
#      if 'payload' in res2[i]['content'] and res2[i]['content']['payload'][0] == 'F':
#         payloads.append(res2[i]['content']['payload'])

# print(payloads)

res = json.loads(requests.get('https://liveobjects.orange-business.com/api/v0/auditlog/messages?offset=0&limit=1&sort=desc&@any=mac',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)

print(res[0]['timestamp'][:16])
