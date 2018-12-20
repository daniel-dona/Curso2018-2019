#!/usr/bin/env python
# encoding: utf-8

from rdflib import Graph
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utm import to_latlon

from data import BicyPoint, Base


engine = create_engine('mysql://bicy:parking@db/bicyparking?charset=utf8', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def rdf_to_db():
    session = Session()

    graph = Graph()
    graph.load("aparcabicis-updated.rdf")

    ns_id = 'http://purl.org/dc/terms/'
    ns_type = 'http://www.semanticweb.org/group10/Propiedades#'

    for row in graph.query('SELECT ?instance WHERE {?instance rdf:type clase:Aparcamiento .}'):
        r = {}
        for p, o in graph.predicate_objects(row.instance):
            if str(p) == '{}identifier'.format(ns_id):
                r['identifier'] = o.value
            else:
                for prop in ['direccion', 'coordenadaX', 'coordenadaY']:
                    if str(p) == '{}{}'.format(ns_type, prop):
                        r[prop] = o.value.replace(',', '.')
        if r:
            lat, lng = to_latlon(float(r['coordenadaX']), float(r['coordenadaY']), 30, 'T')
            bicy_point = BicyPoint(
                id=int(r['identifier']),
                address=r['direccion'],
                lat=lat,
                lng=lng,
            )
            session.add(bicy_point)
            session.commit()


if __name__=='__main__':
    rdf_to_db()

