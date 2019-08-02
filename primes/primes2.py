number=10
if number > 1:
    for num in range(2,number):
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num," ")
else:
   print("Belirtilen sayidan kucuk asal sayi yoktur")