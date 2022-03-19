import game_logic
import balance_info
from time import sleep

print('----------!!!Welcome to casino!!!----------')
sleep(0.5)
print(f'Balance:{balance_info.balance}')
while True:
    menu = input('Check Balance:1)\nStart roulette:2)\nExit:3)')
    if menu == '1':
        print(f'Your Balance:{balance_info.MY_MONEY}')
    elif menu == '2':
        game_logic.fortune()
    elif menu == '3':
        print('Good Bye')

        print(f'Balance:{balance_info.balance}')
        break

lucker = input('----------Check your luck with the JUDGE\nPRESS 1\nELSE 0')
if lucker.title() == '1':
    game_logic.check_lucker()
if lucker.title() == '0':
    logo = (f'----------You are suck----------')
    for i in logo:
        sleep(0.1)
        print(i)

print(f'{balance_info.balance}')