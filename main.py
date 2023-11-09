import re

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

code = ".-...-"

# detect three times the same char
def consecutive(s):
    return re.search(r'(.)\1\1', s)

def decipher(code: str, word: str, removeConsecutive: bool = False) -> list:
    result = []
    for letter, morse in MORSE_CODE_DICT.items():
        if code.startswith(morse):
            new_word = word + letter
            new_code = code[len(morse):]
            if (len(new_code) == 0):
                # check for unnatural repetition of chars
                if not (consecutive(new_word) and removeConsecutive):
                    result.append(new_word)
            else:
                result.extend(decipher(new_code, new_word))
    return result

if __name__ == '__main__':
    results = decipher(code, "")
    print("There are", len(results), "combinations.")
    for r in results:
        print(r)
