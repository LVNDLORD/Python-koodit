# thislist = [["apple", 1], ["banana", 1], ["cherry", 1]]
# thislist2 = [["kiwi", 1], ["cherry", 1], ["grape", 1]]
#
# final = thislist + thislist2

# print(final)
# for name, num in final:
#	while num < 10:
#  		print(name, num)
#  		num += 1



# while count < 10:

fin = [['ABC-1', 115], ['ABC-2', 176], ['ABC-3', 118],
         ['ABC-4', 129], ['ABC-5', 124], ['ABC-6', 143],
         ['ABC-7', 144], ['ABC-8', 170], ['ABC-9', 116],
         ['ABC-10', 116]]

final = [['ABC-1', 195], ['ABC-2', 197]]

for name, num in final:
    while num != 200:
        count = 0
        for name, num in final:
            print(name, num)
            loop_list = []
            num = num + 1
            # print(str(name), str(num) + ' after count')
            loop_list.append(name)
            loop_list.append(num)
            final.pop(count)
            final.insert(count, loop_list)
            count = count + 1
            if count == 9 or num == 200:  # count 9 for 10 objects, num as 10k
                                            # add other properties of each object
                break
        else:
            print(final + 'inside loop')

print(final)
