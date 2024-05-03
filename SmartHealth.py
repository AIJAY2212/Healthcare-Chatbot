from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from werkzeug.utils import secure_filename
from werkzeug.utils import secure_filename
import mysql.connector
import sys
import pickle
import numpy as np
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from requests import get
from bs4 import BeautifulSoup
import os
from flask import Flask, render_template, request, jsonify


english_bot = ChatBot('Bot',
                      storage_adapter='chatterbot.storage.SQLStorageAdapter',
                      logic_adapters=[
                          {
                              'import_path': 'chatterbot.logic.BestMatch'
                          },

                      ],
                      trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)


'''bot= ChatBot('ChatBot')

trainer = ListTrainer(bot)





for file in os.listdir('C:/Users/Fantasy/PycharmProjects/MedicalChatBotPy/data/'):

    chats = open('C:/Users/Fantasy/PycharmProjects/MedicalChatBotPy/data/' + file, 'r').readlines()

    trainer.train(chats)'''

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/Home")
def Home():
    return render_template('index.html')
@app.route("/DoctorLogin")
def DoctorLogin():
    return render_template('DoctorLogin.html')

@app.route("/NewDoctor")
def NewDoctor():
    return render_template('NewDoctor.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')
@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')

@app.route("/CompanyLogin")
def CompanyLogin():
    return render_template('CompanyLogin.html')
@app.route("/NewCompany")
def NewCompany():
    return render_template('NewCompany.html')
@app.route("/Heart")
def Heart():
    return render_template('Heart.html')


@app.route("/ask", methods=['GET', 'POST'])
def ask():
    message = str(request.form['messageText'])
    bott=''
    bott1 = ''
    sresult1=''

    bot_response = english_bot.get_response(message)

    print(bot_response)


    word = 'appointment'



    if word in message :

        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')

        cur1 = conn1.cursor()
        cur1.execute(
            "SELECT  distinct  UserName  from  doctortb")
        data = cur1.fetchall()

        for item in data:

            greet = ' <p class="price">  Hello  Search Result </p> <br>'

            doct = ' <p class="price">  Please Select Your Doctor to this list </p> <br>'

            ss = '<a href="http://127.0.0.1:5000/fullInfo?pid='
            ss1 = item[0] + '">'
            ss2 = item[0]
            ss3='</a> <br>'







            bot_response = ss + ss1+ss2+ss3

            if (bott == ""):
                bott = bot_response
            else:
                bott = bott + bot_response

            print(bott)





        return jsonify({'status': 'OK', 'answer':greet+ doct+bott})










    while True:




        if bot_response.confidence > 0.1:

            bot_response = str(bot_response)
            print(bot_response)
            return jsonify({'status': 'OK', 'answer': bot_response})

        elif message == ("bye") or message == ("exit"):

            bot_response = 'Hope to see you soon' + '<a href="http://127.0.0.1:5000/UserHome">Exit</a>'

            print(bot_response)
            return jsonify({'status': 'OK', 'answer': bot_response})

            break



        else:

            try:
                url = "https://en.wikipedia.org/wiki/" + message
                page = get(url).text
                soup = BeautifulSoup(page, "html.parser")
                p = soup.find_all("p")
                return jsonify({'status': 'OK', 'answer': p[1].text})



            except IndexError as error:

                bot_response = 'Sorry i have no idea about that.'

                print(bot_response)
                return jsonify({'status': 'OK', 'answer': bot_response})

    # return render_template("index.html")

@app.route("/fullInfo")
def fullInfo():
    pid = request.args.get('pid')
    session['pid'] = pid



    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctortb where UserName='" + pid + "' ")
    data1 = cur.fetchall()

    return render_template('UserAppointment.html',data=data1 )


