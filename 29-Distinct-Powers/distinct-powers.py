def distinct_powers(L):

    r = range(2, L+1)

    return len({a**b for a in r for b in r})


if __name__ == '__main__':
    print(distinct_powers(100))
