
import threading

def print_test():
    print('othre thread')
    print('othre thread')
    print('othre thread')

def main():
    print('this is main thread')
    t = threading.Thread(target=print_test)
    t.start()
    t.join()

if __name__ == '__main__':
    main()
