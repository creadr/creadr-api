# -*- coding=UTF-8 -*-
def split_zh_en(string):

    # convert to unicode string

    string = string.decode('utf-8')

    unicodeStr = string
    zh_group = []
    zh_gather = ""
    zh_status = False

    for c in unicodeStr:
        if not zh_status and is_zh(c):
            zh_status = True
        elif not is_zh(c) and zh_status:
            zh_status = False
            if zh_gather != "":
                zh_group.append(zh_gather.encode('utf-8'))
        if zh_status:
            zh_gather += c
        else:
            zh_gather = ""


    if zh_gather != "":
# return bytethings
        zh_group.append(zh_gather.encode('utf-8'))

    return zh_group


def is_zh(c):
    # c needs to by a unicode string
    x = ord(c)
    # Punct & Radicals
    if x >= 0x2e80 and x <= 0x33ff:
        return True

    # Fullwidth Latin Characters
    elif x >= 0xff00 and x <= 0xffef:
        return True

    # CJK Unified Ideographs &
    # CJK Unified Ideographs Extension A
    elif x >= 0x4e00 and x <= 0x9fbb:
        return True
    # CJK Compatibility Ideographs
    elif x >= 0xf900 and x <= 0xfad9:
        return True

    # CJK Unified Ideographs Extension B
    elif x >= 0x20000 and x <= 0x2a6d6:
        return True

    # CJK Compatibility Supplement
    elif x >= 0x2f800 and x <= 0x2fa1d:
        return True

    else:
        return False