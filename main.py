from instabot.instabot import InstaBot
from FindMostPopularAccountByTag import FindMostPopularAccountByTags

USERNAME = "avizetser"
PASSWORD =  "e7mc2rt457"
TAGS = ['cat', 'dog']


def main():
    ib = InstaBot(USERNAME, PASSWORD)
    print FindMostPopularAccountByTags(ib, TAGS, 5).get_all_media_by_tag(TAGS[1])

if __name__ == '__main__':
    main()