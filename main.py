# main.py
from sum import add
from difference import subtract

def main():
    a, b = 10, 5
    print("Sum:", add(a, b))
    print("Difference:", subtract(a, b))

if __name__ == "__main__":
    main()