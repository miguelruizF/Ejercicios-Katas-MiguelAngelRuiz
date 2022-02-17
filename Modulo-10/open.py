""" def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main() """

""" try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")
 """
""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!") """

""" def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!") """

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
if __name__ == '__main__':
    main()