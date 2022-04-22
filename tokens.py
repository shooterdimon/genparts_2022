from prelog_msg import *
import time
import sys


class TokenList:
    counter = 0

    def __init__(self, *tokens_list):
        self.tokens = tokens_list
        self.active_token = self.tokens[0]

    def next_token(self):
        if self.counter < len(self.tokens)-1:
            self.counter += 1
        else:
            user_response = input(user_info + ' All tokens have been used. Do you want to start from begin (y/n)? ')
            if 'y' in user_response.lower():
                self.counter = 0
            else:
                print('Program has stopped. You can close the window or it will be automatically closed in 5 minutes')
                time.sleep(300)
                sys.exit(0)
        self.active_token = self.tokens[self.counter]

    def get_active_token(self):
        return self.active_token

    def get_token_order(self):
        return self.counter
