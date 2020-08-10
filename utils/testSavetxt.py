
twoArray = [["sadasd", "sadasd"], ["asdsad", "asdsad"]]


with open("file.txt", 'w') as output:
    for row in twoArray:
        for j, element in enumerate(row):
            if j < len(row)-1:
                output.write(element + " ")
            else:
                output.write(element)

        output.write('\n')
