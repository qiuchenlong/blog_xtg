# coding=utf-8


class LoginUser(dict):
        # self['id'] = None
        # self['name'] = None
        # self['avatar'] = None

    def __init__(self, user):
        super(LoginUser, self).__init__()
        if isinstance(user, dict):
            self.update(user)

    # def add_message(self, message):
    #     if 'messages' not in self:
    #         self['messages'] = [message]
    #     else:
    #         self['messages'].append(message)
    #
    # def read_messages(self):
    #     all_messages = self['messages']
    #     self['messages'] = None
    #     return all_messages
