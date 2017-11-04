import random
import sys

import time

from FindMostPopularAccountByTag import FindMostPopularAccountByTags

from instabot.instabot import InstaBot

USERNAME = "julietmiler"
PASSWORD = "Choya1985"
TAGS = ['wedding', 'חתונה']


def main():
    bot = InstaBot(USERNAME, PASSWORD, tag_list=['wedding', 'חתונה'])

    bot.new_auto_mod()
    # print(FindMostPopularAccountByTags(bot, TAGS, 5).get_all_media_by_tag(TAGS[1]))


if __name__ == '__main__':
    main()


def new_auto_mod_feed(self):
    while True:
        # ------------------- Get media_id -------------------
        if len(self.media_on_feed) == 0:
            # chooses randomly - TODO: change according to weight.
            self.get_media_id_recent_feed()
            self.like_count = 0
            # have random max_like - TODO: change according to user weight
        # ------------------- Like -------------------
        self.new_auto_mod_like_feed()
        # ------------------- Follow -------------------
        # self.new_auto_mod_follow()
        # ------------------- Unfollow -------------------
        # self.new_auto_mod_unfollow()
        # ------------------- Comment -------------------
        # self.new_auto_mod_comments()
        # Bot iteration in 1 sec
        time.sleep(3)


def new_auto_mod_like_feed(self):
    if time.time() > self.next_iteration["Like"] and self.like_per_day != 0 \
            and len(self.media_on_feed) > 0:
        # You have media_id to like:
        if self.like_all_exist_media(media_size=1, delay=False):
            # If like go to sleep:
            self.next_iteration["Like"] = time.time() + \
                                          self.add_time(self.like_delay)
        # Del first media_id
        del self.media_on_feed[0]


def like_all_exist_media(self, media_size=-1):
    """ Like all media ID that have self.media_by_tag """

    if self.login_status:
        if self.is_by_tag:
            i = 0
            for d in self.media_by_tag:
                # Media count by this tag.
                if media_size > 0 or media_size < 0:
                    media_size -= 1
                    l_c = self.media_by_tag[i]['likes']['count']
                    if ((l_c <= self.media_max_like and
                                 l_c >= self.media_min_like) or
                            (self.media_max_like == 0 and
                                     l_c >= self.media_min_like) or
                            (self.media_min_like == 0 and
                                     l_c <= self.media_max_like) or
                            (self.media_min_like == 0 and
                                     self.media_max_like == 0)):
                        for blacklisted_user_name, blacklisted_user_id in self.user_blacklist.items():
                            if self.media_by_tag[i]['owner']['id'] == blacklisted_user_id:
                                self.write_log(
                                    "Not liking media owned by blacklisted user: "
                                    + blacklisted_user_name)
                                return False
                        if self.media_by_tag[i]['owner']['id'] == self.user_id:
                            self.write_log(
                                "Keep calm - It's your own media ;)")
                            return False
                        try:
                            caption = self.media_by_tag[i][
                                'caption'].encode(
                                'ascii', errors='ignore')
                            tag_blacklist = set(self.tag_blacklist)
                            if sys.version_info[0] == 3:
                                tags = {
                                    str.lower(
                                        (tag.decode('ASCII')).strip('#'))
                                    for tag in caption.split()
                                    if (tag.decode('ASCII')
                                        ).startswith("#")
                                }
                            else:
                                tags = {
                                    unicode.lower(
                                        (tag.decode('ASCII')).strip('#'))
                                    for tag in caption.split()
                                    if (tag.decode('ASCII')
                                        ).startswith("#")
                                }

                            if tags.intersection(tag_blacklist):
                                matching_tags = ', '.join(
                                    tags.intersection(tag_blacklist))
                                self.write_log(
                                    "Not liking media with blacklisted tag(s): "
                                    + matching_tags)
                                return False
                        except:
                            self.write_log(
                                "Couldn't find caption - not liking")
                            return False

                        log_string = "Trying to like media from tag: %s" % \
                                     (self.media_by_tag[i]['id'])
                        self.write_log(log_string)
                        like = self.like(self.media_by_tag[i]['id'])
                        # self.comment(self.media_by_tag[i]['id'], 'Cool!')
                        # elf.follow(self.media_by_tag[i]["owner"]["id"])
                        if like != 0:
                            if like.status_code == 200:
                                # Like, all ok!
                                self.error_400 = 0
                                self.like_counter += 1
                                log_string = "Liked: %s. Like #%i." % \
                                             (self.media_by_tag[i]['id'],
                                              self.like_counter)
                                self.write_log(log_string)
                            elif like.status_code == 400:
                                log_string = "Not liked: %i" \
                                             % (like.status_code)
                                self.write_log(log_string)
                                # Some error. If repeated - can be ban!
                                if self.error_400 >= self.error_400_to_ban:
                                    # Look like you banned!
                                    time.sleep(self.ban_sleep_time)
                                else:
                                    self.error_400 += 1
                            else:
                                log_string = "Not liked: %i" \
                                             % (like.status_code)
                                self.write_log(log_string)
                                return False
                                # Some error.
                            i += 1
        else:
            i = 0
            for d in self.media_on_feed:
                # Media count by this tag.
                if media_size > 0 or media_size < 0:
                    media_size -= 1
                    log_string = "Trying to like media from tag: %s" % \
                                 (self.media_on_feed[i]['node']['id'])
                    self.write_log(log_string)
                    like = self.like(self.media_on_feed[i]['node']['id'])
                    # self.comment(self.media_by_tag[i]['id'], 'Cool!')
                    # elf.follow(self.media_by_tag[i]["owner"]["id"])
                    if like != 0:
                        if like.status_code == 200:
                            # Like, all ok!
                            self.error_400 = 0
                            self.like_counter += 1
                            log_string = "Liked: %s. Like #%i." % \
                                         (self.media_on_feed[i]['node']['id'],
                                          self.like_counter)
                            self.write_log(log_string)
                        elif like.status_code == 400:
                            log_string = "Not liked: %i" \
                                         % (like.status_code)
                            self.write_log(log_string)
                            # Some error. If repeated - can be ban!
                            if self.error_400 >= self.error_400_to_ban:
                                # Look like you banned!
                                time.sleep(self.ban_sleep_time)
                            else:
                                self.error_400 += 1
                        else:
                            log_string = "Not liked: %i" \
                                         % (like.status_code)
                            self.write_log(log_string)
                            return False
                            # Some error.
                        i += 1
    else:
        self.write_log("No media to like!")
