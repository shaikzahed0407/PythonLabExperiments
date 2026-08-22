#Fibonacci Series
def fibonacci_series(N):
    """Generate Fibonacci sreis up to N terms"""
    series=[]
    a,b=0,1
    for _ in range(N):
        series.append(a)
        a,b=b,a+b
    return series
def main():
    N=int(input("Enter the number of terms:"))
    if N<=0:
        print("Enter a positve integer grater than zero")
    else:
        print(fibonacci_series(N))
main()                