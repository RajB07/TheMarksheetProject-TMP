import re


#Find all digit characters:

#x = re.findall("\d{2}", txt)
# x = re.findall('\d{7}', txt)

def splitEachRow(txt):
    # txt = re.sub('-+','',txt)
    # txt = re.sub('\s\s+','   ',txt).lstrip().rstrip()
    txt = re.sub('[/]',' ',txt)
    # txt = re.sub('\s[)]',')',txt)
    # txt = re.sub('\s[(]','(',txt)
    txt = ' ' + txt
    y = re.split(r'(\s[0-9][0-9][0-9][0-9][0-9][0-9][0-9]\D)',txt)
    y.pop(0)
    return y

splitEachRow(t)
