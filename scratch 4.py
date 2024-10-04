listt = list(range(1,100))
print(list)



def generators (list = listt, adjacent_digit = 1): 
    for i in range(len(list) - adjacent_digit +1): 
        digits = listt[i:i +adjacent_digit] 
        print(digits)
   
generators()


def generator(list = listt, adjacent_digit = 1): 
    for i in range(len(list) - adjacent_digit + 1): 
        digits = listt[i:i + adjacent_digit]
        for digit in digits: 
            sum = listt[i] + digit
        return sum

generator ()