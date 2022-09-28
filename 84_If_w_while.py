cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
print("The cargo list is:", cargo)

boxCapacity = 90
box = []
i = 0


while sum(box) + cargo[i] < boxCapacity and i < len(cargo):
    box.append(cargo[i])
    i += 1

print("The collected items sum is:",sum(box))
print("The elements are:",box)