from flaskcrud import app
from flask import Flask, render_template, request, redirect, url_for, flash
from flaskcrud.models import Data
from flaskcrud.forms import Item
from flaskcrud import db
from werkzeug.utils import secure_filename

@app.route("/")
def Index():
    form = Item()
    all_data = Data.query.all()


    return render_template("index.html", employees = all_data, form = form)

@app.route("/insert", methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))

# @app.route("/update", methods = ['GET', 'POST'])
# def update():
#     if request.method == 'POST':
#         my_data = Data.query.get(request.form.get('id'))
#         my_data.name = request.form['name']
#         my_data.email = request.form['email']
#         my_data.phone = request.form['phone']

#         db.session.commit()
#         flash("Employee Updated Sucessfully")

#         return redirect(url_for('Index'))

@app.route("/delete/<id>", methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Sucessfully")

    return redirect(url_for('Index'))


@app.route("/home", methods= ['GET', 'POST'])
def home():
    form = Item()
    if form.validate_on_submit():
        my_data = Data(name = form.name.data, email = form.email.data, phone = form.phone.data)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('Index'))

    return render_template('home.html', form = form)

@app.route("/update", methods= ['GET', 'POST'])
def update():
    form = Item()
    if request.method == 'POST':
        print(request.form.get('name'))
        my_data = Data.query.get(request.form.get('id'))
        # my_data = Data(name = form.name.data, email = form.email.data, phone = form.phone.data)
        my_data.name = form.name.data
        my_data.email = form.email.data
        my_data.phone = form.phone.data

        db.session.commit()
        flash("Employee Updated Sucessfully")

        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
