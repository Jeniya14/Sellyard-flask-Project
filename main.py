import mysql.connector
from flask import Flask, render_template, request, redirect, session, url_for
import re

app = Flask(__name__)
app.secret_key = "your secret key"


@app.route("/")
def jeniya():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@app.route("/order")
def order():
    return render_template('order.html')


@app.route("/profile")
def pf():
    return render_template('profile.html')


@app.route("/adminlogin")
def al():
    return render_template("adminlogin.html")


@app.route("/alogin", methods=["GET", "POST"])
def alogin():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    msg = ''
    if request.method == 'POST':
        adminname = request.form['adminname']
        password = request.form['password']
        cursor.execute("SELECT * FROM admin WHERE adminname='"+adminname+"' AND password='"+password+"'")
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['id'] = record[1]
            msg = 'Logged in successfully !'
            return render_template('admin.html', msg=msg)
        else:
            msg = 'Incorrect User/Password, Try again!!'
            return render_template('adminlogin.html', msg=msg)


@app.route("/admin")
def admin():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from fruit"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('admin.html')


@app.route("/ManageSellers")
def ms():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from seller"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('ManageSellers.html', data=result)


@app.route("/ManageProducts")
def mp():
    return render_template('ManageProducts.html')


@app.route("/afruits")
def afruits():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from fruit"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('afruits.html', data=result)


@app.route("/avegetables")
def avegetables():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from vegetables"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('avegetables.html', data=result)


@app.route("/ahomemade")
def ahomemade():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from handmade"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('ahomemade.html', data=result)


@app.route("/ahandcraft")
def ahandcraft():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from handcraft"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('ahandcraft.html', data=result)


@app.route('/fruitsdelete', methods=["POST", "GET"])
def fruitsdelete():
    id=request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    cursor.execute("delete FROM fruit WHERE fruit_id='"+id+"'")
    con.commit()
    con.close()
    return redirect(url_for('afruits'))


@app.route('/vegetablesdelete', methods=["POST", "GET"])
def vegetablesdelete():
    id=request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    cursor.execute("delete FROM vegetables WHERE vegetable_id='"+id+"'")
    con.commit()
    con.close()
    return redirect(url_for('avegetables'))


@app.route('/homemadedelete', methods=["POST", "GET"])
def homemadedelete():
    id=request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    cursor.execute("delete FROM handmade WHERE handmade_id='"+id+"'")
    con.commit()
    con.close()
    return redirect(url_for('ahandmade'))


@app.route('/handcraftdelete', methods=["POST", "GET"])
def handcraftdelete():
    id=request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    cursor.execute("delete FROM handcraft WHERE handcraft_id='"+id+"'")
    con.commit()
    con.close()
    return redirect(url_for('ahandcraft'))


@app.route('/sellerdelete', methods=["POST", "GET"])
def sellerdelete():
    id=request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    cursor.execute("delete FROM seller WHERE seller_id='"+id+"'")
    con.commit()
    con.close()
    return redirect(url_for('ManageSellers'))


@app.route("/sellerlogin")
def sl():
    return render_template("sellerlogin.html")


@app.route("/Productdetails")
def pd():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from fruit"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("Productdetails.html", data=result)


@app.route("/addproducts", methods=['GET', 'POST'])
def addproducts():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    if request.method == 'POST':
        fruit_name = request.form['fruit_name']
        fruit_weight = request.form['fruit_weight']
        fruit_rate = request.form['fruit_rate']
        fruit_desc = request.form['fruit_desc']
        fruit_image = request.form['fruit_image']
        cursor.execute("INSERT INTO fruit (fruit_name, fruit_weight, fruit_rate, fruit_desc, fruit_image) VALUES ('" + fruit_name + "','" + fruit_weight + "','" + fruit_rate + "','" + fruit_desc + "', '" + fruit_image + "')")
        con.commit()
        return render_template('Productdetails.html')
    else:
        return render_template("addproducts.html")


@app.route("/SellerAccInfo", methods=["POST", "GET"])
def sellerinfo():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sellername = request.form['sellername']
    password = request.form['password']
    email=request.form['email']
    address=request.form['address']
    delivery=request.form['delivery']
    sql = ("UPDATE seller (sellername, password, email, firstname, lastname) SET ('" + sellername + "', '" + password + "','" + email + "','" + address + "','"+delivery+"')")
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("SellerAccInfo.html", data=result)


@app.route("/sorder")
def sorder():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from order"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("sorder.html", data=result)



@app.route("/contactus")
def contactus():
    return render_template("contactus.html")


@app.route("/slogin", methods=["GET", "POST"])
def slogin():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    msg = ''
    if request.method == 'POST':
        sellername = request.form['sellername']
        password = request.form['password']
        cursor.execute("SELECT * FROM seller WHERE sellername='"+sellername+"' AND password='"+password+"'")
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['id'] = record[1]
            msg = 'Logged in successfully !'
            return render_template('seller.html', msg=msg)
        else:
            msg = 'Incorrect User/Password, Try again!!'
            return render_template('sellerlogin.html', msg=msg)


@app.route("/seller")
def seller():
    return render_template('seller.html')


@app.route('/productsdelete', methods=["POST", "GET"])
def productsdelete():
    id = request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    cursor.execute("delete FROM fruit WHERE fruit_id='"+id+"'")
    con.commit()
    con.close()
    return redirect(url_for('pd'))


@app.route("/login", methods=["GET", "POST"])
def login():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM user WHERE username='"+username+"' AND password='"+password+"'")
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['id'] = record[1]
            msg = 'Logged in successfully !'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Incorrect User/Password, Try again!!'
            return render_template('index.html', msg=msg)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor = con.cursor()
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        cursor.execute("INSERT INTO user  (username, password, email, firstname, lastname) VALUES ('" + username + "', '" + password + "','" + email + "','" + firstname + "', '" + lastname + "')")
        con.commit()
        msg = 'You have successfully registered !'
        return render_template('index.html', msg=msg)
    else:
        msg = 'Please fill out the form !'
    return render_template('registration.html', msg=msg)


@app.route("/fruits")
def jeniya2():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from fruit"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("fruits.html", data=result)


@app.route("/vegetables")
def jeniya3():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from vegetables"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("vegetables.html", data=result)


@app.route("/homemade")
def jeniya4():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from handmade"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("homemade.html", data=result)


@app.route("/handcraft")
def jeniya5():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from handcraft"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("handcraft.html", data=result)


@app.route("/addtocart")
def atd():
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cur = con.cursor()
    sql = "select * from cart"
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("addtocart.html", data=result)


@app.route("/addtocartSave", methods=["POST", "GET"])
def addtocart():
    id = request.args.get("id")
    con = mysql.connector.Connect(user="root", database="jeniyadb")
    cursor1 = con.cursor1()
    cursor1.execute("SELECT* FROM fruit where product_id='"+id+"'")
    record = cursor1.fetchone()
    cursor = con.cursor()
    cursor.execute("insert into cart values('44', '"+session['id']+"', '"+record[0]+"','"+record[2]+"','2','"+record[4]+"')")
    con.commit()
    return render_template("addtocart.html")


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return render_template("index.html")


if __name__ == '__main__':
   app.run(debug=True)
