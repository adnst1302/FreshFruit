from os import stat
from flask import jsonify 
from model.buah import *
from helper.response import *

def c_dataBuahAll():
    dataBuah = m_getBuahAll()
    br = buildResponse(200, 'load fruit data successfully', dataBuah)
    return jsonify(br)

def c_tambahBuah(request):
    try:
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']
        if m_createBuah(nama, harga, stok) == True:
            br = buildResponse(200, 'fruit create succesfully', None)
        else:
            br = buildResponse(200, 'error connection database', None)
    except:
        br = buildResponse(200, 'error request format', None)

    return jsonify(br)

def c_hapusBuah(request):
    try:
        kdBuah = request.form['kdBuah']
        if m_deleteBuah(kdBuah) == True:
            br = buildResponse(200, 'fruit delete succesfully', None)
        else:
            br = buildResponse(200, 'error connection database', None)
    except:
        br = buildResponse(200, 'error request format', None)
        
    return jsonify(br)