import re
from . import emo_unicode
from string import digits 
#import emo_unicode

'''emot library to detect emoji and emoticons.

    >>> import emot
    >>> text = "I love python 👨 :-)"
    >>> emot.emoji(text)
    >>> {'value': ['👨'], 'mean': [':man:'], 'location': [[14, 14]], 'flag': True}
    >>> emot.emoticons(text)
    >>> {'value': [':-)'], 'location': [[16, 19]], 'mean': ['Happy face smiley'], 'flag': True}
'''

__all__ = ['emoji','emoticons']

def emoji(string):
    '''emot.emoji is use to detect emoji from text

        >>> text = "I love python 👨 :-)"
        >>> emot.emoji(text)
        >>> {'value': ['👨'], 'mean': [':man:'], 'location': [[14, 14]], 'flag': True}
    '''
    __entities = {}
    __value = []
    __mean = []
    __location = []
    flag = True
    try:
        pro_string = str(string)
        for pos,ej in enumerate(pro_string):
            if ej in emo_unicode.UNICODE_EMO:
                try:
                    __value.append(ej)
                    __mean.append(emo_unicode.UNICODE_EMO[ej])
                    __location.append([pos,pos])
                except Exception as e:
                    flag = False
                    __entities.append({"flag": False})
                    return __entities

    except Exception as e:
        flag = False
        __entities.append({"flag": False})
        return __entities
    if len(__value) < 1:
        flag = False    
    __entities = {
        'value' : __value,
        'mean' : __mean,
        'location' : __location,
        'flag' : flag
    }

    return __entities

def emoticons(string):
    '''emot.emoticons is use to detect emoticons from text

        >>> text = "I love python 👨 :-)"
        >>> emot.emoticons(text)
        >>> {'value': [':-)'], 'location': [[16, 19]], 'mean': ['Happy face smiley'], 'flag': True}
    '''
    __entities = []
    flag = True
    try:
        pattern = u'(' + u'|'.join(k for k in emo_unicode.EMOTICONS) + u')'
        __entities = []
        __value = []
        __location = []
        matches = re.finditer(r"%s"%pattern,str(string))
        for et in matches:
            __value.append(et.group().strip())
            __location.append([et.start(),et.end()])
            
        __mean = []
        for each in __value:
            __mean.append(emo_unicode.EMOTICONS_EMO[each])
        
        if len(__value) < 1:
            flag = False
        __entities = {
        'value' : __value,
        'location' : __location,
        'mean' : __mean,
        'flag' : flag
        }
    except Exception as e:
        __entities = {'flag' : False}
        #print("No emoiticons found")
        return __entities

    return __entities

def convert_emojis(text):
    """ Function to convert emoji into word """
    for emot in emo_unicode.UNICODE_EMO:
        text = text.replace(emot, "_".join(emo_unicode.UNICODE_EMO[emot].replace(",","").replace(":","").split()))
    return text 

def convert_emoticons(text):
    """ Function to convert emoticons into word """
    for emot in emo_unicode.EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(emo_unicode.EMOTICONS[emot].replace(",","").split()), text)
    return text




# ------------------- Under development -----------------------
def convert_emojis_vn(text):
    """ Function to convert emoji into word """
    for emot in emo_unicode.UNICODE_EMO_VN:
        # using translate and digits 
        # to remove numeric digits from string 
        remove_digits = str.maketrans('', '', digits) 
        text = text.replace(emot, " ".join(emo_unicode.UNICODE_EMO_VN[emot].\
            replace(",","").replace(":","").split()).translate(remove_digits).strip())
    return text 

def convert_emoticons_vn(text):
    """ Function to convert emoticons into word """
    for emot in emo_unicode.EMOTICONS_VN:
        text = re.sub(u'('+emot+')', " ".join(emo_unicode.EMOTICONS_VN[emot].replace(",","").split()), text)
    return text



def remove_emoji(string):
    """ Function to remove emoji. """
    emoji_pattern = re.compile("["
                            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "\U0001F300-\U0001F5FF"  # symbols & pictographs
                            "\U0001F600-\U0001F64F"  # emoticons
                            "\U0001F680-\U0001F6FF"  # transport & map symbols
                            "\U0001F700-\U0001F77F"  # alchemical symbols
                            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                            "\U0001FA00-\U0001FA6F"  # Chess Symbols
                            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                            "\U00002702-\U000027B0"  # Dingbats
                            "\U000024C2-\U0001F251" 
                            "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def remove_emoticons(text):
    """ Function for removing emoticons """
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in emo_unicode.EMOTICONS) + u')')    # OR
    return emoticon_pattern.sub(r'', text)



def test_emo():
    test = "I love python 👨 :-)"
    print(test)
    print(emoji(test))
    print(emoticons(test))
    return None

def about():
    text = "emot library: emoji and emoticons library for python. It return emoji or emoticons from string with location of it. \nAuthors: \n Neel Shah: neelknightme@gmail.com or https://github.com/NeelShah18 \n Subham Rohilla: kaka.shubham@gmail.com or https://github.com/kakashubham"
    print(text)
    return None

if __name__ == '__main__':
    test_emo()
