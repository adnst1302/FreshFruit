from flask import jsonify 
from model.stockMasuk import *
from helper.response import *

def c_stockMasukAll():
    dr = {'status':200}
    return jsonify(dr)