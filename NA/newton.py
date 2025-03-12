
x = 100000
for i in range(10):
    print(f"{i}th iteration  =>  {x}")
    x = x - (x**2) / (2*x)
