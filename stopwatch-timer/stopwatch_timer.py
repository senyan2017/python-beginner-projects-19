import time


def read_positive_seconds():
    while True:
        raw_value = input("Enter time in seconds: ").strip()
        if not raw_value:
            print("Please enter a value.")
            continue
        try:
            seconds = int(raw_value)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if seconds <= 0:
            print("Please enter a positive number of seconds.")
            continue
        return seconds


def stopwatch():
    print("Stopwatch started. Press Enter to stop.")
    start_time = time.time()
    input()
    elapsed = time.time() - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")


def timer(seconds):
    print(f"Timer started for {seconds} seconds.")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!            ")


def main():
    while True:
        print("\nChoose an option:")
        print("1. Stopwatch")
        print("2. Timer")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            stopwatch()
        elif choice == "2":
            timer(read_positive_seconds())
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
