def get_type(message):
    #program
    if message[0] == 1: 
        return ['Programme', "Type,Jour,Index,Heure,Consigne","00020"]
    #forcing
    elif message[0] == 2:
        return {
            0 : ['Forcage : Éclairage',"Type,TypeForçage,Durée1/4h,Consigne","0000"],
            1 : ['Forcage : Message réalisé',"Type,TypeForçage","00"],
            2 : ['Forcage : Message Ligne de viE', "Type,TypeForçage","00"], 
            3 : ['Forcage : Message Configuration générale', "Type,TypeForçage","00"], 
            4 : ['Forcage : Message Configuration programme', "Type,TypeForçage,Erase,TypePrj,Joursemaine","00000"], 
            5 : ['Forcage : RAZ cumul', "Type,TypeForçage,PowerOnTimeerase,LampOnTimeerase,PowerLamperase,CycleNumbererase","000000"],             
            6 : ['Forcage : Reset de la carte', "Type,TypeForçage,Password#,PasswordS,Passwordi,PasswordC,Password@","0000000"],
            7 : ['Forcage : Non utilisé', ""], 
        }[message[1]]
    #Acknowledge
    elif message[0] == 3:
        return ['Acknowledge',""]
    #Realized
    elif message[0] == 4:
        return ['Realized',""]
    #configuration
    elif message[0] == 5: 
        return {
            0 : ['Configuration : date', "Type, Typeconfig, Date, Heure, Spare","00320"],
            1 : ['Configuration : ephemeris', "Type, Typeconfig, Offset","000"],
            2 : ['Configuration : position', "Type, Typeconfig, Latitude, Longitude","0000"],
            3 : ['Configuration : Ack' , "Type, Typeconfig,Acquittementjournalier,AcquittementSemaine,Nb OTAA","00000"],
            4 : ['Configuration : min_button_priority', "Type, Typeconfig, DPB","000"],
            5 : ['Configuration : lamp_type', "Type, Typeconfig, Type de lampe","000"],
            6 : ['Configuration : lamp_power', "Type, Typeconfig, Puissance","000"], 
            7 : ['Configuration : realized_hour', "Type, Typeconfig, Heure","002"], 
            8 : ['Configuration : realized_freq_daily', "Type, Typeconfig,Next Step, Fréquence","0000"], 
            9 : ['Configuration : realized_freq_minute', "Type, Typeconfig, Frequence","000"], 
            10 : ['Configuration : lifeline_freq_daily' , "Type, Typeconfig,Next Step, Fréquence","0000"],
            11 : ['Configuration : lifeline_hour', "Type, Typeconfig, Heure","000"], 
            12 : ['Configuration : lifeline_freq', "Type, Typeconfig,Frequence","000"],
        }[message[1]]
    #Protocole LoRaWan
    elif message[0] == 14: 
        return {
            0 : ['LoRaWan : Ack_downlink', "Type,Identifiant,‘E’,‘r’,‘o’,‘r’","000000"],
            1 : ['LoRaWan : Pass_to_classeC', "Type,Identifiant,‘O’,‘k’,‘ ’,‘C’,‘l’,‘a’,‘s’,‘s’,‘C’","00000000000"]
        }[message[1]]
    #Uplink
    elif message[0] == 15: 
        return {
            1 : ['Uplink : Life_line', "Type,Id,V,HW,SW,Next Index0 (Date),Next Index0 (Heure),Last Index15 (Date),Last Index15 (Heure),last power off (Date),last power off (Heure),last power on (Date),last power on (Heure),Next consigne (Date),Next consigne (Heure),Now (Date),Now (Heure),Status Prg,Tempe- rature,Lamp Status","00000323232323232000"],
            3 : ['Uplink : Realized',"Type,Id,V,HW,SW,Prev State (Date),Prev State (Heure),Prev State (Consigne),Prev State (Index),Prev State (Duration),Prev State (Prg),Actual State (Date),Actual State (Heure),Actual State (Consigne),Actual State (Index),Actual State (Duration),Actual State (Prg),Lamp Status,Status Prg,Forcage,Tempe- rature,Lamp Current,Power On Time,Lamp On Time,Number Cycle,Power Lamp","00000320000320000000000000"],
            4 : ['Uplink : Acquitement : Programme de marche',"Type,Id,Type,Type Acq,Date,Debut (Heure),Fin (Heure),Nb de consigne,Minutes marche,Nb cycle","0000322000"],
            5 : ['Uplink : Acquitement : Programme hebdomadaire', "Type,Id,Type,Type Acq,N° Sem,Nb de consigne, Minutes marche, Nb cycle","00000000"],
            6 : ['Uplink : general_configuration', "Type,Id,Type,Latitude,Longitude,Offset éphéméride,DPB*1,Type de lampe,Puissance,NSR,HR (Heure),Fréquence FRJ,Fréquence FRM,NSE,HE (Heure),Fréquence FEJ,Fréquence FEM,Ack journalier,Ack Semaine","0000000000200020000"], 
            7 : ['Uplink : Programme', "Type,Id,Type,Type Prj,Jour,Index 0 (Heure),Index 0 (Consigne),Index 1 (Heure),Index 1 (Consigne),Index 2 (Heure),Index 2 (Consigne),Index 3 (Heure),Index 3 (Consigne),Index 4 (Heure),Index 4 (Consigne),Index 5 (Heure),Index 5 (Consigne),Index 6 (Heure),Index 6 (Consigne),Index 7 (Heure),Index 7 (Consigne),Index 8 (Heure),Index 8 (Consigne),Index 9 (Heure),Index 9 (Consigne),Index 10 (Heure),Index 10 (Consigne),Index 11 (Heure),Index 11 (Consigne),Index 12 (Heure),Index 12 (Consigne),Index 13 (Heure),Index 13 (Consigne),Index 14 (Heure),Index 14 (Consigne),Index 15 (Heure),Index 15 (Consigne)","0000020202020202020202020202020202020"]
        }[message[1]]
    else:
        return 'Erreur'
