from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # This is just a test version — Member B’s logic will go here later
    age = request.form.get('age')
    goal = request.form.get('goal')
    return render_template('index.html', result=f"Got data: Age={age}, Goal={goal}")

if __name__ == '__main__':
    app.run(debug=True)
