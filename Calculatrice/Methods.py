from math import *


class methods :

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    #Calculs simples

    def addition():
        var1 = int(input("Choissez votre 1ere valeur"))
        var2 = int(input("Choissez votre 2nde valeur"))
        result = (var1 + var2)
        print(f"voici votre résultat : {result}")
    def soustraction():
        var1 = int(input("Choissez votre 1ere valeur"))
        var2 = int(input("Choissez votre 2nde valeur"))
        result = (var1 - var2)
        print(f"voici votre résultat : {result}")
    def division():
        var1 = int(input("Choissez votre 1ere valeur"))
        var2 = int(input("Choissez votre 2nde valeur"))
        result = (var1 / var2)
        print(f"voici votre résultat : {result}")

    #Calculs avancés

    def puissances():
        var2 = int(input("Choissez votre 2nde valeur"))
        var1 = int(input("Choissez votre 1ere valeur"))
        result = (var1 ** var2)
        print(f"voici votre résultat : {result}")

    #à faire
    def pytagore():
        var2 = int(input("Choissez votre 2nde valeur"))
        var1 = int(input("Choissez votre 1ere valeur"))
        resprt1 = ((var1 ** var1) + (var2 ** var2))
        resprt2 = math.sqrt(resprt1)
        print(f"voici votre résultat : {resprt2}")
