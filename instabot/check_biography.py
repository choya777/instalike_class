from langdetect import detect_langs


words_he = ['איפור', 'מאפרת', 'ומאפרת', 'מעצבת שיער', 'מעצבת שיער', 'חתונה', 'שמלת כלה', 'כלה', 'makeup', 'Makeup', 'bridal']


def get_lang(self):
    lan = detect_langs(self)
    for item in lan:
        if "he" in item.lang:
            print(" hebrew language detected ")
            return "hebrew"
        elif "en" in item.lang:
            print(" hebrew language detected ")
            return "english"
        else:
            print("no language was detected")
            return False

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

def check_biography(self):
    biography = self['user']['biography']
    if biography != None:
        #check if hebrew
        if get_lang(biography) !=False:
            if words_in_string(words_he, biography):
                self.is_selebgram = True
                print("found in biography")
            elif words_in_string(words_he, self.user['full_name']):
                self.is_selebgram = True
                print("found in full name")
            else:
                self.is_selebgram = False
                print("no selebgram")
    else:
        print("no biography or full name found , checking user_media")
        i = 0
        user_media = self['user']['media']['nodes']
        for c in user_media:
            caption = c[i]['caption']
            if words_in_string(words_he, caption):
                print("found in caption")
                self.is_selebgram = True
            else:
                i += 1
        self.is_selebgram = False

