import billboard
chart = billboard.ChartData('country-songs')
print(chart.title)
song = chart[0]  # Get no. 1 song on chart
print(song.title)
print(song.artist)
print(song.weeks)  # Number of weeks on chart