def primes(limit):
    result = 0
    for number in range(0,limit+1):
        if number > 1:
            for num in range(2,number):
                if (number % num) == 0:
                    break
            else:
                result += number
    print(result)

primes(10)