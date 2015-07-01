"""
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then, working out the alphabetical value for each name,
multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical
order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a
score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def generate_names_list(filepath):

    res = []
    with open(filepath, 'r') as f:
        names = f.readline().split(',')
        for name in names:
            res.append(name.replace('"', ""))

    return res




def name_score(name, pos):
    return sum([ord(char.upper()) - 64 for char in list(name)]) * pos


def score_list(filepath):

    names = generate_names_list(filepath)
    names.sort()

    res = 0

    for pos, name in enumerate(names):
        res += name_score(name, pos+1)

    return res




if __name__ == '__main__':

    print(score_list('names.txt'))
