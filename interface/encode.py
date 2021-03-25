from .config import get_type


class Encode:
    def __init__(self, data):
        self.get_bin = lambda x, n: format(x, 'b').zfill(n)
        self.get_neg_bin = lambda x, n: '1' + format(-x-1, 'b').zfill(n-1).replace('1', '2').replace('0', '1').replace('2', '0')
        self.get_hex = lambda x: format(int(x , 2), 'x')
        self.bits_count = 0
        self.encoded = ''
        self.data = data


    def encode_in_binary(self, data=None):
        used_data = data if data is not None else self.data
        nbr_messages = len(used_data)
        for i in range(nbr_messages):
            type = get_type(used_data[i][0], used_data[i][1])
            for j in range(len(type[1])):
                #Traiter les valeurs negatives
                if(used_data[i][j] < 0):
                    self.encoded += self.get_neg_bin(used_data[i][j], type[1][j])
                    self.bits_count += type[1][j]
                    continue
                self.encoded += self.get_bin(used_data[i][j], type[1][j])
                self.bits_count += type[1][j]
        return self.encoded

    def bytes_completion(self, binary):
        count = self.bits_count
        if (count % 8) != 0:
            while count % 8 != 0:
                binary += '0'
                count += 1
        return self.get_hex(binary)
        
    def encode(self, data=None):
        return self.bytes_completion(self.encode_in_binary(data))

