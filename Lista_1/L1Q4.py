def is_prime (n):
    for i in range (n):
        resto = n % (i+2)
        
        if n == 2:
            return True
            print("True")
        
        elif resto == 0:
            return False
            print("False")
        
        else:   
            return True
            print("True")







