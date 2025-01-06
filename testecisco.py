from platform import python_implementation, python_version_tuple

def main():
    # Print the implementation of Python being used
    print(f"Python Implementation: {python_implementation()}")
    
    # Print each part of the Python version
    version_parts = python_version_tuple()
    for part in version_parts:
        print(f"Version Part: {part}")

if __name__ == "__main__":
    main()
