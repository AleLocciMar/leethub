class Solution:
    def test(self, y:int):
        if not (-2 ** 31 <= y <= 2 ** 31 - 1):
            return True
        return False

    def reverse(self, x: int) -> int:

            if self.test(x):
               return 0

            negative = False
            if x < 0:
                negative = True
                x = abs(x)

            num_str = str(x)
            num_str_inv = num_str[::-1]

            if self.test(int(num_str_inv)):
                return 0

            if negative:
                return -1 * int(num_str_inv)

            return int(num_str_inv)