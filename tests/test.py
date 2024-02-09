import unittest
from unittest.mock import patch
from password_generator import generate_password

class TestGeneratePassword(unittest.TestCase):

    @patch('builtins.input', return_value='16') 
    def test_generate_password_default_length(self, mock_input):
        with patch('random.choice', side_effect=lambda x: 'a'):
            generated_password = generate_password(16)
        self.assertEqual(generated_password, 'a' * 16)

    def test_generate_password_randomness(self):

        password1 = generate_password(12)
        password2 = generate_password(12)
        self.assertNotEqual(password1, password2)

if __name__ == '__main__':
    unittest.main()
