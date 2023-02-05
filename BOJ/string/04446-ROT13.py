vowels = {'a': 'e', 'i': 'o', 'y': 'u', 'e': 'a', 'o': 'i', 'u': 'y'}
consonants = {'b': 'p',
              'k': 'v',
              'x': 'j',
              'z': 'q',
              'n': 't',
              'h': 's',
              'd': 'r',
              'c': 'l',
              'w': 'm',
              'g': 'f',
              'p': 'b',
              'v': 'k',
              'j': 'x',
              'q': 'z',
              't': 'n',
              's': 'h',
              'r': 'd',
              'l': 'c',
              'm': 'w',
              'f': 'g'
              }

while 1:
    try:
        sentence = list(input())
        ans = ''

        for each in sentence:
            upper = False
            if each.lower() != each:
                upper = True
            if each.lower() in vowels:
                if upper:
                    ans += vowels[each.lower()].upper()
                else:
                    ans += vowels[each.lower()]

            elif each.lower() in consonants:
                if upper:
                    ans += consonants[each.lower()].upper()
                else:
                    ans += consonants[each.lower()]
            else:
                ans += each
        print(ans)
    except: 
        break
  