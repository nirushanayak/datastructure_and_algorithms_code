def waiter(count, A, q, final_list):
    A1 = []
    B1=[]
    Q = prime_n(count)

    if count == q + 1:
        return B1
    if len(A) == 0:
        return B1
    while (len(A) != 0):
        ele = A.pop()
        if ele % Q == 0:
            B1.append(ele)
        else:
            A1.append(ele)
    count = count + 1
    return final_list+waiter(count, A1, q, final_list)




def prime_n(n):
    # initial prime number list
    prime_list = [2]
    num=3
    # first number to test if prime
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list[-1]


l=waiter(1,[3,3,4,4,9],2,[])
type(l)
