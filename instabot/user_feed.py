#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import time

from user_info import get_user_info


def get_media_id_user_feed(self, username):
    if self.login_status:
        if self.is_by_tag != True:
            log_string = "======> Get media id by user: %s <======" % (
                username)
            self.user_score = get_user_info(self, username)
            url = 'https://www.instagram.com/%s/?__a=1' % (username)
        else:
            log_string = "======> Get media id by Tag <======"
            url = 'https://www.instagram.com/explore/tags/%s/?__a=1' % (
                random.choice(self.tag_list))
        self.write_log(log_string)

        try:
            r = self.s.get(url)
            all_data = json.loads(r.text)

            if self.is_by_tag != True:
                self.media_by_user = list(all_data['user']['media']['nodes'])
            else:
                self.media_by_user = list(all_data['tag']['media']['nodes'])
            log_string = "Get media by user success!"
            self.write_log(log_string)
        except:
            self.media_by_user = []
            self.write_log("XXXXXXX Except on get_media! XXXXXXX")
            time.sleep(60)
            return 0
