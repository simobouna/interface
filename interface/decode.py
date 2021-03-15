from .config import get_next_bits, get_type


class Decode:
    def __init__(self, hex):
        #Nombre de bits
        self.bits = len(hex) * 4 
        #Conversion en binaire
        self.binary = bin(int(hex, 16))[2:].zfill(self.bits)


    def decode(self):
        index = 0
        list = []
        while (self.bits - index > 7):
            #Recuperer la valeur des premiers 4 bits (type) 
            first = int(self.binary[index:4+index], 2)
            if first == 0 : return list
            #Recuperer la valeur du second type
            second = int(self.binary[4+index:4 + index + get_next_bits()[first]], 2)
            #identifier le type du message
            type = get_type(first, second)
            decimals = []
            for b in type[1]:
                #Traiter le cas de la position GPS (Valeurs negatives)
                if b == 25 or b == 26 :
                    if self.binary[index:index + 1] == '1':
                        neg_value = self.binary[index + 1:index + b].replace('1', '2').replace('0', '1').replace('2', '0')
                        neg_value = int(neg_value, 2) + 1
                        decimals.append(-neg_value)
                        index += b
                        continue
                decimals.append(int(self.binary[index:index + b], 2))
                index += b
            list.append(decimals)
        return list

