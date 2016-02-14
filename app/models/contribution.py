from ferris import BasicModel
from google.appengine.ext import ndb
import pprint

class Contribution(BasicModel):
    gift = ndb.StringProperty(required=True)
    amount = ndb.IntegerProperty(required=True)

    @classmethod
    def collected(cls,gift_name):
        """
        Queries all contribution to the given Gift name
        """
        all_contributions = cls.find_all_by_gift(gift_name)
        donation = 0
        for i in all_contributions:
           donation = donation + i.amount
        return donation

