import re
import math

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'Ä':'.-.-', 'Ü':'..--', 'Ö':'---.',
                    'ß':'...--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
           
# wordlist source https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4           
words = open("wordlist-german.txt", encoding="utf8").read().upper().split()
wordcost = dict((k, math.log((i+1)*math.log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def consecutive(s: str) -> bool:
    """
    detect three times the same char
    """
    return re.search(r'(.)\1\1', s)
    
def infer_spaces(s: str) -> list[str]:
    """
        Infers spaces between words from a word list based on a cost function.
        Source https://stackoverflow.com/a/11642687/2173320
    """
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k    
    return " ".join(reversed(out))
    
def decipher(code: str, word: str, removeConsecutive: bool = False) -> list[str]:
    """
        Recursively find all possible combinations of letters of a decuded morse code consisting of '-', and '.'
    """
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


def n_letter_filter(words:list[str], min_letter:int=3, min_letter_percentage:float=0.3) -> bool:
    """
        Returns false, if the words list contains more than min_letter_percentage percent of words with lesser than min_letter characters.
    """
    result = []
    one_letter_count = 0
    for w in words:
        if len(w) < min_letter:
            one_letter_count += 1
    percentage = one_letter_count / len(words)
    if percentage > min_letter_percentage:
        return False
    return True
    

if __name__ == '__main__':
    #code = "-.-.-.-...." # Käse, Kekse
    code = "-.-.-.-.........-.-...-.-.-.-..-." # Käse ist lecker
    results = decipher(code, "")
    print("There are", len(results), "combinations.")
    for r in results:
    
        # infer spaces between words from word list
        with_spaces = infer_spaces(r)
        
        # filter all sentences with more than 30% of words < 3 characters
        if n_letter_filter(with_spaces.split(), 3, 0.3):
            print("raw:", r, "with spaces:", with_spaces)
