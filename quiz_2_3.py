def primesInList(int_list):
    prime_list = []
    for i in int_list:
        factor_num = 0
        for j in range(2, (int(i / 2))+1):
            if i % j == 0:  # finds factors
                factor_num += 1
        if factor_num == 0 and i > 1 and i not in prime_list:
            '''
            detects if a prime number has been found
            since we started dividing our integer by every int > 1 up to its half, any legible int should have exactly
            zero factors found
            
            i > 1 is to exclude 1 which is neither prime nor composite
            i not in prime_list is for preventing duplicates
            '''
            prime_list.append(i)

    return prime_list

test_list = list(range(1, 100))
test_list.append(2)
# print(test_list)
print(primesInList(test_list))
