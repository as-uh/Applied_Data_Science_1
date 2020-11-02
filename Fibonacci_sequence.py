"""
fibonacci function will take input for the number 
of terms as nterms. 
It will print user input number of terms of 
fibonacci sequence."""

def fibonacci(nterms):
    # First and second term of the fibonacci Sequence
    term0=1
    term1=1
    
    # Check if there is any term in the sequence
    if nterms < 1:
        print("Squence have no terms")
    else:
        print(f"First %i terms of Fibonacci sequence are:" 
            %nterms)
        for i in range(nterms):
            print(term0)
            nth_term = term0+term1
            # Update values of the terms
            term0 = term1
            term1 = nth_term

#test values
fibonacci(5)
fibonacci(10)