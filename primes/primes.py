def primes(limit):
    for number in range(0,limit+1):
        if number > 1:
            for num in range(2,number):
                if (number % num) == 0:
                    break
            else:
                print(number)

primes(10)