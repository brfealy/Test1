import sys


if __name__ == "__main__":
    thing = sys.argv[1]
    if thing == "B":
        
        print("Test succeeded, return without error.")

    else:
        raise ValueError("Error in test_simple.py.")

