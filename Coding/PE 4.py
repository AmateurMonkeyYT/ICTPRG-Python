d = 0

for a in range (100,999):

    for b in range (100,999):

        c = a * b
        if (str(c) == str(c)[::-1]) and (c > d):

            d = int(c)
            print(d)



    