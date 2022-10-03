from flask import Blueprint, request, render_template, redirect
from flask_expects_json import expects_json
from flask.helpers import url_for
from .database import Glissades, Users
from . import db

other = Blueprint('other', __name__)
glissadeSetShema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "cle": {"type": "string"},
        "date_maj": {"type": "string"}
    },
    "required": ["name"]
}


# Function A3
@other.route("/doc")
def A3():
    return render_template("doc.html")


# function D1
@other.route("/api/setglissade", methods=["POST"])
@expects_json(glissadeSetShema)
def setglisade():
    r = request.get_json()
    glissade = Glissades.query.filter_by(NAME=r["name"]).first()
    if glissade:
        if "cle" in r:
            glissade.CLE = r["cle"]
        if "date_maj" in r:
            glissade.DATE_MAJ = r["date_maj"]
        db.session.commit()
        return "ok"
    return "none"


# la Function D2
@other.route("/api/delglissade/<int:idg>", methods=["GET"])
def delGlissade(idg):
    toDel = Glissades.query.filter_by(id=idg).first()
    if toDel:
        retValue = f"{toDel.NAME} Deleted!"
        db.session.delete(toDel)
        db.session.commit()
        return retValue

    return "None"
