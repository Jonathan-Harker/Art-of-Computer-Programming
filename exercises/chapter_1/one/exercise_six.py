class EuclidsAlgorithmCounted:
    def __init__(self, counter: int = 0):
        self.counter = counter

    def get_average_times_run(self, max_m: int, n: int) -> float:
        sum_times_ran = 0
        for i in range(1, max_m + 1):
            self.counter = 0
            r = self.euclids_algorithm_counted(m=i, n=n)
            sum_times_ran += r['counter']

        return sum_times_ran / max_m

    def euclids_algorithm_counted(self, m: int, n: int) -> dict:
        self.counter += 1
        if n > m:
            n, m = m, n

        if m % n == 0:
            return {"result": n, "counter": self.counter}

        return self.euclids_algorithm_counted(m=n, n=m % n)


if __name__ == "__main__":
    e = EuclidsAlgorithmCounted()
    r = e.get_average_times_run(max_m=1000000, n=5)
    print(r)
