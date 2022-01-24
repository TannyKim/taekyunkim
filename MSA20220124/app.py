from flask import Flask, redirect
import json
import requests
import pandas as pd


app = Flask(__name__)

@app.route("/") 
def FlaskLab(): 
    return "Flask 데이터를 응답합니다" 

@app.route("/data1")
def FlaskData(): 
    keyValue = r"wtiiIXr9QnvUtWgl%2BVvLU3WpIOX3gJF4Ff9TZ4ZhLx12DzQPEtgxzTa2z%2F3GypeDAlnciIl7zR29ya7bdqtH7A%3D%3D"   

    dataURL = "http://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond" + "%5BorgZipaddr%3A%3ALIKE%5D=%EC%9D%80%ED%8F%89%EA%B5%AC"
    dataURL += "&serviceKey=" + keyValue
    
    dataResult = requests.get(dataURL).json()
    
    with open("mydatas.json", "w", encoding="utf-8") as writeFile:
        json.dump(dataResult, writeFile, ensure_ascii=False, indent=4)

    return redirect(dataURL)

with open("mydatas.json", "rb") as jsonFile:
    tempData = json.load(jsonFile)
