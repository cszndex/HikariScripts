from flask import Flask, render_template, request, redirect, url_for, g, flash, abort, jsonify, make_response
from datetime import datetime, timedelta, timezone
from bs4 import BeautifulSoup
import requests
import base64
import hashlib
import time
import socket
import threading
import random
import string
import os
import re

#App Handler
app = Flask(__name__)
app.config['SECRET_KEY'] = "nova"
app.config.update(
  SESSION_COOKIE_SECURE=True,
  SESSION_COOKIE_HTTPONLY=True,
  SESSION_COOKIE_SAMESITE='Lax',
)

#Error Handler
@app.errorhandler(404)
def notfound(e):
  return "No Found"

def tool_extract_hwid(url):
  match = re.search(r'HWID=([\w\d]+)', url)
  return match.group(1) if match else None
def tool_bypass(hwid):
  Base_Url = f"https://fluxteam.net/android/checkpoint/start.php?HWID={hwid}"
  Referrer = {
    'Referer': "https://linkvertise.com/",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
  }
  session = requests.Session()
  session.get(Base_Url, headers={'Referer': "https://fluxteam.net/"})
  time.sleep(1)
  session.get('https://fluxteam.net/android/checkpoint/check1.php', headers=Referrer)
  time.sleep(1)
  response = session.get("https://fluxteam.net/android/checkpoint/main.php", headers=Referrer)
  time.sleep(1)
  soup = BeautifulSoup(response.text, 'html.parser')
  body_code = soup.select_one('body > main > code').get_text()
  key = re.sub(r'\s+', '', body_code)
  return key

#Routes Handler
@app.route('/', methods=["GET", "POST"])
def home():
  generatedKey = None
  referer = request.headers.get('Referer')
  fhwid = request.cookies.get('fhwid')
  
  if request.method == "POST":
    form = request.form.get("fluxus_url")
    extracted = tool_extract_hwid(form)
    if extracted:
      resp = make_response(render_template('redirect.html'))
      resp.set_cookie("fhwid", extracted)
      return resp 
  if referer == "https://linkvertise.com/" and fhwid:
    generatedKey = tool_bypass(fhwid)
    timeNow = datetime.now()
    expiration = timeNow + timedelta(hours=24)
    expirationStr = expiration.strftime("%B %d, %Y %I:%M %p")
    return render_template("home.html", generatedKey=generatedKey, expirationStr=expirationStr)
  
  return render_template('home.html', generatedKey=generatedKey)

@app.route('/tos')
def tos():
  return render_template("tos.html")