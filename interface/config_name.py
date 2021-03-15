def get_type(messages):
    list = []
    for message in messages:
        #program
        if message[0] == 1: 
            list.append(['Programme', "Type,Jour,Index,Heure,Minute,Consigne"])
        #forcing
        elif message[0] == 2:
            list.append({
                0 : ['Forcage : Éclairage',"Type,TypeForçage,Durée1/4h,Consigne"],
                1 : ['Forcage : Message réalisé',"Type,TypeForçage"],
                2 : ['Forcage : Message Ligne de viE', "Type,TypeForçage"], 
                3 : ['Forcage : Message Configuration générale', "Type,TypeForçage"], 
                4 : ['Forcage : Message Configuration programme', "Type,TypeForçage,Erase,TypePrj,Joursemaine"], 
                5 : ['Forcage : RAZ cumul', "Type,TypeForçage,PowerOnTimeerase,LampOnTimeerase,PowerLamperase,CycleNumbererase"],             
                6 : ['Forcage : Reset de la carte', "Type,TypeForçage,Password#,PasswordS,Passwordi,PasswordC,Password@"],
                7 : ['Forcage : Non utilisé', []], 
            }[message[1]])
        #Acknowledge
        elif message[0] == 3:
            list.append(['Acknowledge',""])
        #Realized
        elif message[0] == 4:
            list.append(['Realized',""])
        #configuration
        elif message[0] == 5: 
            list.append({
                0 : ['Configuration : date', "Type, Typeconfig, Année, Mois, Jour, Heure, Minute, Spare"],
                1 : ['Configuration : ephemeris', "Type, Typeconfig, Offset"],
                2 : ['Configuration : position', "Type, Typeconfig, Latitude, Longitude"],
                3 : ['Configuration : Ack' , "Type, Typeconfig,Acquittementjournalier,AcquittementSemaine,Nb OTAA"],
                4 : ['Configuration : min_button_priority', "Type, Typeconfig, DPB"],
                5 : ['Configuration : lamp_type', "Type, Typeconfig, Type de lampe"],
                6 : ['Configuration : lamp_power', "Type, Typeconfig, Puissance"], 
                7 : ['Configuration : realized_hour', "Type, Typeconfig, Heure, Minute"], 
                8 : ['Configuration : realized_freq_daily', "Type, Typeconfig,Next Step, Fréquence"], 
                9 : ['Configuration : realized_freq_minute', "Type, Typeconfig, Frequence"], 
                10 : ['Configuration : lifeline_freq_daily' , "Type, Typeconfig,Next Step, Fréquence"],
                11 : ['Configuration : lifeline_hour', "Type, Typeconfig, Heure, Minute"], 
                12 : ['Configuration : lifeline_freq', "Type, Typeconfig,Frequence"],
            }[message[1]])
        #Protocole LoRaWan
        elif message[0] == 14: 
            list.append({
                0 : ['LoRaWan : Ack_downlink', "Type,Identifiant,‘E’,‘r’,‘o’,‘r’"],
                1 : ['LoRaWan : Pass_to_classeC', "Type,Identifiant,‘O’,‘k’,‘ ’,‘C’,‘l’,‘a’,‘s’,‘s’,‘C’"]
            }[message[1]])
        #Uplink
        elif message[0] == 15: 
            list.append({
                1 : ['Uplink : Life_line', "Type,Id,V,HW,SW,Next Index0 (202A),Next Index0 (M),Next Index0 (J),Next Index0 (H),Next Index0 (M),Last Index15 (202A),Last Index15 (M),Last Index15 (J),Last Index15 (H),Last Index15 (M),last power off (202A),last power off (M),last power off (J),last power off (H),last power off (M),last power on (202A),last power on (M),last power on (J),last power on (H),last power on (M),Next consigne (202A),Next consigne (M),Next consigne (J),Next consigne (H),Next consigne (M),Now (202A),Now (M),Now (J),Now (H),Now (J),Status Prg,Tempe- rature,Lamp Status"],
                3 : ['Uplink : Realized',"Type,Id,V,HW,SW,Prev State (202A),Prev State (M),Prev State (J),Prev State (H),Prev State(M),Prev State (Consigne),Prev State (Index),Prev State (Duration),Prev State (Prg),Actual State (Idem),Lamp Status,Status Prg,Forcage,Tempe- rature,Lamp Current,Power On Time,Lamp On Time,Number Cycle,Power Lamp"],
                4 : ['Uplink : Acquitement : Programme de marche',"Type,Id,Type,Type Acq,202A,M,J,Debut (Heure),Debut (Minute),Fin (Heure),Fin (Minute),Nb de consigne,Minutes marche,Nb cycle"],
                5 : ['Uplink : Acquitement : Programme hebdomadaire', "Type,Id,Type,Type Acq,N° Sem,Nb de consigne, Minutes marche, Nb cycle"],
                6 : ['Uplink : general_configuration', "Type,Id,Type,Latitude,Longitude,Offset éphéméride,DPB*1,Type de lampe,Puissance,NSR,HR (H),HR (M),Fréquence FRJ,Fréquence FRM,NSE,HE (H),HE (M),Fréquence FEJ,Fréquence FEM,Ack journalier,Ack Semaine"], 
                7 : ['Uplink : Programme', "Type,Id,Index 0 (H),Index 0 (M),Index 0 (Consigne),Index 1 (H),Index 1 (M),Index 1 (Consigne),Index 2 (H),Index 2 (M),Index 2 (Consigne),Index 3 (H),Index 3 (M),Index 3 (Consigne),Index 4 (H),Index 4 (M),Index 4 (Consigne),Index 5 (H),Index 5 (M),Index 5 (Consigne),Index 6 (H),Index 6 (M),Index 6 (Consigne),Index 7 (H),Index 7 (M),Index 7 (Consigne),Index 8 (H),Index 8 (M),Index 8 (Consigne),Index 9 (H),Index 9 (M),Index 9 (Consigne),Index 10 (H),Index 10 (M),Index 10 (Consigne),Index 11 (H),Index 11 (M),Index 11 (Consigne),Index 12 (H),Index 12 (M),Index 12 (Consigne),Index 13 (H),Index 13 (M),Index 13 (Consigne),Index 14 (H),Index 14 (M),Index 14 (Consigne),Index 15 (H),Index 15 (M),Index 15 (Consigne)"]
            }[message[1]])
        else:
            list.append('Erreur')
    return list