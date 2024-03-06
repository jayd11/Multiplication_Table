user=input("Enter your Name: ")
print(f"Hello {user}! Welcome to Mulitplilcation table")
multiplier=input("Enter your multiplier: ")

start,end=input("Enter Multiplicand start,end : ").split(",")
start=int(start)
end=int(end)
print(f"printing multiplication table for {multiplier} from {start} to {end}")

for i in range(start,end+1):
	product=int(multiplier)*i
	print(f"{i}X{multiplier}={product}")

print(f"Thank you {user}!")
