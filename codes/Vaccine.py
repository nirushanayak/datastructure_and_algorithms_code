import sys


class Vaccines:
    def __init__(self, Rna):
        self.rna = self.count_letter(Rna)
        self.vacc = []
        self.count = 0
        self.maximum = 0
        self.i = 0

    def Vaccine_find(self, Str):
        st = self.count_letter(Str)
        t1 = max(self.rna['G'], st['C'])
        if t1 == sys.maxsize:
            t1 = 0
        t2 = max(self.rna['C'], st['G'])
        if t2 == sys.maxsize:
            t2 = 0
        self.vacc.append(t1 + t2)
        if self.vacc[self.count] >= self.maximum:
            self.maximum = self.vacc[self.count]
            self.i = len(self.vacc)
        self.count = self.count + 1

    def count_letter(self, word):
        words = {}
        words['G'] = word.count('G')
        words['C'] = word.count('C')
        if words['G'] == 0:
            words['G'] = sys.maxsize
        if words['C'] == 0:
            words['C'] = sys.maxsize
        return words

    # Write your code here


V=Vaccines('ACGGU')
V.Vaccine_find('AAAA')
print(V.maximum)

# n=int(input())
# length=int(input())
# Rna=input()
# V=Vaccines(Rna)
# for i in range(n):
#     l=int(input())
#     string1=input()
#     V.Vaccine_find(string1)
# print(V.i)
