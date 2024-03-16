#Github: www.github.com/M-Guney
def lowertoupper(kelime):
    harfler = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'ç': 'Ç',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'ğ': 'Ğ',
        'h': 'H',
        'ı': 'I',
        'i': 'İ',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'o': 'O',
        'ö': 'Ö',
        'p': 'P',
        'r': 'R',
        's': 'S',
        'ş': 'Ş',
        't': 'T',
        'u': 'U',
        'ü': 'Ü',
        'v': 'V',
        'y': 'Y',
        'z': 'Z'
    }
    if kelime[0] in harfler:
        return harfler[kelime[0]] + kelime[1:]
    elif kelime[0] not in harfler:
        return kelime[0].upper() + kelime[1:]
    else:
        return kelime

def all_lowertoupper(kelime):
    harfler = {
        'a': 'A',
        'b': 'B',
        'c': 'C',
        'ç': 'Ç',
        'd': 'D',
        'e': 'E',
        'f': 'F',
        'g': 'G',
        'ğ': 'Ğ',
        'h': 'H',
        'ı': 'I',
        'i': 'İ',
        'j': 'J',
        'k': 'K',
        'l': 'L',
        'm': 'M',
        'n': 'N',
        'o': 'O',
        'ö': 'Ö',
        'p': 'P',
        'r': 'R',
        's': 'S',
        'ş': 'Ş',
        't': 'T',
        'u': 'U',
        'ü': 'Ü',
        'v': 'V',
        'y': 'Y',
        'z': 'Z'
    }
    cikti = ''
    for harf in kelime:
        if harf in harfler:
            cikti += harfler[harf]
        else:
            cikti += harf.upper()
    return cikti

def uppertolower(kelime):
    harfler = {
        'A': 'a',
        'B': 'b',
        'C': 'c',
        'Ç': 'ç',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g',
        'Ğ': 'ğ',
        'H': 'h',
        'I': 'ı',
        'İ': 'i',
        'J': 'j',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'O': 'o',
        'Ö': 'ö',
        'P': 'p',
        'R': 'r',
        'S': 's',
        'Ş': 'ş',
        'T': 't',
        'U': 'u',
        'Ü': 'ü',
        'V': 'v',
        'Y': 'y',
        'Z': 'z'
    }
    if kelime[0] in harfler:
        return harfler[kelime[0]] + kelime[1:]
    elif kelime[0] not in harfler:
        return kelime[0].lower() + kelime[1:]
    else:
        return kelime
    
def all_uppertolower(kelime):
    harfler = {
        'A': 'a',
        'B': 'b',
        'C': 'c',
        'Ç': 'ç',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g',
        'Ğ': 'ğ',
        'H': 'h',
        'I': 'ı',
        'İ': 'i',
        'J': 'j',
        'K': 'k',
        'L': 'l',
        'M': 'm',
        'N': 'n',
        'O': 'o',
        'Ö': 'ö',
        'P': 'p',
        'R': 'r',
        'S': 's',
        'Ş': 'ş',
        'T': 't',
        'U': 'u',
        'Ü': 'ü',
        'V': 'v',
        'Y': 'y',
        'Z': 'z'
    }
    cikti = ''
    for harf in kelime:
        if harf in harfler:
            cikti += harfler[harf]
        else:
            cikti += harf.lower()
    return cikti
