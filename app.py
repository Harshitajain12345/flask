from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Choices for the game
choices = ['Stone', 'Paper', 'Scissors']

def determine_winner(player, computer):
    if player == computer:
        return 'Draw'
    elif (player == 'Stone' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Stone') or \
         (player == 'Scissors' and computer == 'Paper'):
        return 'You Win!'
    else:
        return 'Computer Wins!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    player_choice = request.form['choice']
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return render_template('index.html', player_choice=player_choice, computer_choice=computer_choice, result=result)

if __name__ == '__main__':
    app.run(debug=True)
