from flask import Flask, render_template

app = Flask(__name__)

Courses=[
{
'id':1,
'title':'Wedding photography',
'duration':'100 hours',
'fees':'Rs. 3000'
},
{
'id':2,
'title':'Portrait photography',
'duration':'80 hours',
'fees':'Rs. 2000'
},
{
'id':3,
'title':'Street photography',
'duration':'70 hours',
'fees':'Rs. 2500'
},
{
'id':4,
'title':'Product photography',
'duration':'100 hours',
'fees':'Rs. 3000'
},
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                          n=Courses)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)