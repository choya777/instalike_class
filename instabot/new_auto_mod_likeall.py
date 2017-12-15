#likes some number of medias of the user, based on user_score

def new_like_all_exist_media(self):
    i = 0
    num_likes = self.user_score // 50
    # Media count by this user.
    l_c = self.media_by_user

    for i in range(num_likes):
        for d in l_c:
            log_string = "Trying to like media:" + str(d['id'])
            self.write_log(log_string)
            like = self.like(d['id'])
            if like != 0:
                if like.status_code == 200:
                    self.like_counter += 1
                    log_string = "Liked: %s. Media's Total Likes: %i." % \
                                 (self.media_by_user[i]['id'],
                                  self.media_by_user[i]['likes']['count'])
                    self.write_log(log_string)
                    num_likes -= 1
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
            break
    else:
        print('liked media of user: %i' % (num_likes))
        return True
