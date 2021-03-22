def get_next_bits():
    return {
        1:  1, #inutile
        2:  3,
        3:  1, #inutile
        4:  1, #inutile
        5:  4,
        14: 4,
        15: 4
    }

def get_type_index():
    return {
        1: 'program',
        2: 'forcing',
        3: 'acknowledge',
        4: 'realized',
        5: 'configuration',
        14: 'Protocole LoRaWan',
        15: 'Uplink'
    }

def get_type(type, second_type):
    #program
    if type == 1: 
        return ['Programme', [4,3,4,5,6,7]]
    #forcing
    elif type == 2:
        return {
            0 : ['Forcage : Éclairage',[4,3,7,7]],
            1 : ['Forcage : Message réalisé',[4,3]],
            2 : ['Forcage : Message Ligne de viE', [4,3]], 
            3 : ['Forcage : Message Configuration générale', [4,3]], 
            4 : ['Forcage : Message Configuration programme', [4,3,1,2,3]], 
            5 : ['Forcage : RAZ cumul', [4,3,1,1,1,1]],             
            6 : ['Forcage : Reset de la carte', [4,3,8,8,8,8,8]], 
            7 : ['Forcage : Non utilisé', []], 
        }[second_type]
    #Acknowledge
    elif type == 3:
        return ['Acknowledge',[]]
    #Realized
    elif type == 4:
        return ['Realized',[]]
    #configuration
    elif type == 5: 
        return {
            0 : ['Configuration : date', [4,4,7,4,5,5,6,8]], #[4, 4, 'date' ([7,4,5]), 'hour' ([5,6]), 8]
            1 : ['Configuration : ephemeris', [4,4,7], "mama,baba,ana"],
            2 : ['Configuration : position', [4,4,25,26]],
            3 : ['Configuration : Ack' , [4,4,1,1,8]],
            4 : ['Configuration : min_button_priority', [4,4,7]],
            5 : ['Configuration : lamp_type', [4,4,5]],
            6 : ['Configuration : lamp_power', [4,4,10]], 
            7 : ['Configuration : realized_hour', [4,4,5,6]], #[4,4,'hour']
            8 : ['Configuration : realized_freq_daily', [4,4,1,7]], 
            9 : ['Configuration : realized_freq_minute', [4,4,5,6]], #[4,4,'hour']
            10 : ['Configuration : lifeline_freq_daily' , [4,4,1,7]],
            11 : ['Configuration : lifeline_hour', [4,4,5,6]], #[4,4,'hour']
            12 : ['Configuration : lifeline_freq', [4,4,5,6]],
        }[second_type]
    #Protocole LoRaWan
    elif type == 14: 
        return {
            0 : ['LoRaWan : Ack_downlink', [4,4,8,8,8,8,8]],
            1 : ['LoRaWan : Pass_to_classeC', [4,4,8,8,8,8,8,8,8,8,8]]
        }[second_type]
    #Uplink
    elif type == 15: 
        return {
            1 : ['Uplink : Life_line', [4,4,6,4,6,7,4,5,5,6,7,4,5,5,6,7,4,5,5,6,7,4,5,5,6,7,4,5,5,6,7,4,5,5,6,2,8,1]],
            3 : ['Uplink : Realized',[4,4,6,4,6,7,4,5,5,6,7,4,11,2,7,4,5,5,6,7,4,11,2,1,2,1,8,7,16,16,16,16]],
            4 : ['Uplink : Acquitement : Programme journalier',[4,4,4,1,7,4,5,5,6,5,6,5,11,5]],
            5 : ['Uplink : Acquitement : Programme hebdomadaire',[4,4,4,1,6,8,16,8]],
            6 : ['Uplink : general_configuration', [4,4,4,25,26,7,7,5,10,1,5,6,7,11,1,5,6,7,11,1,1]], 
            7 : ['Uplink : Programme', [4,4,4,2,3,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7,5,6,7]]
        }[second_type]
    else:
        return 'Erreur'
