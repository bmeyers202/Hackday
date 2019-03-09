from flask import Flask
from flask import g, session, request, url_for, flash
from flask import redirect, render_template
app = Flask(__name__)

@app.route('/Hello')
def hello_world():
    return render_template("index.html")

food_items = {
    'hot dog': 1,
    'burger': 2
}
def algo(food, quadrant):
    #run algo here
    vendor_num =3
    wait_time =4

    return vendor_num, wait_time

@app.route('/')
def index():
    content = request.json
    print (content)
    quadrant = 1

    # run algorithm
    vendor_num, wait_time = algo(food_items['hot dog'], quadrant)

    # put algorithm output in template variables
    vendor_num = 3
    wait_time = 4
    return render_template("index.html", vendor_num=vendor_num, wait_time=wait_time)

inning_half = "top"
inning_num = 1

@app.route('/set_inning', methods=['GET', 'POST'])
def set_inning():
    '''This endpoint is used to set the current inning'''

    if request.method == 'POST':
        print("POST:")
        for key, value in request.form.items():
            print("{0} {1}".format(key, value))
        inning_half = request.form['half']
        inning_num = request.form['inning_num']

    return render_template("inning.html")

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0", port=8080, use_reloader=True)

