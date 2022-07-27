#Print the following pattern using nested loop.
#     *
#    ***
#   *****
#    ***
#     *

for i in range(3):
    for k in range(2-i):
        print("   ",end='')
    for j in range((2*i)+1):
        print(" * ", end='')
    print()
for a in range(2):
    for b in range(a+1):
        print("   ",end='')
    for c in range(2 * (1-a) + 1):
        print(" * ", end='')
    print("")