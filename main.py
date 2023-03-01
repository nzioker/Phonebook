from flask import Flask, render_template, request, redirect, url_for, flash
import db
import random

app = Flask(__name__)
app.secret_key = "Secret"


@app.route("/")
def contact_home():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def contact_add():
    if request.method == "POST":
        contact_id = random.randint(0, 10000)
        contact_names = request.form.get("c_names")
        contact_number = request.form.get("c_number")
        contact_email = request.form.get("c_email_address")
        contact_fax = request.form.get("c_fax")
        # check whether the contact exists

        # Add to database
        db.PhonebookDB().insert_to_db(
            contact_id, contact_names, contact_number, contact_email, contact_fax
        )
        flash(f"{contact_names} added succesfully")

        return render_template("add_contact.html")
    return render_template("add_contact.html")


@app.route("/display", methods=["GET", "POST"])
def display_contacts():
    all_contacts = db.PhonebookDB().fetch_all_contacts()
    return render_template("all_contacts.html", all_contacts=all_contacts)


@app.route("/update/<int:Id>/", methods=["GET", "POST"])
def update_contact(Id):
    update = db.PhonebookDB().fetch_one_contact(Id)[0]
    name, phone, email, fax = update[1], update[2], update[3], update[4]
    if request.method == "POST":
        db.PhonebookDB().update_db(Id, name, phone, email, fax)
        return render_template("all_contacts.html")

    return render_template(
        "update_contact.html", name=name, phone=phone, email=email, fax=fax
    )


@app.route("/delete/<int:Id>")
def delete_contact(Id):
    contact_name = db.PhonebookDB().fetch_one_contact(Id)[0][1]
    db.PhonebookDB().delete_one_contact(Id)
    flash(f"{contact_name} deleted succesfully")
    return redirect(url_for("display_contacts"))


if __name__ == "__main__":
    app.run(debug=True)
