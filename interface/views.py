from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests, json
from .config_name import get_type
from .decode import Decode

def index(request):
        return render(request, 'index.html')
       
def decoder(request):
    data = request.POST.get('text', False)
    if data :
        try:
            # res = requests.get('http://127.0.0.1:8080/decode?data=' + json.dumps(data))
            # message = json.loads(res.content)['message']
            message = Decode(data).decode()
            return render(request, 'decoder.html',{'message':message, 'type': get_type(message)})
        except ValueError:
            messages.error(request,'Veuillez entrer un bon code SVP')
            return render(request, 'decoder.html')
    else :
        messages.error(request,'Veuillez entrer un code SVP')
        return render(request, 'decoder.html')

def connect(request):
    return render(request, 'connect.html')


def journal(request):
    data = request.POST.get('text', False)
    res1 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices?limit=1000&offset=0',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
    names = dict()
    for i in range(len(res1)):
        res3 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices/'+res1[i]['id'],headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
        names.update({ res1[i]['name'] : res3['interfaces'][0]['definition']['devEUI']})


    if data :
        res2 = json.loads(requests.get('https://liveobjects.orange-business.com/api/v0/auditlog/messages?offset=0&limit=100&sort=desc',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
        payloads = []
        for i in range(len(res2)):
            if 'payload' in res2[i]['content'] and res2[i]['content']['payload'][0] == 'F' and res2[i]['source']['nodeId'] == names[data]:
                payloads.append(res2[i]['content']['payload'])

        Datas = []
        for data in payloads:
            #Datas += json.loads(requests.get('http://127.0.0.1:8080/decode?data=' + json.dumps(data)).content)['message']
            Datas += Decode(data).decode()
        return render(request, 'journal.html',{'devices': list(names.keys()), 'payloads': Datas, 'type': get_type(Datas)})
    else:
        return render(request, 'journal.html',{'devices': list(names.keys())})

def Login(request):
    # Fonction d'authentification de l'utilisateur.
    username = request.POST.get('username', 'nothing')
    print(username)
    mdp = request.POST.get('mdp', 'nothing')
    user = authenticate(username=username, password=mdp)
    if user is not None:
        login(request, user)
        return render(request, 'index.html', {'user': user})
    else:
        # adresse ou mdp incorrect
        messages.error(request,'Identifiants incorrects')
        return render(request, 'connect.html')

def Logout(request):
	# Page de déconnexion, déconnecte et renvoie à l'accueil
	logout(request)
	return render(request, 'index.html')