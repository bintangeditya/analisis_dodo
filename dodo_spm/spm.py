import csv
# import text_utils as tu
from dodo_spm  import text_utils as tu

forbidden_word = []
with open(r'dodo_spm\bad-bad-word-cleaned.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for i in data:
    forbidden_word.append(i[0])

def check_forbidden_word(raw_text)->int:
    '''
    :rtype: integer
    :type text : string
    :param text: type string, text 
    :return: integer, 1 jika menemukan forbidden word, 0 jika tidak ditemukan forbidden word
    '''    
    text_ = raw_text.lower()
    for fword in forbidden_word:
        if fword in text_:
            return 1
    return 0

def profanity_check_url(raw_url):
    url_clean = tu.cleaning_url(raw_url)
    text_ = tu.cleaning_text(url_clean)
    v_check_forbidden_word = check_forbidden_word(url_clean)
    if v_check_forbidden_word == 1: return 'berbahaya'
    return 'aman'