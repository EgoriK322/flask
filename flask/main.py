from flask import Flask, flash, request, redirect, url_for, render_template
import random

app = Flask(__name__)

facts_list=["Я русский", "Фуфелшмертс","Сигма сигма бой сигма бой"]

@app.route("/")
def main():
    return '<a href="/fact/">фактик</a>' '<a href="/how/">.</a>'

@app.route("/fact/")
def fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/how/")
def how():
    return render_template('index.html')


app.run(debug=True)