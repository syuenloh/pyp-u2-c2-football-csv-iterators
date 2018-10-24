import csv

from .models import Player


class FootballExplorer(object):
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def all(self):
        with open(self.csv_file_name, newline='') as csvfile:
            player = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in player:
                return Player(row)

    def search(self, country=None, year=None, age=None, position=None):
        raise NotImplementedError()
