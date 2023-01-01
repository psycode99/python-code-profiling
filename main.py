import time
import cProfile
import pstats


# def fast():
#     print('I run fast!')
#
#
# def slow():
#     time.sleep(3)
#     print('I run slow')
#
#
# def medium():
#     time.sleep(0.5)
#     print('i run slightly slow')
#
#
# def main():
#     fast()
#     slow()
#     medium()
#
#
#
# cProfile.run()


# if __name__ == '__main__':
#     main()


def checker():
    name = True
    clas = True
    if name == True and clas == True:
        print('all true')


cProfile.run('checker()')
