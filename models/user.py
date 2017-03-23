from models import Model
from models.blog import Blog
from models.blog import Comment
from models.todo import Todo


class User(Model):
    @classmethod
    def find_all(cls):
        return cls.all()

    @staticmethod
    def salted_password(password, salt='$i3&f*k'):
        import hashlib
        hash1 = hashlib.sha256(password.encode('ascii')).hexdigest()
        hash2 = hashlib.sha256((hash1 + salt).encode('ascii')).hexdigest()
        return hash2

    def __init__(self, form):
        super(Model, self).__init__()
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.role = 10

    def validate_login(self):
        b = None
        # self.password = self.salted_password(self.password)
        us = User.all()
        for u in us:
            if u.username == self.username and u.password == self.password:
                b = u.id
                break
        return b

    def validate_register(self):
        us = User.all()
        # self.password = self.salted_password(self.password)
        for u in us:
            if u.username == self.username:
                return None
        return self.save()

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
