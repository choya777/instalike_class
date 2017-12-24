

#likes some number of medias of the user, based on user_score
def new_like_all_exist_media(self, num_likes):
    i = 0
    # user's media
    for d in self.media_by_user:
        if i < num_likes:
            log_string = "Trying to like media:" + str(d['id'])
            self.write_log(log_string)
            like = self.like(d['id'])
            if like != 0:
                if like.status_code == 200:
                    self.like_counter += 1
                    log_string = "Liked: %s. Media's Total Likes: %i." % \
                                 (d['id'],
                                  d['likes']['count'])
                    i += 1
                elif like.status_code == 400:
                    log_string = "Not liked: %i" \
                                 % (like.status_code)
                    self.write_log(log_string)
                    break
                else:
                    log_string = "Not liked: %i" \
                                 % (like.status_code)
                    self.write_log(log_string)
                    return False
            else:
                break
