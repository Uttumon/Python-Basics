# Simple function to print multiplication table
def multiplication_table():
    for i in range(2, 21):
        print(f"\nMultiplication table of {i}\n")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")

# Call the function
multiplication_table()
