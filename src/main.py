# This is our first Python program for the AI Agency platform
# It will help us verify our setup and demonstrate basic concepts

def greet_user():
    """
    This function asks for a user's name and greets them.
    It demonstrates basic input/output and string formatting.
    """
    print("Welcome to AI Agency Platform")
    print("-" * 30)  # This creates a line of 30 dashes for visual separation
    
    # Get user input
    name = input("Please enter your name: ")
    
    # Create a personalized greeting
    greeting = f"Hello {name}! Your development environment is set up correctly."
    
    # Display the greeting
    print("\n" + greeting)
    print("\nReady to start building your AI Agency platform!")

# This special if statement tells Python to run our function when the program starts
if __name__ == "__main__":
    greet_user()