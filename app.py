from flask import Flask, render_template, request, jsonify
import os
import json 
import requests as rq
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import glob
import pymongo


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/photos', methods=['GET','POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':

        query =str(request.form['image'])
        spacequery=str(query.replace(" ","+"))
        dbname = query.replace(" ","")
        
        site = "https://www.shutterstock.com/search/"
        links = []

        for i in range(1,6):
            
            alternate_site = 'https://www.shutterstock.com/search/'+str(spacequery)+'?page='+str(i)
            
            client = uReq(alternate_site)
            
            soup3 = BeautifulSoup(client.read(), 'html.parser')
            
            for link in soup3.find_all("img", {"class": "z_h_9d80b z_h_2f2f0"}):
                try:
                    imageLink = link['src']
                    links.append(imageLink)
                except:
                    imageLink = None 

                   
                                
        return render_template('results1.html',links=links)
        
    else:
        return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)        