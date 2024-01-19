from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates', methods=['POST'])
def register():
    first_name = request.form.get('depan')
    last_name = request.form.get('belakang')
    seluler = request.form.get('seluler')
    tanggal = request.form.get('tanggal')
    bulan = request.form.get('bulan')
    tahun = request.form.get('tahun')
    gender = request.form.get('gender')

    return render_template('db.html', first_name=first_name, last_name=last_name,
                           seluler=seluler, tanggal=tanggal, bulan=bulan, tahun=tahun, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)
