import sys


def main():
    thing = sys.argv[1]
    if thing == "B":
        print("Test succeeded, return without error.")
        return 0
    else:
        raise ValueError("Error in test_simple.py.")

if __name__ == "__main__":
    main()
