from oct_turrets.base import BaseTransaction
from oct_turrets.tools import CustomTimer
import random
import time
import requests


class Transaction(BaseTransaction):
    def __init__(self, config, context=None):
        super(Transaction, self).__init__(config, context)
        self.url = "http://prod.latech.io/inuk_api/"
        self.session = None


    def setup(self):
        """Setup data or objects here
        """
        self.session = requests.Session()


    def run(self):
        with CustomTimer(self, 'user page'):
            requests.get(self.url + "users")

        with CustomTimer(self, 'partners page'):
            requests.get(self.url + "partners")

    def tear_down(self):
        """Clear cache or reset objects, etc. Anything that must be done after
        the run method and before its next execution
        """
        self.session.close()


if __name__ == '__main__':
    trans = Transaction(None)
    trans.run()
    print(trans.custom_timers)
