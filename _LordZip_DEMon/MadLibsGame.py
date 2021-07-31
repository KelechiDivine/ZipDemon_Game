from tkinter import *

root = Tk()
root.geometry(" 300x300 ")
root.title('ZipDemon Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)

def lower_creature_name():
    _animal= input("Enter a animal name: ")
    _profession= input("Enter a professional name: ")
    _cloth= input("Enter a cloth name: ")
    _thing("Enter thing name: ")
    _place= input("Enter a place name: ")
    _verb= input("Enter a verb: ")
    _food= input("Enter a food: ")
    
    print( 'say ' + _food + ', the photographer said as the camera flashed! '
       + _name + ' and I had gone to ' + _place +
       ' to get our photos taken ''on my birthday. '
       'The first photo we really wanted was a picture of us dressed as '
       + _animals + ' pretending to be a ' + _profession +
       '. when we saw the second photo, it was '
       'exactly what I wanted. We both looked like ' + _things +
       ' wearing ' + _cloth + ' and ' + _verb +
       ' --exactly what I had in mind')


def non_living_name():
    _adjactive = input('Enter adjective : ')
    _color = input('Enter a color name : ')
    _thing = input('Enter a thing name :')
    _place = input('Enter a place name : ')
    _person = input('Enter a person name : ')
    _adjactive1 = input('Enter a adjactive : ')
    _insect = input('Enter a insect name : ')
    _food = input('Enter a food name : ')
    _verb = input('Enter a verb name : ')
    
    print(
        'Last night I dreamed I was a ' + _adjactive +
        ' butterfly with ' + _color + ' splocthes that looked like '
        + _thing + ' .I flew to ' + _place + ' with my bestfriend and '
        + _person + ' who was a ' + _adjactive1 + ' ' + _insect +
        ' .We ate some ' + _food +
        ' when we got there and then decided to ' + _verb +
        ' and the dream ended when I said-- lets ' + _verb + '.')


def person_name():
    _person = input('Enter person name: ')
    _color = input('Enter color : ')
    _foods = input('Enter food name : ')
    _adjective = input('Enter aa adjective name: ')
    _thing = input('Enter a thing name : ')
    _place = input('Enter place : ')
    _verb = input('Enter verb : ')
    _adverb = input('Enter adverb : ')
    _food = input('Enter food name: ')
    _things = input('Enter a thing name : ')
    
    print(
        'Today we picked apple from '
        + _person + "'s Orchard. "
                   "I had no idea there were so many different "
                   "varieties of apples. I ate " + _color
        + ' apples straight off the tree that tested like '
        + _foods + '. Then there was a '
        + _adjective + ' apple that looked like a '
        + _thing + '.When our bag were full, we went on a'
                  ' free hay ride to ' + _place +
        ' and back. It ended at a hay pile where we got to '
        + _verb + ' ' + _adverb + '. I can hardly wait'
                                ' to get home and cook with the apples.'
                                ' We are going to make appple ' +
        _food + ' and ' + _things + ' pies!.')
    return self.tk.call('wm', 'geometry', self._w, newGeometry)

Button(root, text= 'Demon_Camera', font ='arial 15', command= madlib1, bg =
'ghost white').place(x_axis=60, y_axis=120)
Button(root, text= 'Demon Apple', font ='arial 15', command = madlib3 , bg =
'ghost white').place(x_axis=70, y_axis=180)
Button(root, text= 'The Demon Butterfly', font ='arial 15', command = madlib2, bg =
'ghost white').place(x_axis=80, y_axis=240)

root.mainloop()