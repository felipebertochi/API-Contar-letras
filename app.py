from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def contagem_letras():
    if request.method == 'POST':
        palavra_frase = request.form['palavra_frase']
        contagem_letras = {}

        for letra in palavra_frase:
            if letra.isalpha():
                letra = letra.lower()
                contagem_letras[letra] = contagem_letras.get(letra, 0) + 1
        return render_template('index.html' , contagem_letras = contagem_letras)
    return render_template('index.html')

if __name__  == '__main__':
    app.run(debug=True)
