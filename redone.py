#STILL WORKING ON IT NEEDS TO BE REDONE
import random
import time


def main():
    print("Reaction Time Test")
    print("When 'GO!' appears, press Enter as fast as possible.\n")

    input("Press Enter to begin...")

    attempts = 5
    scores = []

    for round_num in range(1, attempts + 1):
        print(f"Round {round_num} of {attempts}")
        print("Ready...")

        time.sleep(random.uniform(2.0, 4.5))

        print("GO!")
        start = time.monotonic()
        input()
        elapsed = time.monotonic() - start

        scores.append(elapsed)
        print(f"Time: {elapsed:.3f} seconds")

    best = min(scores)
    avg = sum(scores) / len(scores)

    print("--- Results ---")
    print(f"Best time:    {best:.3f}s")
    print(f"Average time: {avg:.3f}s")


if __name__ == "__main__":
    main()