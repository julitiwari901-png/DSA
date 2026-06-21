class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1]
            value = 1

            for j in range(1, i + 1):
                value = value * (i - j + 1) // j
                row.append(value)

            triangle.append(row)

        return triangle
            