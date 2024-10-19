from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# application instance
app = Flask(__name__)

mongodb_client = MongoClient("mongodb+srv://c0917581:2U8jcNKS2WpYWu13@mobile.vpqup.mongodb.net/?retryWrites=true&w=majority&appName=Mobile")
# mongodb+srv://c0917581:<db_password>@mobile.vpqup.mongodb.net/?retryWrites=true&w=majority&appName=Mobile
#to access database from the client
db = mongodb_client["app"]
products_collection = db["products"]
# password and username
# c0917581:2U8jcNKS2WpYWu13

# Access the environment variables
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

mock_datat =[{"name":"HP","tag":"new","price":399.99,"image_path":"/static/images/product1.jpg"},
             {"name":"DELL","tag":"new","price":499.99,"image_path":"/static/images/product2.jpg"}]
# products_collection.insert_many(mock_datat)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    products = list(products_collection.find())
    return render_template("products.html", products=products)


app.run(host='0.0.0.0', port=5000)