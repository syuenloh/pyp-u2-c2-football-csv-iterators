from football_explorer import FootballExplorer

explorer = FootballExplorer(csv_file_name='squads.csv')
# results = explorer.search(country='Argentina')
# results = explorer.search(position='1GK')
# results = explorer.all()
results = explorer.search(country='Brazil')

for player in results:
    print(player)
