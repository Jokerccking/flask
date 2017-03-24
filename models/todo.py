import time

from models import Model


class Todo(Model):

    @classmethod
    def find_all(cls, uid):
        ums = []
        ms = cls.all()
        for m in ms:
            if m.uid == uid:
                ums.append(m)
        return ums

    # @classmethod
    # def tid(cls, i):
    #    ms = cls.all()
    #    td = None
    #    for m in ms:
    #        if m.id == i:
    #            td = m
    #            break
    #    return td

    def __init__(self, form):
        # super(Model, self).__init__()
        self.id = form.get('id')
        self.uid = int(form.get('uid'))
        self.content = form.get('content', '')
        self.ct = form.get('ct', int(time.time()))
        self.ut = form.get('ut', self.ct)
        self.completed = form.get('complete', False)

    def update(self, cnt):
        self.ut = int(time.time())
        self.content = cnt
        return self.save()

    def complete(self):
        self.completed = True
        return self.save()
