#Repeat
# for infection round in range(1,6)
# infected individuals= n*r**i
# if the generation is less than 5:keep infecting
# if 5:done

n=84
r=1.2
for i in range(1,6):
 n=n*r
 print("In round ", i,", ","there is ",n," infected individuals.")

