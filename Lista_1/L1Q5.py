def palindromo (str):
    def inverter(palavra):
        return palavra[::-1]
    
    str1 = str
    
    str2 = inverter(str)
    
    if str1 == str2:
        print ("é palíndromo")
    
    else:
        print ("não é palíndromo")




    



