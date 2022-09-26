from os import stat
from flask import jsonify 
from model.buah import *
from helper.response import *

class baseResponse:
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def buildResponse(self):
        dr = {'status':self.status, 'message':self.message}
        return jsonify(dr)

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
            setBaseResponse(200, 'fruit create succesfully')     
        else:
            setBaseResponse(400, 'error connection to database')
    except:
        setBaseResponse(400, 'error request format')
    baseResponse.buildResponse()

def setBaseResponse(status, message):
    newBasicResponse = baseResponse(status, message)