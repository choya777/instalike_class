from langdetect import detect_langs




def get_lang(self):
    lan = detect_langs(self)
    for item in lan:
        return item.lang





