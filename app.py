from flask import Flask, render_template, request, jsonify
import os
import json 
import requests as rq
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
print(APP_ROOT)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/photos', methods=['GET','POST'])  # This will be called from UI
def math_operation():
    if request.method == 'POST':

        query =str(request.form['image'])

        target = os.path.join(APP_ROOT,'static\\photos\\')
        target_folder = os.path.join(target, '_'.join(query.lower().split(' ')))
        print(target_folder)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            site = "https://www.shutterstock.com/search/"
            searchquery = site+query
            print(searchquery)
            client = uReq(searchquery)
            soup3 = BeautifulSoup(client.read(), 'html.parser')
            links = []
            for link in soup3.find_all("img", {"class": "z_h_c z_h_e"}):
                imageLink = link['src']
                links.append(imageLink)

            # image_data = []
            # for index,img_link in enumerate(links):
            #     img_data = rq.get(img_link).content
            #     image_data.append(img_data)  

            for index,img_link in enumerate(links):
                img_data = rq.get(img_link).content
                with open(target_folder+"/"+str(index+1)+'.jpg','wb+') as f:
                    f.write(img_data)


            return render_template('results.html',result=links)
        else:
            pass
    return render_template('index.html')    

if __name__ == '__main__':
    app.run(debug=True)        