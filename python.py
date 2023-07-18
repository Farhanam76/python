books = {'John Green':'Paper towns', 'Harper lee':'To kill a mockingbird', 'Louisa may alcott':'Little women'}

authorname = str(input('Enter the authors full name: " "'))

print("".join(books[authorname]))

#elif and if exercise 
mark = int(input('enter your mark'))

if mark > 85:
    print('distinction')
elif mark == 85:
    print('pass')
elif mark >= 65:
    print('pass')
else:
    print('fail')

#without elif 
mark = int(input('enter your mark'))

if mark > 85:
    print('distinction')
if mark == 85:
    print('pass')
if mark >= 65 and mark < 85:
    print('pass')
if mark < 65:
    print('fail')

 




# while loop exercise 
count = 1

while count <= 5:
    name = str(input("what is your name? "))
    print(name,"is awesome!")
    count += 1
for i in range(10, 21, 2):
    print(i)
#practice 
1) numbers = []
for num in range(1500-2700):
    if (num%7==0) and (num%5==0):
        numbers.append(str(num))
        print (','.join(numbers))