@app.route("/DoctorUserInfo")
def DoctorUserInfo():
    dname = session['dname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM apptb where DoctorName='"+ dname +"' ")
    data = cur.fetchall()

    return render_template('DoctorUserInfo.html', data=data )


@app.route("/DoctorAssignInfo")
def DoctorAssignInfo():

    dname = session['dname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM drugtb where DoctorName	='"+ dname +"'  ")
    data = cur.fetchall()

    return render_template('DoctorAssignInfo.html', data=data )



@app.route("/doclogin", methods=['GET', 'POST'])
def doclogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['dname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from doctortb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            data1='Username or Password is wrong'
            return render_template('goback.html', data=data1)


        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM doctortb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('DoctorHome.html', data=data)


@app.route("/searchid")
def searchid():
    user= request.args.get('user')
    session['user']=user
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute(
        "SELECT  *  FROM regtb where  username='"+str(user)+"'")
    data = cur.fetchall()
    print(data)



    return render_template('AdminAssign.html',data=data )



@app.route("/assigndrug", methods=['GET', 'POST'])
def assigndrug():
    if request.method == 'POST':

        uname = request.form['UserName']
        phone = request.form['Phone']
        email = request.form['Email']
        dname = session['dname']
        medi = request.form['Medicine']
        other = request.form['Other']
        file = request.files['file']
        file.save("static/upload/" + file.filename)
        Adate = request.form['Adate']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM drugtb ")
        data = cursor.fetchone()

        if data:
            mobile = data[4]

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO  drugtb VALUES ('','" + uname + "','" + phone + "','" + email + "','" + dname + "','" + medi + "','" + other + "','" + file.filename + "','" + Adate + "','','')")
            conn.commit()
            conn.close()








        # return 'file register successfully'
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM drugtb ")
        data = cur.fetchall()

    return render_template('DoctorAssignInfo.html', data=data)




@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        # return 'file register successfully'


    return render_template('UserLogin.html')







@app.route("/newdoctor", methods=['GET', 'POST'])
def newdoctor():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']
        special = request.form['special']

        uname = request.form['uname']
        password = request.form['psw']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO doctortb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','"+special+"','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()

    data1 = 'Record Saved'
    return render_template('goback.html', data=data1)






@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            data1='Username or Password is Incorrect!'
            return render_template('goback.html', data=data1)



        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )



@app.route("/UserSearch", methods=['GET', 'POST'])
def UserSearch():
    if request.method == 'POST':
        special = request.form['special']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM doctortb where Specialist='"+special+"'")
        data = cur.fetchall()

        return render_template('UserAppointment.html', data=data)

@app.route("/UserAppointment")
def UserAppointment():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM doctortb ")
    data = cur.fetchall()

    return render_template('UserAppointment.html', data=data )




@app.route("/UserAssignDrugInfo")
def UserAssignDrugInfo():

    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  drugtb where UserName='" + uname + "'  ")
    data = cur.fetchall()


    return render_template('UserAssignDrugInfo.html', data=data )


@app.route("/UserHome")
def UserHome():

    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where UserName='" + uname + "'  ")
    data = cur.fetchall()


    return render_template('UserHome.html', data=data )


@app.route("/userapp", methods=['GET', 'POST'])
def userapp():
    if request.method == 'POST':


        uname = session['uname']

        dname = request.form['dname']
        date = request.form['date']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM regtb where  UserNAme='" + uname + "'")
        data = cursor.fetchone()

        if data:
            mobile = data[4]
            email = data[3]


        else:

            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  apptb VALUES ('','" + uname + "','" + mobile + "','" + email + "','" + dname + "','" + date + "')")
        conn.commit()
        conn.close()

        data1 = 'Record Saved'
        return render_template('goback.html', data=data1)



@app.route("/heart", methods=['GET', 'POST'])
def heart():
    if request.method == 'POST':


        uname = session['uname']

        age = request.form['age']
        gender = request.form['gender']
        height = request.form['height']
        weight = request.form['weight']
        aphi = request.form['aphi']
        aplo = request.form['aplo']
        choles = request.form['choles']
        glucose = request.form['glucose']
        smoke = request.form['smoke']
        alcohol = request.form['alcohol']




        age = int(age)
        gender = int(gender)
        height = int(height)
        weight = int(weight)
        aphi = int(aphi)
        aplo = float(aplo)
        choles = float(choles)
        glucose = int(glucose)
        smoke = int(smoke)
        alcohol = int(alcohol)


        filename2 = 'heart-prediction-rfc-model.pkl'
        classifier2 = pickle.load(open(filename2, 'rb'))

        data = np.array([[age, gender, height, weight, aphi, aplo, choles, glucose, smoke, alcohol  ]])
        my_prediction = classifier2.predict(data)
        print(my_prediction[0])

        if my_prediction == 1:
            Answer = 'Hello:According to our Calculations, You have Heart disease'



            msg = 'Hello:According to our Calculations, You have Heart disease '
            print('Hello:According to our Calculations, You have Heart disease')

            session['Ans']='Yes'
            #Heart Cancer Diabetes
            session['dtype'] = 'heart'


        else:
            Answer = 'Congratulations!!  You DON T have Heart disease'

            if (aphi >= 100):

                Answer = ' Congratulations!!  You DON T have Heart disease May be Heart Disease Will Affected In Future '
                # Prescription = 'Managing Glucose in T1D Once Had But One Treatment'
            else:
                Answer = 'Congratulations!!  You DON T have Heart disease'
                # Prescription = "Medications Names:Repaglinide(Prandin)Nateglinide (Starlix)"

            msg = 'Congratulations!!  You DON T have Heart disease'
            print('Congratulations!! You DON T have Heart disease')
            Prescription = 'Nill'
            session['Ans'] = 'No'






        return render_template('Answer.html', data=Answer)





@app.route("/ViewDoctor", methods=['GET', 'POST'])
def ViewDoctor():
    if request.method == 'POST':

        ans = session['Ans']
        loc = session['loca']

        if ans == 'Yes':

            special = session['dtype']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multidieasedb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM doctortb where Specialist='" + special + "'  ")
            data = cur.fetchone()
            if data is None:

                data1 = 'No Doctor Found!'
                return render_template('goback.html', data=data1)



            else:
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multidieasedb')
                # cursor = conn.cursor()
                cur = conn.cursor()
                cur.execute("SELECT * FROM doctortb where Specialist='" + special + "' ")
                data = cur.fetchall()
                return render_template('UserAppointment.html', data=data)




        else:
            uname =  session['uname']
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1multidieasedb')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + uname + "' ")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data)



@app.route('/download')
def download():

    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM drugtb where  id = '" + str(id) + "'")
    data = cursor.fetchone()
    if data:
        filename = "static\\upload\\"+data[7]

        return send_file(filename, as_attachment=True)

    else:
        return 'Incorrect username / password !'







@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        date = request.form['date']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1medicalchatdb')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM assigntb where Lastdate='"+date+"'")
        data = cur.fetchall()



        return render_template('Notification.html', data=data)





def sendmsg(targetno,message ):
    import requests
    requests.post("http://smsserver9.creativepoint.in/api.php?username=fantasy&password=596692&to=" + targetno + "&from=FSSMSS&message=Dear user  your msg is " + message + " Sent By FSMSG FSSMSS&PEID=1501563800000030506&templateid=1507162882948811640")



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)