import re
from flask import jsonify 
from model.buah import *

def __init__(self):
        self.c_name = "buah"

def c_dataBuahAll():
    dataBuah = m_getBuahAll()
    dr = {'status' : 'success', 'data':dataBuah}
    return jsonify(dr)

def c_tambahBuah(request):
    try:
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']

        if m_createBuah(nama, harga, stok) == True:
            dr = {'status' : 'success'}
        else:
            dr = {'status' : 'fail'}

    except:
        dr = {'status' : 'fail'}
    
    return jsonify(dr)
