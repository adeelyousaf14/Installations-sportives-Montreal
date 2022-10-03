from typing import List
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template
from flask import Response
from .database import Patinoire, Glissades
from dict2xml import dict2xml
import requests
import xml.etree.cElementTree as ET
from .database import Piscines, Glissades, Patinoire
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from csv import reader
main = Blueprint('main', __name__)


def A1():
    url_1 = ('https://data.montreal.ca/dataset/'
             '4604afb7-a7c4-4626-a3ca-e136158133f2/resource/'
             'cbdca706-569e-4b4a-805d'
             '-9af73af03b14/download/piscines.csv')
    url_2 = ('https://data.montreal.ca/dataset/225ac315-49fe'
             '-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def'
             '-903f-db24408bacd0/download/l29-patinoire.xml')
    url_3 = ('http://www2.ville.montreal.qc.ca/services_citoyens'
             '/pdf_transfert/L29_GLISSADE.xml')
    permission_url1 = requests.get(url_1, allow_redirects=True)
    permission_url2 = requests.get(url_2, allow_redirects=True)
    permission_url3 = requests.get(url_3, allow_redirects=True)
    if permission_url1.status_code == 200 or permission_url2.status_code == 200 or permission_url3.status_code == 200:
        with open('piscines.csv', 'wb') as f:
            f.write(permission_url1.content)
        with open('l29-patinoire.xml', 'wb') as f:
            f.write(permission_url2.content)
        with open('L29_GLISSADE.xml', 'wb') as f:
            f.write(permission_url3.content)
        return True
    else:
        return False




@main.route('/', methods=['GET', 'POST'])
def A5():

    if request.method == 'GET':
        return render_template("index.html", lis=[])
    elif request.method == 'POST':
        ar = request.form.get("arrondissement")
        print(ar)
        if ar:
            p = list(
                Patinoire.query.filter(
                    Patinoire.ARRONDISSEMENT == ar).all())
            format = [
                f"{str(i).split(':')[0]}:{str(i).split(':')[1]}:{str(i).split(':')[2]}" for i in p]
            print(format)
            return render_template("index.html", data=format)


# Func A3


@main.route('/doc', methods=['GET', 'POST'])
def A3():
    return render_template("doc.html")


# Function A4 et C2
@main.route('/api/installations', methods=['GET'])
def A4():
    if request.method == 'GET':
        arrondissement = request.args.get('arrondissement')
        year = request.args.get('year')
        if arrondissement:
            p = list(
                Patinoire.query.filter(
                    Patinoire.ARRONDISSEMENT == arrondissement).all())
            list_of_dicts = [i.__dict__ for i in p]
            for i in list_of_dicts:
                i.pop('_sa_instance_state')
            return jsonify(list_of_dicts)
        if year:
            p = list(Glissades.query.filter().all())
            root = ET.Element("root")
            for i in p:
                if i.ANNEE == year:
                    ET.SubElement(root, "glissade",
                                  id=str(i.ID),
                                  arrondissement=str(i.ARRONDISSEMENT),
                                  annee=str(i.ANNEE),
                                  date=str(i.DATE),
                                  heure=str(i.HEURE),
                                  nom=str(i.NOM)
                                  )
            return Response(dict2xml(root), mimetype='text/xml')


# Function C1
@main.route("/api/ajax", methods=['GET'])
def ajaxrep():
    year = request.args.get('year')
    if year:
        p = list(Glissades.query.filter().all())
        toRet = {year: [str(i).split(":")[1] for i in p if year in str(i)]}
        xml = str(dict2xml(toRet))
        print("ok")
        return Response(xml, mimetype='text/xml')
