from models import Model
from models.blog import Blog
from models.blog import Comment
from models.todo import Todo


class User(Model):
    @classmethod
    def find_all(cls):
        return cls.all()

    @staticmethod
    def salted_password(password, salt='$/i3& f*~^k'):
        import hashlib
        hash1 = hashlib.sha256(password.encode('ascii')).hexdigest()
        hash2 = hashlib.sha256((hash1 + salt).encode('ascii')).hexdigest()
        return hash2

    def __init__(self, form):
        # super(Model, self).__init__()
        self.id = form.get('id')
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.role = 10

    @classmethod
    def validate_login(cls, form):
        ul = cls(form)
        b = None
        ul.password = cls.salted_password(ul.password)
        us = cls.all()
        for u in us:
            if u.username == ul.username and u.password == ul.password:
                b = u
                break
        return b

    @classmethod
    def validate_register(cls, form):
        ur = cls(form)
        us = cls.all()
        ur.password = cls.salted_password(ur.password)
        for u in us:
            if u.username == ur.username:
                return None
        return ur.save()

    def todos(self):
        return Todo.find_all(self.id)

    def blogs(self):
        return Blog.find_all(self.id)

    def comments(self):
        return Comment.find_all(self.id)

    def others(self):
        ms = self.all()
        u = None
        for m in ms:
            if m.id == self.id:
                u = m
        ms.remove(u)
        return ms
