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
            message = Decode(data).decode()
            print(message)
            title = []
            for msg in message:
                title.append(get_type(msg))
            return render(request, 'decoder.html',{'message':message, 'type': title})
        except :
            messages.error(request,'Veuillez entrer un bon code SVP')
            return render(request, 'decoder.html')
    else :
        return render(request, 'decoder.html')

def connect(request):
    return render(request, 'connect.html')


def journal(request):
    name = request.POST.get('name', False)
    date_from = request.POST.get('date_from', False)
    date_to = request.POST.get('date_to', False)
    type_message = request.POST.get('select_type', False)
    filter_message = request.POST.get('filter_message', False)
    limit = request.POST.get('limit', False)
    nrgyboxs = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices?limit=1000&offset=0',headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
    names = dict()
    for i in range(len(nrgyboxs)):
        names.update({ nrgyboxs[i]['name'] : nrgyboxs[i]['id']})
    if name :
        nodeId = json.loads(requests.get('https://liveobjects.orange-business.com/api/v1/deviceMgt/devices/'+names[name],headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)['interfaces'][0]['nodeId']
        requete = 'https://liveobjects.orange-business.com/api/v0/auditlog/messages?offset=0&sort=desc&limit='+ limit + '&source.nodeId=' + nodeId
        if date_from :
            requete +=  '&from='+ date_from
        if date_to:
            requete +=  '&to='+ date_to
        if filter_message:
            requete +=  '&@any='+ filter_message
        msgs = json.loads(requests.get(requete,headers={'X-API-KEY': 'f4c185cd78404771bb9edfc3b614f2da'}).content)
        output_titles = []
        output_values = []

        if type_message == '0':
            for i in range(len(msgs)):
                tmp_value = []

                tmp_value.append(msgs[i]['timestamp'][:16].replace('-','/').replace('T',' '))

                tmp_value.append(msgs[i]['description']) 

                index = msgs[i]['detailedDescription'].lower().find('mac')
                if  index == -1:
                    if msgs[i]['description'].lower().find('join') != -1:
                        tmp_value.append(msgs[i]['detailedDescription'])
                    else :
                        tmp_value.append("Vide")
                else:
                    tmp_value.append(msgs[i]['detailedDescription'][index:])

                if 'port' in msgs[i]['content']: 
                    tmp_value.append(msgs[i]['content']['port']) 
                else : 
                    tmp_value.append("Vide")

                if 'fcnt' in msgs[i]['content']['frameHeader']: 
                    tmp_value.append(msgs[i]['content']['frameHeader']['fcnt']) 
                else : 
                    tmp_value.append("Vide")

                if 'signal' in msgs[i]['content']: 
                    tmp_value.append(msgs[i]['content']['signal']['sf']) 
                else : 
                    tmp_value.append("Vide")


                if 'payload' in msgs[i]['content'] :
                    data = msgs[i]['content']['payload']
                    try :
                        decode = Decode(data).decode()
                        for msg in decode:
                            output_titles.append([get_type(msg)[0],"Timestamp,Desc,Detail desc,Port,fcnt,sf," + get_type(msg)[1],'000000'+get_type(msg)[2]])
                            output_values.append( tmp_value + msg)
                    except :
                        output_titles.append(["Message","Timestamp,Desc,Detail desc,Port,fcnt,sf",'000000'])
                        output_values.append(tmp_value)
                else :
                    output_titles.append(["Message","Timestamp,Desc,Detail desc,Port,fcnt,sf",'000000'])
                    output_values.append(tmp_value)
            return render(request, 'journal.html',{'devices': list(names.keys()), 'payloads': output_values, 'type': output_titles ,'type_message': type_message})
        else :
            for i in range(len(msgs)):
                if 'payload' in msgs[i]['content'] and msgs[i]['content']['payload'][0:2] == type_message:
                    tmp_value = []

                    tmp_value.append(msgs[i]['timestamp'][:16].replace('-','/').replace('T',' '))

                    tmp_value.append(msgs[i]['description']) 

                    index = msgs[i]['detailedDescription'].lower().find('mac')
                    if  index == -1:
                        if msgs[i]['description'].lower().find('join') != -1:
                            tmp_value.append(msgs[i]['detailedDescription'])
                        else :
                            tmp_value.append("Vide")
                    else:
                        tmp_value.append(msgs[i]['detailedDescription'][index:])

                    if 'port' in msgs[i]['content']: 
                        tmp_value.append(msgs[i]['content']['port']) 
                    else : 
                        tmp_value.append("Vide")

                    if 'fcnt' in msgs[i]['content']['frameHeader']: 
                        tmp_value.append(msgs[i]['content']['frameHeader']['fcnt']) 
                    else : 
                        tmp_value.append("Vide")

                    if 'signal' in msgs[i]['content']: 
                        tmp_value.append(msgs[i]['content']['signal']['sf']) 
                    else : 
                        tmp_value.append("Vide")

                    data = msgs[i]['content']['payload']
                    try :
                        decode = Decode(data).decode()
                        for msg in decode:
                            output_titles.append([get_type(msg)[0],"Timestamp,Desc,Detail desc,Port,fcnt,sf," + get_type(msg)[1],'000000'+get_type(msg)[2]])
                            output_values.append( tmp_value + msg)
                    except :
                        output_titles.append(["Message","Timestamp,Desc,Detail desc,Port,fcnt,sf",'000000'])
                        output_values.append(tmp_value)

            return render(request, 'journal.html',{'devices': list(names.keys()), 'payloads': output_values, 'type': output_titles, 'type_message': type_message})
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