class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx + 4
        position[1] = position[1] + dy + 6
        return position

summer = Bird()
print 'after move:',summer.move(5,8),summer.way_of_reproduction,summer.have_feather


class Chicken(object):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
#print summer.have_feather
#print summer.move(6,8)
print summer.way_of_move
print summer.possible_in_KFC