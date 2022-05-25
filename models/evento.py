from utils.db import db

class Evento(db.Model):
    eve_id = db.Column(db.Integer, primary_key=True)
    eve_codigo = db.Column(db.Integer,nullable=False)
    eve_nombre = db.Column(db.String(80), nullable=False)
    eve_entradas = db.Column(db.Integer, nullable=False)
    eve_fecha = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, eve_codigo, eve_nombre, eve_entradas, eve_fecha):
        self.eve_codigo = eve_codigo
        self.eve_nombre = eve_nombre
        self.eve_entradas = eve_entradas
        self.eve_fecha = eve_fecha