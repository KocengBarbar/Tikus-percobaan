from random import choice
from os import system
from time import sleep

hil='''pilihan

1.Gunting
2.Batu
3.Kertas
'''

def game():
    while True:
        system('clear')
        print hil
        kom=choice(['Gunting','Batu','Kertas'])
        pil=int(raw_input('masukkan pilihan :  '))
        if pil==2:
            print 'anda          :Batu'
            print 'komputer :',kom
            if kom=='Batu':
                print '\t draw' 
            elif kom=='Gunting':
                print'\t anda Anda Menang'
            elif kom== 'Kertas':
                print '\tAnda Kalah!'
        elif pil==1:
            print 'anda          :Gunting'
            print 'komputer :',kom
            if kom=='Batu':
                print '\t anda menang'
            elif kom=='Gunting':
                print '\t draw'
            elif kom== 'Kertas':
                print '\tAnda kalah'
        
       
        elif pil==3:
            print 'anda          :Kertas'
            print 'komputer :',kom
            if kom=='Batu':
                print '\t anda menang\n'
            elif kom=='Gunting':
                print '\t anda kalah\n'
            elif kom== 'Kertas':
                print '\tdraw\n'

        else:
            print 'pilihan yang anda masukkan salah'
            sleep(2)
            continue

        q=raw_input('[+] Press ENTER To Continue Or q To Exit: ')
        if q == 'q':
            break
        elif q == '':
            continue
        else:
            print 'Wrong Input'
            sleep(2)

game()