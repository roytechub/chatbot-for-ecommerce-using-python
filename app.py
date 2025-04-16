from flask import Flask, render_template, request, jsonify
from chat import get_response

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/product')  # <--- NEW ROUTE
def product():
    print("✅ /product route was hit")
    return render_template('product.html')



@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    #Todo : Checking if the text is valid
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)

if __name__=="__main__":
    app.run(debug=True)