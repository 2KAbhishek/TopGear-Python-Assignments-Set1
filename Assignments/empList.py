empNames = ['Ab', 'Hi', 'Sh', 'Ek', 'Ku', 'Ma', 'Rk', 'Es', 'Hr', 'I']
empId = [68, 20, 12, 17, 10, 21, 19, 55, 62, 98]

print(empNames)

print(empNames[int(input('Enter index: '))])

print(empNames[3:9])

print(empNames[2:])

print(empNames * int(input('Repeat count: ')))

for i in range(len(empNames)):
    print(empNames[i] + ':' + str(empId[i]))
