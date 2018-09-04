n= int(input("Enter the length of the sequence: "))

tala1 = 1
print(tala1)
tala2 = 2
print(tala2)
tala3 = 3
print(tala3)
num_now = 0
counter = 0

while counter < n-3:
    num_now = tala3 + tala2 +tala1
    print(num_now)
    tala1 = tala2
    tala2 = tala3
    tala3 = num_now
    counter += 1