from flask import Flask, redirect, url_for, request, render_template,jsonify
import json
import pandas as pd

app = Flask(__name__)

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])

def generateResult(datainput) :
   global df
   data = pd.read_csv('data.csv')
   for i in range(89):
      s = 0
      for j in range(5):
         if data.iloc[i,j] == datainput[str(j)]:
               s = s+1
      data.loc[i,'Score'] = s
   df = data.sort_values(by=['Score'],ascending=False).head(5)
   print(df.values.tolist())

@app.route('/results', methods = ['GET'])
def result():
   # return render_template('RecommendationPage.html')
   return render_template('RecommendationPage.html', data=df.values.tolist())

@app.route('/receiver',methods = ['POST'])
def ress():
   rf = request.form
   for key in rf.keys():
      data = key
   data = json.loads(data)
   generateResult(data)
   # resp_dic = {'Hell':"hs"}
   # resp = jsonify(resp_dic)
   # resp.headers['Access-Control-Allow-Origin']='*'
   return redirect(url_for('result'))
   

@app.route('/sad',methods = ['GET'])
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True, port=5000)

   