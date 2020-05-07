from flask import Flask
import MySQLdb

app = Flask(__name__)
conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='fenixmcs_user')
cursor=conn.cursor()