#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import random
import time

from get_lang import get_lang

words_he = ['איפור', 'מאפרת', 'ומאפרת', 'מעצבת שיער', 'מעצבת שיער', 'חתונה' ,'לכלות',  'שמלת כלה', 'כלה']
words_en = [ 'makeup', 'Makeup', 'bridal']

def get_user_info(self, username):
    score = 0
    if self.login_status:
        now_time = datetime.datetime.now()
        log_string = "%s : Get user info \n%s" % (username, now_time.strftime("%d.%m.%Y %H:%M"))
        self.write_log(log_string)
        if self.login_status == 1:
            url = 'https://www.instagram.com/%s/?__a=1' % (username)
            try:
                r = self.s.get(url)
                user_info = json.loads(r.text)
                log_string = "Checking user info.."
                self.write_log(log_string)
                follows = user_info['user']['follows']['count']
                follower = user_info['user']['followed_by']['count']
                media = user_info['user']['media']['count']
                follow_viewer = user_info['user']['follows_viewer']
                followed_by_viewer = user_info['user']['followed_by_viewer']
                requested_by_viewer = user_info['user']['requested_by_viewer']
                has_requested_viewer = user_info['user']['has_requested_viewer']
                full_name = user_info['user']['full_name']
                biography = user_info['user']['biography']
                log_string = "Follower : %i" % (follower)
                self.write_log(log_string)
                log_string = "Following : %i" % (follows)
                self.write_log(log_string)
                log_string = "Media : %i" % (media)
                self.write_log(log_string)
                log_string = "Full Name : %s" % (full_name)
                self.write_log(log_string)
                #AI
                score = 0
                if follower < 10000:
                    score += follower // 100
                else:
                    score += follower // 1000
                score += check_biography(user_info, biography)
                if media > 100:
                    score += 30
                if 'he' in get_lang(full_name):
                    score += 30
                if follower > follows:
                    score += 40
                if follow_viewer == True:
                    score += 30
                self.user_score = score
                return self.user_score
            except:
                self.media_on_feed = []
                self.write_log("Except on get_info!")
                time.sleep(2)
                return 0
        else:
            return 0
    return score

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

def check_biography(self, biography):
    if biography == None:
        #get language of media caption
        for i in range(len(self['user']['media']['nodes'])):
            lang = get_lang(self['user']['media']['nodes'][i]['caption'])
            if 'he' in lang:
                return 30
    elif words_in_string(words_he, biography):
            return 100
    elif words_in_string(words_en, biography):
            return 50
    else:
            return 0

#def user_weight():

'''def post_weight(self):
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
                break
            else:
                i += 1
        self.is_selebgram = False
'''