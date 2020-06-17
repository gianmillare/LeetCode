class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = map(str, digits)
        digits = ''.join(digits)
        digits = int(digits)
        digits += 1
        digits = str(digits)
        digits = list(digits)
        results = map(int, digits)
        return results