from flask import Flask,jsonify, request,render_template
from flask_opensearch import FlaskOpenSearch
import os
import random
app = Flask(__name__,template_folder='templates')

app.config["OPENSEARCH_HOST"] = "localhost"
app.config["OPENSEARCH_USER"] = "admin"
app.config["OPENSEARCH_PASSWORD"] = "admin"

opensearch = FlaskOpenSearch(
    app=app,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)









'''@app.route('/createindex', methods=['GET'])
def create_index():
    connected = opensearch.ping()
    print(connected)  # True
    res_1 = opensearch.index("test")
    return 'created the index' '''

    






'''@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    title=request_data['title']
    director=request_data['director']
    year=request_data['year']
    id=request_data['id']
    res_3 = opensearch.index(
        "test-index",
        body={
            'title': title,
            'director': director,
            'year': year
        },
        id=id,
        refresh=True,
    )
    print(res_3)
    return jsonify({'response': 'response','message':'null','code':'Successfully inserted in Opensearch Index'})'''



@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data})

'''@app.route('/delete', methods = ['POST'])
def delete():
    if(request.method == 'POST'):
        res_4 = opensearch.delete(
        index="test-index",
        id="1",
    )
    print(res_4) 
    return jsonify({'response': 'response','message':'null','code':'Successfully deleted  in Opensearch Index'})'''



@app.route('/index',methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/north',methods = ['GET', 'POST'])
def north_kolkata():
    return render_template('north_kolkata.html')
    
@app.route('/south_kolkata',methods = ['GET', 'POST'])
def south_kolkata():
    return render_template('south_kolkata.html')


@app.route('/submit',methods=['POST'])
def submit():

    if request.method=='POST' :
        name=request.form.get('fname')
        print(name)
        phonenumber=request.form.get('phonenumber')
        address=request.form.get('address')
        print(phonenumber)
        email=request.form.get('email')
        id=random.randint(0,100000)
        print(name)

    
    res_3 = opensearch.index(
        "durgapuja-index",
        body={
            'name': name,
            'phonenumber': phonenumber,
            'address':address,
            'email': email
        },
        id=id,
        refresh=True,
    )
    print(res_3) 
    return f'Hello , {name} , {phonenumber},{id},{email} is submitted '
    
    

if __name__ == "__main__":
    app.run(debug=True,port=5500)
