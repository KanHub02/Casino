from envparse import env
import os
balance = env('Balance', 1000)
env.read_envfile('settings.env')



MY_MONEY = (os.getenv('settings.env'))
# class Balance:
#     def __init__(self, MY_MONEY, val):
#         self.__MY_MONEY = MY_MONEY
#         self.__val = val
#
#     @property
#     def val(self):
#         return self.__val
#
#     @val.setter
#     def val(self, value):
#         self.__val = value
#
#     @property
#     def MY_MONEY(self):
#         return self.__MY_MONEY
#
#     @MY_MONEY.setter
#     def MY_MONEY(self, value):
#         self.__MY_MONEY = value
#
#
# balance = Balance('MY_MONEY', 1000)
