from ferris import BasicModel
from google.appengine.ext import ndb


class Gift(BasicModel):
    name = ndb.StringProperty(required=True)
    total = ndb.IntegerProperty()

