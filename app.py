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
        
        searchquery = site+spacequery
        client = uReq(searchquery)
        soup3 = BeautifulSoup(client.read(), 'html.parser')
        links = []
        for link in soup3.find_all("img", {"class": "z_h_c z_h_e"}):
            try:
                imageLink = link['src']
                links.append(imageLink)
            except:
                imageLink = None    
        images_names = []
                

        # for index,img_link in enumerate(links):
        #             img_data = rq.get(img_link).content
        #             my_dict = {'image':img_data,'imagelink':img_link}
        #             db[dbname].insert(my_dict) 
        #             images_names.append(my_dict)

        print(links)
                   
        return render_template('results1.html',links=links)
        
    else:
        return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)        