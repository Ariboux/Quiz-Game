# Quiz Game

Welcome to the Trivia Quiz Game! This simple Python script fetches trivia questions from the Open Trivia Database, presents them to the user, and checks if their answers are correct. The questions cover a variety of categories and difficulty levels.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Ariboux/Quiz_Game-Balderacchi_Adrien-CDOF1.git
cd Quiz_Game-Balderacchi_Adrien-CDOF1
```

2. Install the required dependency. This game uses some libraries but the only not yet installed is requests:

```bash
pip install requests
```
3. Run the game:

```bash
python trivia_game.py
```

## How to Play

1. You will have 10 questions about cinema from the Open Trivia Database.
2. For each question, it displays the question and a list of possible answers.
3. Choose the correct answer by typing the corresponding (NOT YET IMPLEMENTED).
4. The game will inform you if your answer is correct or not.
5. Repeat for all 10 questions. Soon, a score will be implemented.

## Code Explanation

The game is written in Python and utilizes the requests library to fetch trivia questions from the Open Trivia Database. It then uses the json library to parse the response and extract the questions, correct answers, and options.
The html module is used to decode HTML entities in the questions and answers. The game displays the questions one by one, shuffles the answer options, and checks if the user's response is correct.
I want to say a big thank you to the contributor [@Valouz](https://github.com/valoubinouz). Feel free to combritue this project, answer the issues or, for you personal use, customize the code, add new features, or modify the trivia database parameters in the URL to suit your preferences.
Have fun playing and learning! If you have any questions or improvements, feel free to open an issue or submit a pull request.
