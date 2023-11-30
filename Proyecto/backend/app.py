import matplotlib
from flask import Flask, render_template, jsonify, request
import json
import io
import matplotlib.pyplot as plt
from io import BytesIO
import base64

#Se cambia el matplotlib para usar un backend que no requiera un bucle principal
matplotlib.use('Agg')  #'Agg' es un backend no interactivo

def graficoGeneros(conteos): #Genera el grafico para los generos
    categorias = ["pop", "rap", "rock", "latin", "r&b", "edm"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Generos')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

def graficoSubPop(conteos): #Genera el grafico para los subgeneros de pop
    categorias = ["dance pop", "indie poptimism", "post-teen pop","electropop"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Subgeneros pop')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

def graficoSubRap(conteos): #Genera el grafico para los subgeneros de rap
    categorias = ["hip hop","southern hip hop", "gangster rap", "trap"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Subgeneros Rap')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

def graficoSubRock(conteos): #Genera el grafico para los subgeneros de rock
    categorias = ["classic rock","album rock", "permanent wave", "hard rock"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Subgeneros Rock')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

def graficoSubLatin(conteos): #Genera el grafico para los subgeneros de latin
    categorias = ["tropical","latin pop", "reggaeton", "latin hip hop"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Subgeneros Latin')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

def graficoSubRB(conteos): #Genera el grafico para los subgeneros de r&b
    categorias = ["urban contemporary","new jack swing", "neo soul", "hip pop"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Subgeneros R&B')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

def graficoSubEDM(conteos): #Genera el grafico para los subgeneros de edm
    categorias = ["electro house","big room", "pop edm", "progressive electro house"]
    datos = [conteos[categoria] for categoria in categorias]

    plt.bar(categorias, datos)
    plt.xlabel('Subgeneros EDM')
    plt.ylabel('Cantidad de canciones')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    imagen_codificada = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return imagen_codificada

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obtener_grafico_generos')
def obtener_grafico_generos():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()

    tipoGrafico = request.args.get('tipo', 'bar')

    conteosG = {
        "pop": 0,
        "rap": 0,
        "rock": 0,
        "latin": 0,
        "r&b": 0,
        "edm": 0,
    }

    for linea in datos:
        if linea["playlist_genre"] in conteosG:
            conteosG[linea["playlist_genre"]] += 1

    imagen_codificada = graficoGeneros(conteosG)
    return jsonify({"imagen_codificada": imagen_codificada})

@app.route('/obtener_grafico_subgenerospop')
def obtener_grafico_subgenerosP():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()

    tipoGrafico = request.args.get('tipo', 'bar')
    
    #subgeneros pop
    conteosSubP = {
        "dance pop": 0,
        "indie poptimism":0,
        "post-teen pop":0,
        "electropop":0
    }

    for linea in datos:
        if linea["playlist_subgenre"] in conteosSubP:
            conteosSubP[linea["playlist_subgenre"]] += 1

    imagen_codificada = graficoSubPop(conteosSubP)
    return jsonify({"imagen_codificada": imagen_codificada})

@app.route('/obtener_grafico_subgenerosrap')
def obtener_grafico_subgenerosRap():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()
    
    tipoGrafico = request.args.get('tipo', 'bar')
    
    #subgeneros rap
    conteosSubRap = {
        "hip hop": 0, 
        "southern hip hop": 0,
        "gangster rap": 0,
        "trap": 0
    }
       
    for linea in datos:
        if linea["playlist_subgenre"] in conteosSubRap:
            conteosSubRap[linea["playlist_subgenre"]] += 1
            
    imagen_codificada = graficoSubRap(conteosSubRap)
    return jsonify({"imagen_codificada": imagen_codificada})

@app.route('/obtener_grafico_subgenerosrock')
def obtener_grafico_subgenerosRock():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()
    
    tipoGrafico = request.args.get('tipo', 'bar')
    
    #subgeneros rock
    conteosSubRock = {
        "classic rock": 0, 
        "album rock": 0,
        "permanent wave": 0,
        "hard rock": 0
    }
       
    for linea in datos:
        if linea["playlist_subgenre"] in conteosSubRock:
            conteosSubRock[linea["playlist_subgenre"]] += 1
            
    imagen_codificada = graficoSubRock(conteosSubRock)
    return jsonify({"imagen_codificada": imagen_codificada})

@app.route('/obtener_grafico_subgeneroslatin')
def obtener_grafico_subgenerosLatin():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()
    
    tipoGrafico = request.args.get('tipo', 'bar')
    
    #subgeneros latin
    conteosSubLatin= {
        "tropical": 0, 
        "latin pop": 0,
        "reggaeton": 0,
        "latin hip hop": 0
    }
       
    for linea in datos:
        if linea["playlist_subgenre"] in conteosSubLatin:
            conteosSubLatin[linea["playlist_subgenre"]] += 1
            
    imagen_codificada = graficoSubLatin(conteosSubLatin)
    return jsonify({"imagen_codificada": imagen_codificada})

@app.route('/obtener_grafico_subgenerosrb')
def obtener_grafico_subgenerosRB():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()
    
    tipoGrafico = request.args.get('tipo', 'bar')
    
    #subgeneros r&b
    conteosSubRB= {
        "urban contemporary": 0, 
        "new jack swing": 0,
        "neo soul": 0,
        "hip pop": 0
    }
       
    for linea in datos:
        if linea["playlist_subgenre"] in conteosSubRB:
            conteosSubRB[linea["playlist_subgenre"]] += 1
            
    imagen_codificada = graficoSubRB(conteosSubRB)
    return jsonify({"imagen_codificada": imagen_codificada})

if __name__ == '__main__':
    app.run(debug=True)
    

@app.route('/obtener_grafico_subgenerose')
def obtener_grafico_subgenerosEDM():
    archivoJson = open("data.json", "r")
    datos = json.load(archivoJson)
    archivoJson.close()
    
    tipoGrafico = request.args.get('tipo', 'bar')
    
    #subgeneros edm
    conteosSubEDM= {
        "electro house": 0, 
        "big room": 0,
        "pop edm": 0,
        "progressive electro house": 0
    }
       
    for linea in datos:
        if linea["playlist_subgenre"] in conteosSubEDM:
            conteosSubEDM[linea["playlist_subgenre"]] += 1
            
    imagen_codificada = graficoSubEDM(conteosSubEDM)
    return jsonify({"imagen_codificada": imagen_codificada})

if __name__ == '__main__':
    app.run(debug=True)
    
        
