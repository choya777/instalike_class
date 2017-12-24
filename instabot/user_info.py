#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json
import random
import time

import sys

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
            #try:
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
            # AI
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
            if follow_viewer:
                score += 20
            else:
                score += 50
            posts_score = posts_weight(self, user_info['user']['media']['nodes'])
            if posts_score == None:
                print("post score none " + str(posts_score))
            else:
                score += posts_score
            print("user's score: " + str(score))
            return score
            #except:
                #print("Unexpected error:", sys.exc_info()[0])
                #self.media_on_feed = []
                #self.write_log("Except on get_info!")
                #time.sleep(2)
                #return 0
        else:
            return 0

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


def posts_weight(self, media_list):
    posts_score = 0
    try:
        for media in media_list:
            com_count = media['comments']['count']
            like_count = media['likes']['count']
            # if number of comments is high, raise score
            if com_count >= 5:
                self.bot_comment_sit.append(media['id'])
                posts_score += com_count
            else:
                posts_score += com_count
            if like_count <= 180:
                posts_score += 5
            elif like_count > 180 <= 1000:
                posts_score += 4
            elif like_count > 1000:
                self.bot_comment_sit = media['id']
                posts_score += 2
            if media['caption'] != None:
                words_in_string(words_he, media['caption'])
                posts_score += 2
            else:
                return 0
        return posts_score
    except:
        print("Unexpected error:", sys.exc_info()[0])


