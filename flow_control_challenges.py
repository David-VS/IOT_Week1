####################
## easy challenge ##
####################

print("ggd")
a = int(input("geef getal 1:"))
b = int(input("geef getal 2:"))
ggd = 1

#option 1
for i in range (1, a):
    if a % i == 0 and b % i == 0:
        ggd = i
print("classic: " + str(ggd))

#option 2
while a != 0:
    temp = a
    a = b % a
    b = temp
print("euclidean: " + str(b))



########################
## hardcore challenge ##
########################
print("opdelen 152")
to_divide = int(input("geef een getal:"))

counter = 1
temp = 0

while counter < to_divide:
    counter *= 10
    temp = to_divide % counter
    print(str(counter/10)+" talen " + str (int(temp // (counter/10))))
