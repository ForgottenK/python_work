name_list = ['jing zhang', 'tieshuan wang', 'yueling shi']
print('I want to invite ' + name_list[0].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[1].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[2].title() + ' to have dinner with me.')
print(name_list[0].title() + ' is busy, so can not come to have dinner with me.')
name_list[0] = 'hong yuan'
print('I want to invite ' + name_list[0].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[1].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[2].title() + ' to have dinner with me.')
print('I have discovered a bigger dinner table')
name_list.insert(0, 'jing wang')
name_list.insert(2, 'tian zhang')
name_list.append('yang cheng')
print('I want to invite ' + name_list[0].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[1].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[2].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[3].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[4].title() + ' to have dinner with me.')
print('I want to invite ' + name_list[5].title() + ' to have dinner with me.')
print('I invited ' + str(len(name_list)) + ' people to have dinner with me.')
print('I received a message that the new table can not be send in time, \nso that I can only invite two person to have dinner with me.')
print("I'm so sorry to tell " + name_list.pop().title() + " that I can't have dinner with you.")
print("I'm so sorry to tell " + name_list.pop().title() + " that I can't have dinner with you.")
print("I'm so sorry to tell " + name_list.pop().title() + " that I can't have dinner with you.")
print("I'm so sorry to tell " + name_list.pop().title() + " that I can't have dinner with you.")
print('So ' + name_list[0].title() + ' is still can have dinner with me.')
print('So ' + name_list[1].title() + ' is still can have dinner with me.')
print('So I invited ' + str(len(name_list)) + ' people to have dinner with me.')
del name_list[1]
del name_list[0]
print(name_list)