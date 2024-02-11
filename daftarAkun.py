from flask import Flask, render_template, request
import json
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', database='siswa', port=3306)
db_cursor = db.cursor()

app = Flask(__name__)

with open('D:\produktif bu Tya\GUI LOGIN\launch.json', 'r') as dataJson:
    data = json.load(dataJson)

@app.route('/')
def index():
    return render_template('daftar.html', tanggal = data['tanggal'], bulan = data['bulan'], tahun = data['tahun'])

@app.route('/templates', methods=['POST'])
def register():
    nama_depan = request.form.get('depan')
    nama_belakang = request.form.get('belakang')
    email_or_noHp = request.form.get('seluler')
    passwd = request.form.get('password')
    tanggal = request.form.get('tanggal')
    bulan = request.form.get('bulan')
    tahun = request.form.get('tahun')
    gender = request.form.get('gender')
    
    sql = "INSERT INTO login(Nama_Depan,Nama_Belakang,Seluler, Password, Tanggal, Bulan,Tahun, Gender ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (nama_depan, nama_belakang, email_or_noHp, passwd, tanggal, bulan, tahun,gender)
    db_cursor.execute(sql, val)
    db.commit()
    
    return render_template('dbDaftar.html', depan=nama_depan, belakang=nama_belakang, seluler=email_or_noHp, password=passwd, 
                           tgl=tanggal, bln=bulan, thn=tahun, gender = gender)

if __name__ == '__main__':
    app.run(debug=True)