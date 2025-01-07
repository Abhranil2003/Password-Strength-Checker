import re

def check_password_strength(password):
    """
    Analyzes the strength of a password and provides feedback for improvement.
    
    Parameters:
        password (str): The password to analyze.
        
    Returns:
        tuple: A boolean indicating if the password is strong, and a list of feedback messages.
    """
    feedback = []
    is_strong = True

    # Define criteria
    min_length = 8
    if len(password) < min_length:
        is_strong = False
        feedback.append(f"Password should be at least {min_length} characters long.")

    if not re.search(r'[A-Z]', password):
        is_strong = False
        feedback.append("Password should include at least one uppercase letter.")

    if not re.search(r'[a-z]', password):
        is_strong = False
        feedback.append("Password should include at least one lowercase letter.")

    if not re.search(r'\d', password):
        is_strong = False
        feedback.append("Password should include at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        is_strong = False
        feedback.append("Password should include at least one special character (e.g., @, #, $).")

    if re.search(r'\s', password):
        is_strong = False
        feedback.append("Password should not contain spaces.")

    # Check for common patterns or weaknesses (e.g., repetitive characters)
    if len(set(password)) < len(password) // 2:
        is_strong = False
        feedback.append("Password has too many repetitive characters; try adding more variety.")

    # Add more custom checks if needed

    return is_strong, feedback


def main():
    """
    Main function to interact with the user for password analysis.
    """
    print("Welcome to the Password Strength Checker!")
    print("Enter a password to analyze its strength or type 'exit' to quit.")

    while True:
        # Take user input
        user_input = input("\nEnter your password: ").strip()

        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye! Stay safe online!")
            break

        # Analyze password strength
        strong, suggestions = check_password_strength(user_input)

        # Provide feedback to the user
        if strong:
            print("✅ Your password is strong!")
        else:
            print("❌ Your password is weak. Here are some suggestions to improve it:")
            for suggestion in suggestions:
                print(f"- {suggestion}")


# Entry point
if __name__ == "__main__":
    main()
