window.onload = function() {
    var order = document.getElementById("order");
    var type = document.getElementById("type");
    var container = document.getElementById("container");
    orders = {
        '1' : {
            'Programme': "Type,Jour,Index,Heure,Minute,Consigne"
        },
        '2' : {
            'Éclairage': "Type,TypeForçage,Durée1/4h,Consigne",
            'Message réalisé': "Type,TypeForçage",
            'Message Ligne de viE': "Type,TypeForçage",
            'Message Configuration générale': "Type,TypeForçage",
            'Message Configuration programme': "Type,TypeForçage,Erase (0: NOK | 1: OK),TypePrj,Joursemaine (0-6: Jour | 7: toute la semaine)",
            'RAZ cumul': "Type,TypeForçage,PowerOnTimeerase (0: NOK | 1: OK),LampOnTimeerase(0: NOK | 1: OK),PowerLamperase(0: NOK | 1: OK),CycleNumbererase(0: NOK | 1: OK)",
            'Redémarrage': "Type,TypeForçage",
        },
        '5' : {
            'Date': "Type, Typeconfig, Année,Mois,Jour,Heure,Minute",
            'Ephéméride':"Type, Typeconfig, Offset (-2.1 = 21)",
            'Adresse':"Type, Typeconfig, Adresse",
            'Acquittement': "Type, Typeconfig,Acquittementjournalier (0: NOK | 1: OK),AcquittementSemaine (0: NOK | 1: OK),Nb OTAA",
            'Min_button_priority': "Type, Typeconfig, DPB",
            'Lamp_type': "Type, Typeconfig, Type de lampe",
            'Lamp_power': "Type, Typeconfig, Puissance",
            'Realized_hour': "Type, Typeconfig,Heure,Minute",
            'Realized_freq_daily': "Type, Typeconfig,Next Step (0: Désactivé | 1: Changement d'index), Fréquence",
            'Realized_freq_minute': "Type, Typeconfig, Frequence",
            'Lifeline_freq_daily': "Type, Typeconfig,Next Step (0: Désactivé | 1: Changement d'index), Fréquence",
            'Lifeline_hour': "Type, Typeconfig, Heure (24: Power On | 25: Index 0 | 26: Index 15),Minute",
            'Lifeline_freq': "Type, Typeconfig,Frequence"
        }    ,
    }

    order.onchange = function (){ 
        localStorage["order"] = this.value; 
        type.length = 1;
        //display correct values
        var i
        var types = Object.keys(orders[this.value]);
        for (i = 0; i < types.length; i++) {
            type.options[type.options.length] = new Option(types[i],i);
        }
    }
    type.onchange = function (){
        localStorage["type"] = this.value;
        var types = Object.keys(orders[order.value]);
        document.getElementById("input").remove();
        input = document.createElement("div");
        input.setAttribute("class","row");
        input.setAttribute("style","margin-top: 5%;");
        input.setAttribute("id","input");
        var i;
        titles = orders[order.value][types[this.value]].split(',');
        tmp = document.createElement('input');
        tmp.setAttribute("class","input--style-4");
        tmp.setAttribute("type","text");
        tmp.setAttribute("name",0);
        tmp.setAttribute("value",order.value);
        tmp.setAttribute("type","hidden");
        input.append(tmp);
        var start = 1;
        if (order.value != 1){
            tmp = document.createElement('input');
            tmp.setAttribute("class","input--style-4");
            tmp.setAttribute("type","text");
            tmp.setAttribute("name",1);
            tmp.setAttribute("value",type.value);
            tmp.setAttribute("type","hidden");
            input.append(tmp);
            start = 2;
        }
        for (i = start; i < titles.length; i++) {
            tmp = document.createElement('h4');
            tmp.textContent = titles[i];
            input.append(tmp);
            tmp = document.createElement('input');
            tmp.setAttribute("class","input--style-4");
            tmp.setAttribute("type","text");
            tmp.setAttribute("name",i);
            input.append(tmp);
        }
        container.append(input);
    }
    var devices = JSON.parse(document.getElementById('name_var').textContent);
    var groupes = JSON.parse(document.getElementById('groupe_var').textContent);
    var tags = JSON.parse(document.getElementById('tag_var').textContent);
    var groupe_select = document.getElementById("groupe");
    var device_select = document.getElementById("name");
    var tag_select = document.getElementById("tag");
    var i
    for (i = 0; i < groupes.length; i++) {
        groupe_select.options[groupe_select.options.length] = new Option(groupes[i], groupes[i]);
    }
    groupe_select.onchange = function() {
        localStorage["groupe"] = this.value;
        device_select.length = 0;
        //display correct values
        var i
        for (i = 0; i < devices.length; i++) {
            split = devices[i].split(',');
            if (split[1].search(this.value) != -1){
                device_select.options[device_select.options.length] = new Option(split[0], split[0]);
            }
        }
    }
    tag_select.onchange = function() {
        localStorage["tag"] = this.value;
        device_select.length = 0;
        //display correct values
        var i
        for (i = 0; i < devices.length; i++) {
            split = devices[i].split(',');
            if (split[2].search(this.value) != -1){
                device_select.options[device_select.options.length] = new Option(split[0], split[0]);
            }
        }
    }
    var i;
    for (i = 0; i < tags.length; i++) {
    option = document.createElement('option');
    option.setAttribute("value", tags[i]);
    option.textContent = tags[i];
    tag_select.append(option);
    }
    if (localStorage["groupe"]) {
        groupe_select.value = localStorage["groupe"]; 
        //display correct values
        var i
        for (i = 0; i < devices.length; i++) {
            split = devices[i].split(',');
            if (split[1].search(groupe_select.value) != -1){
                device_select.options[device_select.options.length] = new Option(split[0], split[0]);
            }
        }
    }
    if (localStorage["tag"]) { 
        tag.value = localStorage["tag"];
        //display correct values
        var i
        for (i = 0; i < devices.length; i++) {
            split = devices[i].split(',');
            if (split[2].search(tag_select.value) != -1){
                device_select.options[device_select.options.length] = new Option(split[0], split[0]);
            }
        } 
      }
      if (localStorage["order"]) { 
        order.value = localStorage["order"];
        //display correct values
        var i
        type.length = 1;
        //display correct values
        var i
        var types = Object.keys(orders[order.value]);
        for (i = 0; i < types.length; i++) {
            type.options[type.options.length] = new Option(types[i],i);
        } 
      }

}
