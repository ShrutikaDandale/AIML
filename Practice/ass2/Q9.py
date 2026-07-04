def prime(n):
     n > 2

     if n < 2:
          return False
     
     for i in range(2, n):
          if i % n == 0:
               return False
          
     return True
    
print(prime(8))