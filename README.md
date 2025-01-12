# Password Strength Checker
**Author:** Abhranil Poddar

A Python-based tool to analyze the strength of passwords and provide actionable feedback for improvement. It checks passwords against various criteria to ensure they are secure and hard to guess. Also generates passwords as per users' choice.

---

## 🚀 Features

- Validates password strength based on:
  - Minimum length
  - Uppercase, lowercase letters
  - Digits and special characters
  - Absence of spaces
  - Variety in characters (avoids repetitive patterns)
- Provides detailed feedback for weak passwords.
- Interactive command-line interface (CLI).
- Unit-tested for reliability.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PasswordStrengthChecker.git
   cd PasswordStrengthChecker
   ```

2. Ensure you have Python 3 installed. Run the following to check:
   ```bash
   python --version
   ```

3. Install any required dependencies (none needed for basic functionality):
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ Usage

1. Run the password checker:
   ```bash
   python password_checker.py
   ```

2. Follow the prompts to enter a password. The tool will analyze the password and provide feedback on its strength.

3. To exit the tool, type `exit`.

Example interaction:
```
Welcome to the Password Strength Checker!
Enter a password with minimum length of 16 to analyze its strength or type 'exit' to quit.

Enter your password: weakpass
❌ Your password is weak. Here are some suggestions to improve it:
- Password should be at least 16 characters long.
- Password should include at least one uppercase letter.
- Password should include at least one special character (e.g., @, #, $).

Would you like the program to generate a strong password for you? (yes/no): yes
Enter the desired length of the password (must be 16 or greater): 20
A strong password has been generated. Please copy it from the program output.
@Gt8!FbnF$2kLm&9qJ4z
```

---

## 🧪 Testing

Unit tests are included to validate the functionality of the password checker.

1. Run the tests using:
   ```bash
   python -m unittest test_password_checker.py
   ```

2. All tests should pass if the implementation is correct.

---

## 🗂 Project Structure

```
PasswordStrengthChecker/
│
├── password_checker.py       # Core password strength checking functionality
├── test_password_checker.py  # Unit tests for the password checker
├── requirements.txt          # Dependencies
├── LICENSE                   # License for the project
└── README.md                 # Project documentation
```

---

## 📈 Future Enhancements

- Check passwords against a blacklist of common passwords.
- Add entropy calculation for more accurate strength evaluation.
- Provide a GUI or web-based interface.
- Integrate with external applications via APIs.

---

## 🐜 License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request with a detailed description of changes.

---

## 💬 Feedback

We welcome your feedback! If you encounter any issues or have suggestions for improvement, feel free to open an issue or contribute to the project.

### How to Provide Feedback:
1. **Open an Issue**: If you find a bug or have an enhancement suggestion, please open an issue in the [GitHub repository](https://github.com/your-username/PasswordStrengthChecker/issues).
2. **Submit a Pull Request**: If you've fixed a bug or added a new feature, submit a pull request for review. Please follow the contribution guidelines outlined below.

### Common Feedback Topics:
- Bug reports
- Feature requests
- Performance improvements
- UI/UX suggestions (if applicable)

Thank you!
