# list: append, remove, in

# loop, sum & range
""" total = 0
expenses = []

for x in range(3):
    expenses.append(float(input("Enter your expense:")))

total = sum(expenses)
print("finally you spent $", total, sep = '', end = "\n\nFuck, it's again too much") """

# loan
owed = float(input("How much do you owe?\n")) # $50,000
percentage_rate = float(input("What is your annual percentage?\n"))/100/12 # 3%
payment = float(input("How much will you pay?\n")) # $1,000
months = int(input("How many monts?\n")) # 12

total_interset_paid = 0

for i in range(months):
    interest = owed * percentage_rate
    total_interset_paid = total_interset_paid + interest
    owed = owed + interest

    if (owed - payment < 0):
        print("Its ok you payed everything in ", i+1, " months")
        print("total_interset_paid", total_interset_paid)
        break

    owed = owed - payment

    print("Paid", payment, "of which", interest, "was interest")
    print("Owed", owed)