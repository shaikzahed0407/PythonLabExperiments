class Complex: 
    def __init__(self, real=0.0, imag=0.0): 
        self.real = real 
        self.imag = imag 
 
    def __str__(self): 
        if self.imag >= 0: 
            return f"{self.real} + {self.imag}i" 
        return f"{self.real} - {abs(self.imag)}i" 
 
 
def add_two_complex(c1, c2): 
   
    sum_real = c1.real + c2.real 
    sum_imag = c1.imag + c2.imag 
    return Complex(sum_real, sum_imag) 
 
 
def main(): 
    print("--- Complex Number Addition Program ---") 
    try: 
        n = int(input("Enter the number of complex numbers to add (N >= 2): ")) 
        if n < 2: 
            print("Please enter a number greater than or equal to 2.") 
            exit()
    except ValueError: 
        print("Invalid input. Please enter an integer.") 
    complex_numbers = [] 
    for i in range(n): 
        print(f"\nEnter complex number {i + 1}:") 
        while True: 
            try: 
                real = float(input("  Enter Real part: ")) 
                imag = float(input("  Enter Imaginary part: ")) 
                complex_numbers.append(Complex(real, imag)) 
                break 
            except ValueError: 
                print("  Invalid input! Please enter numeric values for real and imaginary parts.") 
    total_sum = complex_numbers[0] 
    for i in range(1, n): 
        total_sum = add_two_complex(total_sum, complex_numbers[i]) 
    print("\n--- Results ---") 
    print("Entered Complex Numbers:") 
    for c in complex_numbers: 
        print(f"  {c}")      
    print(f"\nFinal Sum of all {n} complex numbers:") 
    print(f"  {total_sum}") 
if __name__ == "__main__": 
    main() 