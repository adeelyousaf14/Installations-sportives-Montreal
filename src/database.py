from . import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    ARRONDISSEMENT = db.Column(db.String(200))

    def __repr__(self):
        return f"{self.id}:{self.email}:{self.ARRONDISSEMENT}"


class Piscines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NOM = db.Column(db.String(120), nullable=False)
    ARRONDISSE = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id}:{self.NOM}:{self.ARRONDISSE}"


class Glissades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(120))
    ARRONDISSEMENT = db.Column(db.String(120))
    CLE = db.Column(db.String(120))
    DATE_MAJ = db.Column(db.String(120))
    CONDITION = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id}:{self.NAME}:{self.ARRONDISSEMENT}:{self.DATE_MAJ}"


class Patinoire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(120))
    ARRONDISSEMENT = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.id}:{self.NAME}:{self.ARRONDISSEMENT}"
