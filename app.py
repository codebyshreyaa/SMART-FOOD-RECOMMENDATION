from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            goal = request.form['goal']
            
            # Simple recommendation logic
            if goal == "Muscle Gain":
                protein = round(age * 1.5, 1)
                result = f"Recommended Protein Intake: {protein} grams/day"
            elif goal == "Weight Loss":
                calories = round(2000 - age * 5, 0)
                result = f"Recommended Daily Calories: {calories} kcal"
            else:
                result = "Goal not recognized."
        except ValueError:
            result = "Please enter a valid age."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
