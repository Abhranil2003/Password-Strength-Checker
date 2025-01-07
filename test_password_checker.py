import unittest
from password_checker import check_password_strength

class TestPasswordStrengthChecker(unittest.TestCase):
    def test_strong_password(self):
        """Test a strong password."""
        password = "Str0ng@Passw0rd!"
        is_strong, feedback = check_password_strength(password)
        self.assertTrue(is_strong)
        self.assertEqual(len(feedback), 0)

    def test_short_password(self):
        """Test a password that is too short."""
        password = "Ab1!"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password should be at least 8 characters long.", feedback)

    def test_missing_uppercase(self):
        """Test a password missing uppercase letters."""
        password = "weakpass1!"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password should include at least one uppercase letter.", feedback)

    def test_missing_lowercase(self):
        """Test a password missing lowercase letters."""
        password = "WEAKPASS1!"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password should include at least one lowercase letter.", feedback)

    def test_missing_digit(self):
        """Test a password missing digits."""
        password = "NoDigits!"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password should include at least one digit.", feedback)

    def test_missing_special_character(self):
        """Test a password missing special characters."""
        password = "NoSpecial1"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password should include at least one special character (e.g., @, #, $).", feedback)

    def test_contains_spaces(self):
        """Test a password that contains spaces."""
        password = "Invalid Password1!"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password should not contain spaces.", feedback)

    def test_repetitive_characters(self):
        """Test a password with too many repetitive characters."""
        password = "aaaBBB111!!!"
        is_strong, feedback = check_password_strength(password)
        self.assertFalse(is_strong)
        self.assertIn("Password has too many repetitive characters; try adding more variety.", feedback)

if __name__ == "__main__":
    unittest.main()
