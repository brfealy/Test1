import sys
import os

def main():
    x = sys.argv[1]
    if x == "A":
        print("Test succeeded, return 0")
        return 0
    else:
        raise ValueError("Error in test_simple.py")

if __name__ == "__main__":
    main()