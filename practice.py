import math

class SelectionProbability:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    def calculate_combinations(self):
        return math.comb(self.n, self.r)

    def calculate_probability(self):
        total_combinations = self.calculate_combinations()
        if total_combinations > 0:
            return 1 / total_combinations
        else:
            return 0

def main():
    while True:
        try:
            n = int(input("Enter the total number of seats (N): "))
            if n == 0:
                print("Exit")
                break
            r = int(input("Enter the number of participants to select (r): "))

            if r > n:
                print("Invalid input! r cannot be greater than N.")
                continue

        except ValueError:
            print("Invalid input! Please enter an integer value.")
            continue

        selection_prob = SelectionProbability(n, r)
        combinations = selection_prob.calculate_combinations()
        probability = selection_prob.calculate_probability()

        print(f"\nNumber of ways to select {r} participants from {n} available seats: {combinations}")
        print(f"Probability of selecting any specific group of {r} participants: {probability:.6f}")

if __name__ == "__main__":
    main()
