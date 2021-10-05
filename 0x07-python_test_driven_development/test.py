char = "Calomni vacius irementa de . la guarda espanyol"
line_i = ['.',':', '?']
length = len(char)
for i in range(length) :
    if char[i] in line_i:
        print(char[i], end='')
        if (char[i + 1]) == " ":
            print("", end="")
        print("")
    elif char[i] ==" ":
        print("", end=" ")
    else:
        print(char[i], end="")
