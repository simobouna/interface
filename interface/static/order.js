var order = document.getElementById("order");
var type = document.getElementById("type");
var container = document.getElementById("container");
orders = {
    '1' : {
        'Programme': "Type,Jour,Index,Heure,Consigne"
    },
    '2' : {
        'Éclairage': "Type,TypeForçage,Durée1/4h,Consigne",
        'Message réalisé': "Type,TypeForçage",
        'Message Ligne de viE': "Type,TypeForçage",
        'Message Configuration générale': "Type,TypeForçage",
        'Message Configuration programme': "Type,TypeForçage,Erase,TypePrj,Joursemaine",
        'RAZ cumul': "Type,TypeForçage,PowerOnTimeerase,LampOnTimeerase,PowerLamperase,CycleNumbererase",
        'Reset de la carte': "Type,TypeForçage,Password#,PasswordS,Passwordi,PasswordC,Password@",
    },
    '5' : {
        'Date': "Type, Typeconfig, Date, Heure, Spare",
        'Ephemeris':"Type, Typeconfig, Offset",
        'Position':"Type, Typeconfig, Latitude, Longitude",
        'Ack': "Type, Typeconfig,Acquittementjournalier,AcquittementSemaine,Nb OTAA",
        'Min_button_priority': "Type, Typeconfig, DPB",
        'Lamp_type': "Type, Typeconfig, Type de lampe",
        'Lamp_power': "Type, Typeconfig, Puissance",
        'Realized_hour': "Type, Typeconfig, Heure",
        'Realized_freq_daily': "Type, Typeconfig,Next Step, Fréquence",
        'Realized_freq_minute': "Type, Typeconfig, Frequence",
        'Lifeline_freq_daily': "Type, Typeconfig,Next Step, Fréquence",
        'Lifeline_hour': "Type, Typeconfig, Heure",
        'Lifeline_freq': "Type, Typeconfig,Frequence"
    }    ,
}
order.onchange = function (){  
    type.length = 1;
    //display correct values
    var i
    var types = Object.keys(orders[this.value]);
    for (i = 0; i < types.length; i++) {
        type.options[type.options.length] = new Option(types[i], types[i]);
    }
}
type.onchange = function (){
    document.getElementById("input").remove();
    input = document.createElement("div");
    input.setAttribute("class","row");
    input.setAttribute("style","margin-top: 5%;");
    input.setAttribute("id","input");
    var i;
    titles = orders[order.value][this.value].split(',');
    tmp = document.createElement('h4');
    tmp.textContent = titles[0];
    input.append(tmp);
    tmp = document.createElement('input');
    tmp.setAttribute("class","input--style-4");
    tmp.setAttribute("type","text");
    tmp.setAttribute("value",order.value);
    input.append(tmp);
    if (order.value != 1){
        tmp = document.createElement('h4');
        tmp.textContent = titles[1];
        input.append(tmp);
        tmp = document.createElement('input');
        tmp.setAttribute("class","input--style-4");
        tmp.setAttribute("type","text");
        tmp.setAttribute("value",Object.keys(orders[order.value]).indexOf(type.value));
        input.append(tmp);
    }

    for (i = 2; i < titles.length; i++) {
        tmp = document.createElement('h4');
        tmp.textContent = titles[i];
        input.append(tmp);
        tmp = document.createElement('input');
        tmp.setAttribute("class","input--style-4");
        tmp.setAttribute("type","text");
        input.append(tmp);
    }
    container.append(input);
}