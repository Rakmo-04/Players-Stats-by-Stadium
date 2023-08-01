import matplotlib.pyplot as plt
import numpy as np
import csv
def create_pie_chart(stadium_name, player_name):
  """Creates a pie chart of the player's stats at the given stadium."""

  data = get_data(stadium_name, player_name)
  labels = data.index
  values = data.values

  fig, ax = plt.subplots()
  ax.pie(values, labels=labels, autopct='%1.1f%%')
  ax.set_title(f'Player Stats at {stadium_name}')
  plt.show()

def get_data(stadium_name, player_name):
  """Returns the player's stats at the given stadium."""

  data = []
  with open('CSV_FILE_PATH.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
      if stadium_name == row[0] and player_name == row[2]:
        data.append(row[5:])

  return np.array(data)

if __name__ == '__main__':
  stadium_name = input('Enter the stadium name: ')
  player_name = input('Enter the player name: ')
  create_pie_chart(stadium_name, player_name)