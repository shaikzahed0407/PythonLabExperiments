def DivExp(a, b):
    assert a > 0, "Assertion Error: a must be greater than 0"
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    c=a/b
    return c
def main():
    try:
        a = float(input("Enter value of a: "))
        b = float(input("Enter value of b: "))

        result = DivExp(a, b)

        print("Result =", result)

    except ValueError:
        print("Enter Numerical Values for a and b")

    except (AssertionError,ZeroDivisionError) as e:
        print(e)

if __name__=='__main__':
    main()