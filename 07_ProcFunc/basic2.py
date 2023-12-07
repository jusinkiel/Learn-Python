# Global Variable
# Local Variable

# Rand2 is global variable
rand2 = "xxxxx"

def test():
    # Rand is a local variable
    rand = "blablabla"
    
    return True

def main():
    test()
    print("rand ", rand2)
    print(test())


if __name__ == '__main__':
    main()

