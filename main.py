from time import sleep, time

import sys

from get_user_feed import get_user_feed
from instabot.instabot import InstaBot
from new_auto_mod_like2 import new_auto_mod_like2
from new_auto_mod_likeall import new_like_all_exist_media
from recent_feed import get_media_id_recent_feed
from user_feed import get_media_id_user_feed
from user_info import get_user_info

bot = InstaBot(
    login="julietmiler",
    password="Choya1985",
    like_per_day=500,
    comments_per_day=0,
    tag_list=['חתונה', 'מאורסת', 'israel', 'makeupaddict', 'איפורכלה', 'מתחתנת' ,'איפור'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=10,
    follow_time=1 * 60,
    unfollow_per_day=300,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your"],
                  ["photo", "picture", "pic", "shot", "snapshot"],
                  ["is", "looks", "feels", "is really"],
                  ["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])


def like1(self, list):
    log_string = "Trying to like media: %s" % \
                 (list['node']['id'])
    print(log_string)
    like = self.like(list['node']['id'])
    # self.comment(self.media_by_tag[i]['id'], 'Cool!')
    # elf.follow(self.media_by_tag[i]["owner"]["id"])
    if like != 0:
        if like.status_code == 200:
            # Like, all ok!
            self.error_400 = 0
            self.like_counter += 1
            log_string = "Liked: %s. Like #%i." % \
                         (list['node']['id'],
                          self.like_counter)
            self.write_log(log_string)
        elif like.status_code == 400:
            log_string = "Not liked: %i" \
                         % (like.status_code)
            self.write_log(log_string)
            # Some error. If repeated - can be ban!
            if self.error_400 >= self.error_400_to_ban:
                # Look like you banned!
                sys.exit()
                #time.sleep(self.ban_sleep_time)
            else:
                self.error_400 += 1
        else:
            log_string = "Not liked: %i" \
                         % (like.status_code)
            self.write_log(log_string)
            return False

def get_feed(self):
    while True:
        get_media_id_recent_feed(self)
        for d in self.media_on_feed:
            feed = {}
            media_preview_like = d['node']['edge_media_preview_like']
            media_preview_comment = d['node']['edge_media_preview_like']
            media_tagged_user = d['node']['edge_media_to_tagged_user']['edges']
            madia_caption = d['node']['edge_media_to_caption']
            owner = d['node']['owner']['username']
            location = d['node']['location']
            media_id = d['node']['id']
            #get the owner from media and evaluate it, if high score like users's media.
            self.user_score = get_user_info(self, owner)
            if self.user_score >=100:
                get_user_feed(self, owner)
                num_likes = self.user_score // 50
                new_like_all_exist_media(self, num_likes)
            #get all user which liked the media and evaluate score, user with high score get to self.bot_follow_list
            for media in media_preview_like['edges']:
                self.user_score = get_user_info(self, media['node']['username'])
                if self.user_score >= 100:
                    self.bot_follow_list.append(media['username'])
                    new_like_all_exist_media(self, num_likes)

            return



            #get_media_id_user_feed(bot, user_name)
            # get_user_info(bot, user_name)


def main():
    get_feed(bot)
    #comment(self.bot_comment_list)
    new_auto_mod_like2(bot)
            # print(FindMostPopularAccountByTags(bot, TAGS, 5).get_all_media_by_tag(TAGS[1]))

if __name__ == '__main__':
    main()








    
'''

def like_all(self):
    for i in self.media_id:
        like = self.like(i)
        # self.comment(self.media_by_tag[i]['id'], 'Cool!')
        # elf.follow(self.media_by_tag[i]["owner"]["id"])
        if like != 0:
            if like.status_code == 200:
                # Like, all ok!
                self.error_400 = 0
                self.like_counter += 1
                log_string = "Liked: %s. Like #%i." % (i, self.like_counter)
                self.write_log(log_string)
            elif like.status_code == 400:
                log_string = "Not liked: %i" % (like.status_code)
                self.write_log(log_string)
                # Some error. If repeated - can be ban!
                if self.error_400 >= self.error_400_to_ban:
                    # Look like you banned!
                    time.sleep(self.ban_sleep_time)
                else:
                    self.error_400 += 1
            else:
                log_string = "Not liked: %i" % (like.status_code)
                self.write_log(log_string)
                return False
                # Some error.
'''