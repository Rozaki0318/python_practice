class Roboko(object):
  def __init__(self, name):
    self.name = name
    print('{} has been created!'.format(self.name))

  def say_hello(self):
    print('Hello friends! How is it going?')

roboko = Roboko('Hanako')
roboko.say_hello()
