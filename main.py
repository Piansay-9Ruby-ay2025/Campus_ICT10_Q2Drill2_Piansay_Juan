# gettung data from a text box
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ' '
    club_members = ['comanda', 'panela', 'veran', 'mariano', 'tabije', 'calaca', 'barlisan']

    name = document.getElementById('lname').value.lower().strip()
    validation1 = name in club_members # true or falsse 1 true false 0

    display_message = ('Sorry your name is not on the list', f'Congratulation your {name} is on the list')

    display(display_message[validation1], target = 'div1')


    document.getElementById('div2').innerHTML = ' '
    club_members = ['pocholo', 'macy', 'lucian', 'anika', 'wacky', 'mohamad', 'yanna']

    name = document.getElementById('fname').value.lower().strip()
    validation2 = name in club_members # true or falsse 1 true false 0

    display_message = ('Sorry your name is not on the list', f' Congratulation your {name} is on the list')

    display(display_message[validation2], target = 'div2')

