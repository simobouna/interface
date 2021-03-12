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
                1 : ['Uplink : Life_line', "Type,Identifiant,Version,HW,SW,Prochain démarrage Index 0 (Heure),Prochain démarrage Index 0 (Minute),Dernière Extinction Index 15 (Heure),Dernière Extinction Index 15 (Minute),Dernière mise hors tension de l’NRGYBOX (Heure),Dernière mise hors tension de l’NRGYBOX (Minute),Dernière mise sous tension de l’NRGYBOX (Heure),Dernière mise sous tension de l’NRGYBOX (Minute),Prochaine consigne à exécuter (Heure),Prochaine consigne à exécuter (Minute),Heure courante (Heure),Heure courante (Minute),Status_Prg,Temperature,Lamp_Status"],
                3 : ['Uplink : Realized',"Type,Identifiant,Version,HW,SW,Prev_State(Année),Prev_State(Mois),Prev_State(Jour),Prev_State(Heure),Prev_State(Minute),Prev_State(Consigne),Prev_State(Index),Prev_State(Duration),Prev_State(Prg),Actual_State(Idem),Lamp_Status,Status Prg,Forcage,Temperature,Lamp_Current,PowerOnTime,LampOnTime,NumberCycle,PowerLamp"],
                4 : ['Uplink : Acquitement : Programme de marche',"Type,Identifiant,Type,TypeAcq,Année,Mois,Jour,Debut(Heure),Debut(Minute),Fin(Heure),Fin(Minute),Nb de consigne,Minutes marche,Nbcycle"],
                5 : ['Uplink : Acquitement : Programme hebdomadaire', "Type,Identifiant,Type,Type Acq,N° Sem,Nb de consigne, Minutesmarche, Nbcycle"],
                6 : ['Uplink : general_configuration', "Type,Identifiant,Type,Latitude,Longitude,Offset éphéméride,DPB*1,Type de lampe,Puissance,NSR,HR (Heure),HR (Minute),Fréquence FRJ,Fréquence FRM,NSE,HE (Heure),HE (Minute),Fréquence FEJ,Fréquence FEM,Acquittement journalier,Acquittement Semaine"], 
                7 : ['Uplink : Programme', "Type,Identifiant,Index 0 (Heure),Index 0 (Minute),Index 0 (Consigne),Index 1 (Heure),Index 1 (Minute),Index 1 (Consigne),Index 2 (Heure),Index 2 (Minute),Index 2 (Consigne),Index 3 (Heure),Index 3 (Minute),Index 3 (Consigne),Index 4 (Heure),Index 4 (Minute),Index 4 (Consigne),Index 5 (Heure),Index 5 (Minute),Index 5 (Consigne),Index 6 (Heure),Index 6 (Minute),Index 6 (Consigne),Index 7 (Heure),Index 7 (Minute),Index 7 (Consigne),Index 8 (Heure),Index 8 (Minute),Index 8 (Consigne),Index 9 (Heure),Index 9 (Minute),Index 9 (Consigne),Index 10 (Heure),Index 10 (Minute),Index 10 (Consigne),Index 11 (Heure),Index 11 (Minute),Index 11 (Consigne),Index 12 (Heure),Index 12 (Minute),Index 12 (Consigne),Index 13 (Heure),Index 13 (Minute),Index 13 (Consigne),Index 14 (Heure),Index 14 (Minute),Index 14 (Consigne),Index 15 (Heure),Index 15 (Minute),Index 15 (Consigne)"]
            }[message[1]])
        else:
            list.append('Erreur')
    return list