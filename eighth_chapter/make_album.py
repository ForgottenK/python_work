def make_album(artist, album, songs=''):
	dist = {'artist': artist, 'album': album}
	if songs:
		dist['songs'] = songs
	return dist
print(make_album('Michael Jackson', 'Dangerous'))
print(make_album('Maroon5', 'V'))
print(make_album('Jason Mraz', 'I\'m Yours', '5'))
while True:
	print('Enter \'q\' to quit at anytime')
	artist = input('Please input an artist\'s name: ')
	if artist == 'q':
		break
	album = input('Please input an album\'s name: ')
	if album == 'q':
		break
	print(make_album(artist, album))