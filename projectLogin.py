from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

    return render_template('db.html', nama_depan=nama_depan, nama_belakang=nama_belakang,
                           email_or_noHp=email_or_noHp, tanggal=tanggal, bulan=bulan, tahun=tahun, gender=gender, password=passwd)

if __name__ == '__main__':
    app.run(debug=True)
