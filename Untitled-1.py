import math as m
import collections as coll

def SummBin(a, l):
    num = ''
    for i in range(0,l):
        a *= 2.0
        num += str(m.trunc(a))
        if a >= 1.0:
            a -= 1.0
    return num

class Coder:
    text = ''
    code = ''
    new_word = {}
    deword = {}
    def Coder(self):          
        sum = 0.0
        for i in self.text:
            if i not in self.new_word:
                self.new_word[i.lower()] = [1, 0, 0, '']
            else:
                self.new_word[i][0] += 1
        self.new_word = coll.OrderedDict(sorted(self.new_word.items(),key = lambda i:i[0]))
        for i in self.new_word:
            self.new_word[i][0] /=  len(self.text)
            self.new_word[i][1] = m.ceil(m.log2(1 / self.new_word[i][0])) + 1
            self.new_word[i][2] = self.new_word[i][0] / 2 + sum
            self.new_word[i][3] = SummBin(self.new_word[i][2], self.new_word[i][1])
            sum += self.new_word[i][0]
        for i in self.text.lower():
            self.code += self.new_word[i][3]
        print(self.code)
    def Decoder(self):
        for k, i in self.new_word.items():
            self.deword[i[3]] = k 
        w = ''
        for i in self.code:
            try:
                w += i
                print(self.deword[w], end='')
                w = ''
            except:
                pass
            

cod = Coder()
cod.text = input()
cod.Coder()
cod.Decoder()
s = 0.0
H = 0.0
for i in cod.text.lower():
    s += cod.new_word[i][0] * cod.new_word[i][1]
    H += cod.new_word[i][0] * m.log2(1 / cod.new_word[i][0])
print('\n', s, sep='')
print(H + 2)