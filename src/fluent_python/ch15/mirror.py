# -*- coding: UTF-8 -*-


class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):  # <5>
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # <6>
        import sys  # <7>
        sys.stdout.write = self.original_write  # <8>
        if exc_type is ZeroDivisionError:  # <9>
            print('Please DO NOT divide by zero!')
            return True  # <10>


def main():
    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)


if __name__ == '__main__':
    main()
