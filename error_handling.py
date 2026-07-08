# Error handling in Python -try/except is Python's version of try/catch in C++

# Basic example
try:
    number = int(input("Enter a number:"))
    result = 100 / number
    print(f"100 divided by {number} is {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This always runs, no matter what.")

    # Why this matter in ML:
    # When loading datasets, files might be missing
    # When pasring data, values might be wrong types
    # Your training pipeline should never crash from bad data



        # You can also raise your own errors
    def validate_age(age):
            if age < 0:
                raise ValueError(f"Age cannot be negative, got {age}")
            if age > 150:
                raise ValueError(f"Age {age} is not realistic.")
            return f"Valid age: {age}"
    
    try:
        print(validate_age(19))
        print(validate_age(-5))
    except ValueError as e:
        print(f"Validation error: {e}")