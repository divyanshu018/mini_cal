from flask import Flask,render_template,jsonify,request
import math


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template("Index.html")


@app.route("/math",methods=['POST'])
def math_operation():
    if(request.method=='POST'):
       ops= request.form['operation']
       num1=int(request.form["num1"])
       num2=int(request.form["num2"])
       if(ops=='add'):
           r=num1+num2
           result="The sum of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)
       
       if(ops=='subtract'):
           r=num1-num2
           result="The sub of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)

       if(ops=='multiply'):
           r=num1*num2
           result="The multiply of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)

       if(ops=='divide'):
           r=num1/num2
           result="The divide of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)

       if(ops=='log'):
           r=math.log(num1+num2)
           result="The lan of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)

       if(ops=='square_root'):
           r=math.sqrt(num1+num2)
           result="The sqrt of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)

       if(ops=='inverse_cosine'):
           r=math.acos(num1+num2)
           result="The lan of " + str(num1) + ' and '+ str(num2) +' is  : ' +str(r)
           return render_template("results.html",result=result)






if __name__=="__main__":
    app.run(host="0.0.0.0")