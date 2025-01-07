import re

def check_password_strength(password, user_name="YourName"):
    """
    Analyzes the strength of a password and provides feedback for improvement.
    
    Parameters:
        password (str): The password to analyze.
        user_name (str): The user's name to check for in the password (default is "YourName").
        
    Returns:
        tuple: A boolean indicating if the password is strong, and a list of feedback messages.
    """
    feedback = []
    is_strong = True

    # Define criteria
    min_length = 16
    if len(password) < min_length:
        is_strong = False
        feedback.append("Password should be at least 16 characters long.")

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

    # Custom Checks
    if has_sequential_chars(password):
        is_strong = False
        feedback.append("Password should not contain sequential characters (e.g., '123', 'abc').")

    if has_repeated_characters(password):
        is_strong = False
        feedback.append("Password should not contain excessive repeated characters (e.g., 'aaa', '111').")

    if contains_dictionary_word(password):
        is_strong = False
        feedback.append("Password should not contain common dictionary words (e.g., 'password', 'admin').")

    if has_similar_characters(password):
        is_strong = False
        feedback.append("Password should avoid visually similar characters (e.g., 'I', 'l', '1').")

    if contains_user_name(password, user_name):
        is_strong = False
        feedback.append(f"Password should not contain your name: {user_name}.")

    return is_strong, feedback


# Custom check functions

def has_sequential_chars(password):
    """Check for sequential characters."""
    patterns = ['123', '234', '345', 'abc', 'abcd', 'qwerty']
    for pattern in patterns:
        if pattern in password.lower():
            return True
    return False

def has_repeated_characters(password):
    """Check for excessive repeated characters."""
    return any(password.count(char) > 2 for char in password)

def contains_dictionary_word(password):
    """Check if password contains any dictionary words."""
    dictionary_words = ["password", "admin", "123456", "letmein", "qwerty", "welcome", "password123"]
    for word in dictionary_words:
        if word in password.lower():
            return True
    return False

def has_similar_characters(password):
    """Check for visually similar characters in the password."""
    similar_chars = ['I', 'l', '1', 'O', '0', 'Q', 'O']
    return any(char in similar_chars for char in password)

def contains_user_name(password, user_name):
    """Check if password contains the user's name."""
    return user_name.lower() in password.lower()


def main():
    """
    Main function to interact with the user for password analysis.
    """
    print("Welcome to the Password Strength Checker!")
    print("Enter a password with minimum length of 16 to analyze its strength or type 'exit' to quit.")

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
            print("1. Password should be at least 16 characters long.")
            print("2. Password should include at least one uppercase and one lowercase letter.")
            print("3. Password should include at least one digit.")
            print("4. Password should include at least one special character (e.g., @, #, $).")


# Entry point
if __name__ == "__main__":
    main()
