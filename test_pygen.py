import unittest
from pygenerator import PyGen


class BasicSecureTest(unittest.TestCase):

    def test_password_length(self):
        # test length
        result = PyGen("hello")
        self.assertEqual(result.is_password_strong, False)

    def test_unsecure_passwords(self):
        # unsecure passwords greater than or equal to a minimun length of 8.
        unsecure_passwords = [
            "THUTFDGSV",
            "pzagzqmxk",
            "97505417562",
            "!!=>$@<^%*]",
            "l#[f+$_m==h",
            "U!Q%*P?;EA",
            "6)+|4$52|4",
            "mRwFifffFaV",
            "M7YB10Z1JIK",
            "36x51r2oopu",
            "QM0BERFEEH1",
            "h<zi|!`d>-k"
        ]

        for password in unsecure_passwords:
            result = PyGen(password=password)
            self.assertEqual(result.is_password_strong, False)


if __name__ == '__main__':
    unittest.main()
