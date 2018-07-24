sum = 0.0
while True:	
    number = input("Enter Integer or Float Here :")
    if number == '':
        break
    try:
        sum += float(number)
    except ValueError: 
        continue		
print("Total : ", sum)

