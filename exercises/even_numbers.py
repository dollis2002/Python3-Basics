"""
Print all even numbers lesser that the number given by the user
"""
#%% Using for loop
last = int(input('Insert last number: '))

for i in range(0, last+1):
    if i%2 == 0:
        print(i)

#%% Using while loop
start = 0
last = int(input('Insert last number: '))

while start <= last:
    if start%2 == 0:
        print(start)
    start += 1

#%% One liner
print([i for i in range(0,int(input('Final number >>>'))+1) if i%2 == 0])