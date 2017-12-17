#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import random
import time

from get_lang import get_lang

words_he = ['איפור', 'מאפרת', 'ומאפרת', 'מעצבת שיער', 'מעצבת שיער', 'חתונה' ,'לכלות',  'שמלת כלה', 'כלה']
words_en = [ 'makeup', 'Makeup', 'bridal', 'woman', 'israel']

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
                score += check_biography(biography)
                if media > 100:
                    score += 30
                if 'he' in get_lang(full_name):
                    score += 30
                if follower > follows:
                    score += 40
                if follow_viewer == True:
                    score += 30
                if follow_viewer:
                    score += 20
                else:
                    score += 50
                score += posts_weight(user_info['user']['media']['nodes'])
                self.user_score = score
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

def check_biography(biography):
    if biography == None:
        return 0
    elif words_in_string(words_he, biography):
        return 100
    elif words_in_string(words_en, biography):
        return 50
    else:
        return 0


def posts_weight(self):
   for d in self:
       score= 0
       com_count = d['comments']['count']
       like_count = d['likes']['count']
       #if number of comments is high, raise score
       if com_count >= 5:
           self.recommend_comment = True
           score += com_count * 3
       else:
           score += com_count
       if like_count <= 180:
           score += 30
       elif like_count > 180 <= 1000:
           score += 20
       elif like_count > 1000:
           self.recommend_comment = True
           score += 10
       if words_in_string(words_he, d['caption']):
           score += 10
           return score

