from flask import Flask, render_template, request, jsonify
import os
import json 
import requests as rq
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/photos', methods=['GET','POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':

        query =str(request.form['image'])
        #n_images = int(request.form['number'])

        site = "https://www.shutterstock.com/search/"

        
        searchquery = site+query
        print(searchquery)

        client = uReq(searchquery)

        #r2 = rq.get(searchquery).text

        soup3 = BeautifulSoup(client.read(), 'html.parser')

        links = []
        for link in soup3.find_all("img", {"class": "z_h_c z_h_e"}):
            imageLink = link['src']
            links.append(imageLink)



        
        


        return render_template('results.html',result=links)

    return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)        