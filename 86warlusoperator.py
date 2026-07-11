# =========================================================================
# DEMO 1: WALRUS OPERATOR WITH LIST POP
# =========================================================================
numbers = [1, 2, 3, 4, 5]

# JADU 1: (n := len(numbers)) ne do kaam ek sath kiye!
# 1. len(numbers) nikal kar 'n' variable mein save kiya.
# 2. Aur sath hi check kiya ki kya 'n > 0' hai ya nahi.
while (n := len(numbers)) > 0:
    # pop() list ke aakhri item ko nikal kar bahar phenk deta hai
    print(numbers.pop())

print("-" * 50)


# =========================================================================
# DEMO 2: PURANA TARIKA (Bina Walrus Operator ke Loop chalana)
# =========================================================================
foods= list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break  # Loop todne ke liye alag se 2 lines likhni padi
    foods.append(food)

print(foods)
print("-" * 50)


# =========================================================================
# DEMO 3: NAYA TARIKA (Walrus Operator ke sath Lines ki bachat)
# =========================================================================
foods = list()

# JADU 2: Ek hi jhatke mein user se input liya, use 'food' variable mein daala,
# aur turant check bhi kar liya ki kahin woh "quit" toh nahi hai!
while (food := input("[Walrus Way] What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)
