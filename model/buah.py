import uuid
from conf.db import db

def m_getBuahAll():
    buah = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_buah")
    hasil = cursor.fetchall()
    for x in hasil:
        bRecord = {'kd':x[1],'nama':x[2], 'stok':x[3], 'harga':x[4]}
        buah.append(bRecord)
    return buah

def m_createBuah(nama, harga, stok):
    try:
        cursor = db.cursor()
        kd_buah = uuid.uuid4()
        sql = "INSERT INTO tbl_buah (id, kd_buah, nama_buah, harga, stok) VALUES (null,%s,%s,%s,%s);"
        val = (str(kd_buah), nama, harga, stok)
        cursor.execute(sql, val)
        db.commit()
        return True
    except:
        return False
   