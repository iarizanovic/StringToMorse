Scrap dictionary from: https://en.wikipedia.org/wiki/Morse_code

Then, convert the string from input to morse and decode it for test.

Scraped dictionary:
```
{
    ' ': '    ', 
    'A': '  ▄ ▄▄▄ ', 
    'a': '  ▄ ▄▄▄ ', 
    'B': '  ▄▄▄ ▄ ▄ ▄ ', 
    'b': '  ▄▄▄ ▄ ▄ ▄ ', 
    'C': '  ▄▄▄ ▄ ▄▄▄ ▄ ', 
    'c': '  ▄▄▄ ▄ ▄▄▄ ▄ ', 
    'D': '  ▄▄▄ ▄ ▄ ', 
    'd': '  ▄▄▄ ▄ ▄ ', 
    'E': '  ▄ ', 
    'e': '  ▄ ', 
    'F': '  ▄ ▄ ▄▄▄ ▄ ', 
    'f': '  ▄ ▄ ▄▄▄ ▄ ', 
    'G': '  ▄▄▄ ▄▄▄ ▄ ', 
    'g': '  ▄▄▄ ▄▄▄ ▄ ', 
    'H': '  ▄ ▄ ▄ ▄ ', 
    'h': '  ▄ ▄ ▄ ▄ ', 
    'I': '  ▄ ▄ ', 
    'i': '  ▄ ▄ ', 
    'J': '  ▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'j': '  ▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'K': '  ▄▄▄ ▄ ▄▄▄ ', 
    'k': '  ▄▄▄ ▄ ▄▄▄ ', 
    'L': '  ▄ ▄▄▄ ▄ ▄ ', 
    'l': '  ▄ ▄▄▄ ▄ ▄ ', 
    'M': '  ▄▄▄ ▄▄▄ ', 
    'm': '  ▄▄▄ ▄▄▄ ', 
    'N': '  ▄▄▄ ▄ ', 
    'n': '  ▄▄▄ ▄ ', 
    'O': '  ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'o': '  ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'P': '  ▄ ▄▄▄ ▄▄▄ ▄ ', 
    'p': '  ▄ ▄▄▄ ▄▄▄ ▄ ', 
    'Q': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    'q': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    'R': '  ▄ ▄▄▄ ▄ ', 
    'r': '  ▄ ▄▄▄ ▄ ', 
    'S': '  ▄ ▄ ▄ ', 
    's': '  ▄ ▄ ▄ ', 
    'T': '  ▄▄▄ ', 
    't': '  ▄▄▄ ', 
    'U': '  ▄ ▄ ▄▄▄ ', 
    'u': '  ▄ ▄ ▄▄▄ ', 
    'V': '  ▄ ▄ ▄ ▄▄▄ ', 
    'v': '  ▄ ▄ ▄ ▄▄▄ ', 
    'W': '  ▄ ▄▄▄ ▄▄▄ ', 
    'w': '  ▄ ▄▄▄ ▄▄▄ ', 
    'X': '  ▄▄▄ ▄ ▄ ▄▄▄ ', 
    'x': '  ▄▄▄ ▄ ▄ ▄▄▄ ', 
    'Y': '  ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    'y': '  ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    'Z': '  ▄▄▄ ▄▄▄ ▄ ▄ ', 
    'z': '  ▄▄▄ ▄▄▄ ▄ ▄ ', 
    '0': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    '1': '  ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    '2': '  ▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    '3': '  ▄ ▄ ▄ ▄▄▄ ▄▄▄ ', 
    '4': '  ▄ ▄ ▄ ▄ ▄▄▄ ', 
    '5': '  ▄ ▄ ▄ ▄ ▄ ', 
    '6': '  ▄▄▄ ▄ ▄ ▄ ▄ ', 
    '7': '  ▄▄▄ ▄▄▄ ▄ ▄ ▄ ', 
    '8': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ', 
    '9': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    '.': '  ▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ', 
    ',': '  ▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄ ', 
    '?': '  ▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄ ', 
    "'": '  ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    '!': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    '/': '  ▄▄▄ ▄ ▄ ▄▄▄ ▄ ', 
    '(': '  ▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ', 
    ')': '  ▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    ':': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄ ', 
    ';': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄ ', 
    '=': '  ▄▄▄ ▄ ▄ ▄ ▄▄▄ ', 
    '+': '  ▄ ▄▄▄ ▄ ▄▄▄ ▄ ', 
    '_': '  ▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    '"': '  ▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄ ', 
    '$': '  ▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄▄▄ ', 
    '@': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄ ', 
    'À': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    'à': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    'Ä': '  ▄ ▄▄▄ ▄ ▄▄▄ ', 
    'ä': '  ▄ ▄▄▄ ▄ ▄▄▄ ', 
    'Å': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    'å': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄▄▄ ', 
    'Ą': '  ▄ ▄▄▄ ▄ ▄▄▄ ', 
    'ą': '  ▄ ▄▄▄ ▄ ▄▄▄ ', 
    'Æ': '  ▄ ▄▄▄ ▄ ▄▄▄ ', 
    'æ': '  ▄ ▄▄▄ ▄ ▄▄▄ ', 
    'Ć': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄ ', 
    'ć': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄ ', 
    'Ĉ': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄ ', 
    'ĉ': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄ ', 
    'Ç': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄ ', 
    'ç': '  ▄▄▄ ▄ ▄▄▄ ▄ ▄ ', 
    'Đ': '  ▄ ▄ ▄▄▄ ▄ ▄ ', 
    'đ': '  ▄ ▄ ▄▄▄ ▄ ▄ ', 
    'Ð': '  ▄ ▄ ▄▄▄ ▄▄▄ ▄ ', 
    'ð': '  ▄ ▄ ▄▄▄ ▄▄▄ ▄ ', 
    'É': '  ▄ ▄ ▄▄▄ ▄ ▄ ', 
    'é': '  ▄ ▄ ▄▄▄ ▄ ▄ ', 
    'È': '  ▄ ▄▄▄ ▄ ▄ ▄▄▄ ', 
    'è': '  ▄ ▄▄▄ ▄ ▄ ▄▄▄ ', 
    'Ę': '  ▄ ▄ ▄▄▄ ▄ ▄ ', 
    'ę': '  ▄ ▄ ▄▄▄ ▄ ▄ ', 
    'Ĝ': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄ ', 
    'ĝ': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄ ', 
    'Ĥ': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'ĥ': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'Ĵ': '  ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'ĵ': '  ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'Ł': '  ▄ ▄▄▄ ▄ ▄ ▄▄▄ ', 
    'ł': '  ▄ ▄▄▄ ▄ ▄ ▄▄▄ ', 
    'Ń': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    'ń': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    'Ñ': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    'ñ': '  ▄▄▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ', 
    'Ó': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'ó': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'Ö': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'ö': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'Ø': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'ø': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄ ', 
    'Ś': '  ▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄ ', 
    'ś': '  ▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄ ', 
    'Ŝ': '  ▄ ▄ ▄ ▄▄▄ ▄ ', 
    'ŝ': '  ▄ ▄ ▄ ▄▄▄ ▄ ', 
    'Š': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'š': '  ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ', 
    'Þ': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄ ', 
    'þ': '  ▄ ▄▄▄ ▄▄▄ ▄ ▄ ', 
    'Ü': '  ▄ ▄ ▄▄▄ ▄▄▄ ', 
    'ü': '  ▄ ▄ ▄▄▄ ▄▄▄ ', 
    'Ŭ': '  ▄ ▄ ▄▄▄ ▄▄▄ ', 
    'ŭ': '  ▄ ▄ ▄▄▄ ▄▄▄ ', 
    'Ź': '  ▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄ ', 
    'ź': '  ▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄ '
}
```