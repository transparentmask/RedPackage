#!/bin/python
# -*- coding: utf-8 -*-
import argparse
from random import randint, uniform


MIN_MONEY = 0.01


def split_money(money, persons):
    if persons == 1:
        return [money]

    # split person first
    count = [persons / 2, persons / 2]
    if persons % 2 != 0:
        count[randint(0, 1)] += 1

    min_money = round(float(MIN_MONEY * count[0]), 2)
    max_money = round(money - float(MIN_MONEY * count[1]), 2)
    first = round(uniform(min_money, max_money), 2)
    second = round(money - first, 2)

    result = []
    result.extend(split_money(first, count[0]))
    result.extend(split_money(second, count[1]))

    return result


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('--money', '-m', help='Total Money', dest='money', default=100, type=float)
    parse.add_argument('--persons', '-p', help='Persons', dest='persons', default=10, type=int)
    args = parse.parse_args()

    if args.money < float(args.persons * MIN_MONEY):
        print('Not enough money!')
        exit(1)

    result = split_money(args.money, args.persons)
    print(result)
    print(sum(result))


if __name__ == '__main__':
    main()
