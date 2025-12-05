import sys

def greet(name):
    return f"Hello, {name}! This is running inside GitHub Actions."

def main():
    if len(sys.argv) < 2:
        print("No name provided.")
        return

    name = sys.argv[1]
    print(greet(name))

if __name__ == "__main__":
    main()
