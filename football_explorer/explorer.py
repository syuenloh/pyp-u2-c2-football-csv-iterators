import csv

from .models import Player

class FootballExplorer():
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open('/Users/kaisyuenloh/WWcodeKL/pyp-u2-c2-football-csv-iterators/test_data.csv') as csvfile:
            player = csv.reader(csvfile, delimiter=',', quotechar='|')
            return [Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]) for row in player]

    def search(self, country=None, year=None, age=None, position=None):
        with open('/Users/kaisyuenloh/WWcodeKL/pyp-u2-c2-football-csv-iterators/test_data.csv') as csvfile:
                player = csv.reader(csvfile, delimiter=',', quotechar='|')
                player_lst=[]
                for row in player:
                    player_lst.append(Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        if country == year == age == position== None:
            raise ValueError
        elif country and year:
            return [p for p in player_lst if p.country==country and p.year==int(year)]
        elif country and not year:
            return [p for p in player_lst if p.country==country]
