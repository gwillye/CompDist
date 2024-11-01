import logging
from .basic_auth import auth
# from .model import Profile

class UserController:
    log = logging.getLogger()

    def get_user(self):
        current_user = auth.current_user()
        return current_user
        # Check if the user exist
        # user_db = Profile.query.filter(Profile.username == current_user)

        # Avoid error while checking the users in database
        # user_list = False
        # try:
        #     user_list = user_db.all()[0]
        # except IndexError:
        #     pass

        # if user_list:
        #     return user
