def check(arrDugOut, direct, lgth):
    final = []
    error = []
    curr = arrDugOut[len(arrDugOut)-1]
    loc = 0
    for x in range(lgth + 1):
        if direct == 'L':
            final = [curr[0] - x, curr[1]] 
            if final in arrDugOut and final != curr:
                error = final
                loc = arrDugOut.index(final)
        elif direct == 'R':
            final = [curr[0] + x, curr[1]]
            if final in arrDugOut and final != curr:
                error = final
                loc = arrDugOut.index(final)
        elif direct == 'D':
            final = [curr[0], curr[1] - x]
            if final in arrDugOut and final != curr:
                error = final
                loc = arrDugOut.index(final)
        elif direct == 'U':
            final = [curr[0], curr[1] + x]
            if final in arrDugOut and final != curr:
                error = final
                loc = arrDugOut.index(final)
        else:
            print("That is not an option")
    
    return error, final, loc

commands = [['R', 2], ['D', 10], ['R', 4]]
dugOut = [[0,-1], [0,-2], [0,-3], [1,-3], [2,-3], [3,-3], [3,-4], [3,-5], [4,-5], [5,-5], [5,-4], [5,-3], [6,-3], [7,-3], [7,-4], [7,-5], [7,-6], [7,-7], [6,-7], [5,-7], [4,-7], [3,-7], [2,-7], [1,-7], [0,-7], [-1,-7], [-1,-6], [-1,-5]]

while True:
    # userDirection = input("Direction (L for left, R for right, D for down, U for up): ").capitalize()
    # userLength = int(input("Length: "))
    for x in commands:
        if x[0] == 'Q':
            print("Thank you for playing")
            quit()
        else:
            error, final, loc = check(dugOut, x[0], x[1])
            if final[0] >= -200 and final[0] <= 200 and final[1] >= -201 and final[1] <= 201:
                if error != []:
                    # Checking if it worked
                    # print("{} {}".format(dugOut[loc], loc))
                    print("{} {} DANGER".format(final[0], final[1]))
                    quit()
                else:
                    dugOut.append(final)
                    print("{} {} safe".format(final[0], final[1]))
            else:
                print("Out of bounds")
                quit()
