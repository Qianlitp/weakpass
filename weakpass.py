#!/usr/bin/python3
"""
    create by 9ian1i

    base

"""

import sys
import getopt
import itertools
import re


input_list = []
number_list = []
letter_list = []
choice = ''
repeat_num = 1


def usage():
    print('     a simple script to create weak password by using keywords')
    print('                                     create by 9ian1i')
    print()
    print('     -h --help   - usage')
    print('     -k          - the keywords.')
    print('     -s          - cartesian products of all keywords')
    print('     -p          - permutations of all keywords')
    print('     -c          - combinations of all keywords')
    print('     -r=number   - allow times of repeat .(default 1, effective except cartesian products)')
    print('     -d          - the directory of output file (default wordlist.txt)')
    print()
    print('     !suggest to separate number and letter when you input the keywords.')
    print('         eg: weakpass -k test,2016,china,muc .Don\'t use such words: -k test123,china2016.')
    sys.exit(0)


def get_input():
    global input_list
    global choice
    global repeat_num

    try:
        options, args = getopt.getopt(sys.argv[1:], "hk:spr:c", ['help'])
    except getopt.GetoptError as error:
        print(str(error))
        usage()
    for opt, arg in options:
        if opt in ("-h", "--help"):
            usage()
        elif opt == "-k":
            input_list = arg.split(',')
        elif opt == "-s":
            choice = 's'
        elif opt == "-p":
            choice = 'p'
        elif opt == "-r":
            if re.match('^\d+$', arg):
                repeat_num = arg
            else:
                exit("repeat times must be a number!")
        elif opt == "-c":
            choice = 'c'
        else:
            print("invalid option!")
            usage()


def main():
    global input_list
    global letter_list

    get_input()
    separate(input_list)
    product()
    upper_lower(letter_list)


# 笛卡尔积
def product():
    global letter_list
    global number_list

    letter = letter_list[:]
    number = number_list[:]
    letter.extend(number)
    for x in range(1, len(letter)+1):
        for i in itertools.permutations(letter, x):
            print(i)


# 字母大小写混淆
def upper_lower(in_list):
    global choice

    for x in range(len(in_list)):
        in_list[x] = in_list[x].lower()
        count = len(in_list[x])
        for y in range(count):
            in_list[x] = in_list[x].replace(in_list[x][y], in_list[x][y].upper(), 1)
            if choice == 's':
                product()


# 排列
def permutation():
    pass


# 区分纯数字和单词
def separate(in_list):
    for each in in_list:
        if re.match('^\d+$', each):
            number_list.append(each)
        elif re.match('^[A-Za-z]+$', each):
            letter_list.append(each)
        else:
            print('warning: abandon the word ' + each)


if __name__ == '__main__':
    main()
