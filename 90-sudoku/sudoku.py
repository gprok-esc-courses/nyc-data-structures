import pandas as pd

df = pd.read_csv('sudoku.csv')
quiz = df.iloc[3]['quizzes']
solution = df.iloc[3]['solutions']
current = quiz 


print(quiz)