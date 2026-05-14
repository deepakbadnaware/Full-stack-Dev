def countdown(n):
    # Base case - when to stop
    if n == 0:
        print("Blastoff!")
        return
    
    # Recursive case - function calls itself
    
    countdown(n - 1)
    print(n)  # Smaller problem

countdown(3)
# Output: 3, 2, 1, Blastoff!