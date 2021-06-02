while True:
    UID = []
    data = str(input("Enter first name: ")).lower()
    if data == "":
        exit("Closing Program.")
    else:
        UID.append(data)
        data = str(input("Enter last name: ")).lower()
        if data == "":
            print("Invalid input.")
            continue
        else:
            UID.append(data)
            data = input("Enter age: ")
            if data == "":
                print("Invalid input.")
                continue
            else:
                data = 2021-(int(data)+5)
                UID.append(str(data))
                print(UID[0][0] + UID[1] + "@Huawow.io | " + UID[0] + UID[1][0].upper() + "_" + UID[2])



            


