import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(r'C:\Users\kaisyuenl\Data science projects\pyp-u2-c2-football-csv-iterators\test_data.csv') as csvfile:
            player = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in player:
                return Player(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])

    def search(self, country=None, year=None, age=None, position=None):
        return Player(self,number,position,name,date_of_birth,caps,club,country,club_country,year)
