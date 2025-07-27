
pid=[""]*5
pname=[""]*5
prices = [0]*5
qtys=[0]*5
totals=[0]*5

for i in range(5):
    print("Enter details for products:", i+1)

    pid[i]=input("enter product id:")
    pname[i]=input("Enter product name:")

    price=input("Enter price ")
    qty=input("enter qty ")

    prices[i] = int(price)
    qtys[i] = int(qty)

    totals[i] = prices[i] * qtys[i]

total_amount=0
for i in range(5):
    total_amount=total_amount+totals[i]

if total_amount > 10000:
    discount_rate=0.20

elif total_amount > 1000:
    discount_rate=0.10
else:
    discount_rate=0.0

discount_amount = total_amount*discount_rate
final_amount=total_amount - discount_amount

print("-------------------Final BILL--------------")
print("PID\tPName\tPrice\tQty\tTotal")
print("-------------------------------------------")


for i in range(5):
    print(pid[i], "\t", pname[i], "\t", prices[i], "\t", qtys[i], "\t", totals[i])

print("-------------------------------------------")
print("total amount:", total_amount)
print("Discount applied: ", discount_amount)
print("Final amount: ", final_amount)
print("-------------------------------------------")














    
