class HarmonicNumbers:
    @classmethod
    def get_result(cls, n: int, result: float = 0.0):
        for i in range(1, n):
            result += 1/i

        return result


if __name__ == "__main__":
    h = HarmonicNumbers.get_result(n=10000)
    print(h)
