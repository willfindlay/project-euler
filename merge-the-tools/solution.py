def diet(string):
    chars = []
    for c in string:
        if c not in chars:
            chars.append(c)
    return ''.join(chars)

def merge_the_tools(string, k):
    strings = [string[i:i+k] for i in range(0, len(string), k)]
    strings = list(map(diet, strings))

    for string in strings:
        print(string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
