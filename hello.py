#import flask module
from flask import Flask, render_template, request

#create an instance of the Flask class
app = Flask(__name__, template_folder='views')

#define route for the root Url
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #proses data form di sini
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']

        #tampilkan pada terminal
        print(f'Nama: {nama}, Email: {email}, Pesan: {pesan}')

    title = 'Contact Page'
    return render_template('contact.html', title=title)

@app.route('/pmb', methods=['GET', 'POST'])
def pmb():
    if request.method == 'POST':
        # Proses data form di sini
        nama = request.form['nama']
        email = request.form['email']
        tempatlahir = request.form['tempat_lahir']
        tanggallahir = request.form['tanggal_lahir']
        asal_sma = request.form['asal_sma']
        no_hp = request.form['nomor']
        foto = request.files['foto']

        # Upload foto ke folder 'uploads'
        foto.save(f'static/uploads/{foto.filename}')

        # Tampilkan di terminal
        print(f'Nama: {nama}, Email: {email}, Tempat Lahir: {tempatlahir}, Tanggal Lahir: {tanggallahir}, Asal SMA: {asal_sma}, No HP: {no_hp}, Foto: {foto.filename}')

    title = 'Penerimaan Mahasiswa Baru'
    return render_template('pmb.html', title=title)

#run the app
if __name__== '__main__':
    app.run(debug=True)