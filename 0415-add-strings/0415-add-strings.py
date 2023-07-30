class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    carry = 0
    result = []
    index1 = len(num1) - 1
    index2 = len(num2) - 1
    while index1 >= 0 or index2 >= 0 or carry:
      if index1 >= 0:
        carry += int(num1[index1])
        index1 -= 1
      if index2 >= 0:
        carry += int(num2[index2])
        index2 -= 1
      result.append(str(carry % 10))
      carry //= 10
    return ''.join(reversed(result))