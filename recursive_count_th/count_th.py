'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur
within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    count = 0
    if len(word) < 2:
        print(f'{word} is < 2 characters; adding {count} and stopping...')
        return count
    elif word.startswith('th'):
        count = 1
        print(f'{word} starts with "th"; adding {count}')
    print(f'next up is {word[1:]}')
    count += count_th(word[1:])
    print(f'updated count is {count}')
    return count
