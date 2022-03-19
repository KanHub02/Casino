import random
from time import sleep
import balance_info


def fortune():
    while True:
        bet = int(input('Your bet'))
        lots = [5, 10, 15, 20, 25, 30]
        winlot = random.choice(lots)
        lot = int(input(f'Choose your lot from {lots} '))
        sleep(1)
        print('...')
        sleep(0.5)
        print('Spinning lots')
        sleep(0.5)
        if lot == winlot:
            balance_info.balance += bet * 2
            print(f'----------You win!!!\n----------Win lot was {winlot}\n----------Balance:{balance_info.balance}')
            q = input('Do want continue 1/0')
            if q == '1':
                continue
            elif q == '0':
                break

        if lot != winlot:
            balance_info.balance -= bet
            print(f'----------Your slot was:{lot}\n----------Win slot:{winlot}\n----------Sorry(, try again\n----------Balance:{balance_info.balance}----------')
            q = input('Do want continue 1/0')
            if q == '1':
                sleep(1)
                print('...')
                continue
            elif q == '0':
                sleep(1)
                print('...')
                break


def check_lucker():
    monsters = ['Ancient Dragon', 'Dwarf', 'Elf of blood']
    true_monster = random.choice(monsters)

    quest = input(f'There is a door in front of you, there is an {true_monster}. Do you believe me?\n1/2')
    if true_monster == monsters[2]:
        if quest.title() == '1':
            balance_info.balance += 1000
            print(f'-----  $$$$$  ----- YOU WIN!!!  -----  $$$$$  -----')
            print(f'Your balance:{balance_info.balance}')
            return
    if quest.title() == '2':
        balance_info.balance -= 1000
        print(f'----- HAHAHA  ----- YOU LOSE!!!  ----- HAHAHA  -----')
        print(f'Your balance:{balance_info.balance}')
        return
    if quest.title() == '1':
        balance_info.balance -= 1000
        print(f'----- HAHAHA  ----- YOU LOSE!!!  ----- HAHAHA  -----')
        print(f'Your balance:{balance_info.balance}')
        return



if __name__ == '__main__':
    check_lucker()
