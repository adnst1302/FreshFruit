from flask import Flask, request, jsonify 
from controller.buah import *
from controller.stockMasuk import *

app = Flask(__name__)

@app.route('/')
def index():
    dr = {'content' : 'Fresh fruit page API'}
    return jsonify(dr)

# ROUTE BUAH 
@app.route('/buah/data/all')
def buahDataAll():
    return c_dataBuahAll()
    
@app.route('/buah/tambah', methods=('GET', 'POST'))
def buahTambah():
    return c_tambahBuah(request)

@app.route('/buah/hapus', methods=('GET', 'POST'))
def buahHapus():
    return c_hapusBuah(request)

@app.route('/buah/update', methods=('GET', 'POST'))
def buahUpdate():
    return c_updateBuah(request)

# ROUTE STOCK MASUK 
@app.route('/stock-masuk/data/all')
def stockMasukDataAll():
    return c_stockMasukAll()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001)


