class FindMostPopularAccountByTags(object):
    def __init__(self, ai, tags_list, limit):
        self.ai = ai
        self.tag_name = tags_list
        self.limit = limit
        self.popularity ={}

    def get_all_media_by_tag(self, tag):
        self.ai.get_media_id_by_tag(tag)
        return self.ai.media_by_tag