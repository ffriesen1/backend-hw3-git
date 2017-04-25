from google.appengine.ext import ndb

class BackendStorage(ndb.Model):
    sender = ndb.StringProperty()
    recipient = ndb.StringProperty()
    msg = ndb.TextProperty()
    msg_date = ndb.DateTimeProperty(auto_now_add=True)
    was_read = ndb.BooleanProperty(default=False)
    lat = ndb.FloatProperty(indexed=False)
    lng = ndb.FloatProperty(indexed=False)
    latlng = ndb.StringProperty()
    version = ndb.IntegerProperty()


def send_msg():
    sender = request.vars.sender
    recipient = request.vars.recipient
    msg = request.vars.msg
    # Now I have to insert the message.
    bs = BackendStorage()
    bs.sender = sender
    bs.recipient = recipient
    bs.msg = msg
    bs.put()
    return response.json("ok")

def get_msg_for_me():
    recipient = request.vars.recipient
    q = BackendStorage.query()
    q.filter(BackendStorage.recipient == recipient)
    res = []
    # Now let's read the data.
    for r in q.iter():
       res.append(dict(
           sender=r.sender,
           msg=r.msg,
           msg_date=r.msg_date,
       ))
    return response.json(dict(results=res))

def get_msg_thread():
    recipient = request.vars.recipient
    sender = request.vars.sender
    q = BackendStorage.query()
    q = q.filter(BackendStorage.recipient == recipient)
    q = q.filter(BackendStorage.sender == sender)
    q = q.order(BackendStorage.msg_date)
    res = []
    # Now let's read the data.
    for r in q.iter():
       res.append(dict(
           sender=r.sender,
           recipient=r.recipient,
           msg=r.msg,
           msg_date=r.msg_date,
       ))
    return response.json(dict(results=res))


