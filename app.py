from flask import Flask, render_template, request, redirect, url_for
import random
import emoji

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'next' in request.form:
            return redirect(url_for('index'))

        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation']
        user_answer = request.form['answer']
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '÷':
            correct_answer = num1 / num2
        elif operation == 'x':
            correct_answer = num1 * num2
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                feedback = emoji.emojize("Well done!.")
            else:
                feedback = emoji.emojize(f"Sorry, the correct answer was {correct_answer}.")
        except ValueError:
            feedback = emoji.emojize("Please enter a valid number.")

        return render_template('index.html', feedback=feedback, num1=num1, num2=num2, operation=operation)

    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operation = random.choice(['+', '-', '÷', 'x'])
        return render_template('index.html', num1=num1, num2=num2, operation=operation)


if __name__ == "__main__":
    app.run(debug=True)
