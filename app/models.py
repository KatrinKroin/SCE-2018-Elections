from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), index=True, unique=False)
    last_name = db.Column(db.String(120), index=True, unique=False)
    id_num = db.Column(db.String(9), index=True, unique=True)
    voted = db.Column(db.BOOLEAN, default=False, index=True, unique=False)

    def __init__(self, first_name, last_name, id_num):
        self.first_name = first_name
        self.last_name = last_name
        self.id_num = id_num
        self.voted = False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.first_name


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    picture = db.Column(db.String(120), index=True, unique=False)
    votes_amount = db.Column(db.Integer, index=True, unique=False)

    def __init__(self, name, picture):
        self.name = name
        self.picture = picture
        self.votes_amount = 0

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<Party %r>' % self.name
