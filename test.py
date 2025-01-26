import random

# Generate a list of random numbers
numbers = [random.randint(1, 100) for _ in range(10)]

# Create a simple function to process the numbers
def process_numbers(num_list):
    total = sum(num_list)
    average = total / len(num_list)
    return total, average

# Generate a random string
letters = 'abcdefghijklmnopqrstuvwxyz'
random_string = ''.join(random.choice(letters) for _ in range(8))

# Main execution
if __name__ == "__main__":
    total, avg = process_numbers(numbers)
    print(f"Random numbers: {numbers}")
    print(f"Total: {total}, Average: {avg:.2f}")
    print(f"Random string: {random_string}")