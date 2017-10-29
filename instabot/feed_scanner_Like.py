#!/usr/bin/env python
# -*- coding: utf-8 -*-
from recent_feed import get_media_id_recent_feed
from user_feed import get_media_id_user_feed

def scan_feed(self):
    #First the bot try to collect media id on your recent feed
    chooser = 0
    while chooser < len(self.media_on_feed):
        get_media_id_recent_feed(self)
        for chooser in range( 0, len(self.media_on_feed)):
            self.current_user = self.media_on_feed[chooser]["node"]["owner"]["username"]
            self.current_id = self.media_on_feed[chooser]["node"]["owner"]["id"]
            media_id = get_media_id_user_feed(self)
            print(media_id)
        return media_id




