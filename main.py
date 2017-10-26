

from FindMostPopularAccountByTag import FindMostPopularAccountByTags
from feed_scanner import feed_scanner
from feed_scanner_Like import scan_feed
from instabot.instabot import InstaBot

USERNAME = "julietmiler"
PASSWORD =  "Choya1985"
TAGS = ['wedding', 'חתונה']


def main():
    bot = InstaBot(USERNAME, PASSWORD, tag_list=['wedding', 'חתונה'])
    #print(FindMostPopularAccountByTags(bot, TAGS, 5).get_all_media_by_tag(TAGS[1]))
    feed_scanner(bot)



if __name__ == '__main__':
    main()