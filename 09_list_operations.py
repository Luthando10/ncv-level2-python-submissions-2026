marks = []
i = 0

mark = int(input('Enter mark(or -1 to stop)'))
while mark != -1:
    marks.append(mark)
    mark = int(input('Enter mark(or -1 to stop)'))
    
print(f'Our list has {len(marks)} elements')

for x in range(len(marks)):
    print(marks[x])
    mark = int(input('Enter mark(or -1 to stop)'))

##The of all marks
sum = 0
for x in range (len()):
    mark = marks[x]
    sum = sum + mark
print(f'The sum of all marks = {sum}')

##The average of all marks
total = 0
for x in range (len()):
    mark = marks[x]
    total = total + mark
print(f'The sum of all marks = {sum}')

avg = total / len(marks)
print(f'The average of all marks = {avg}')

