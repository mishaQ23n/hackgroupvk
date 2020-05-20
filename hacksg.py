import time, vk_api,colorama
from vk_api.longpoll import VkLongPoll, VkEventType
from colorama import Fore, Back, Style
colorama.init()

for i in range(2000):
  print(Fore.RED + 'Создатель https://vk.com/ultimatescam')
sisi = [
"""
               МЫ НЕ НЕСЕМ ОТВЕСТВЕННОСТЬ!
                  
                  
     МНЕ ПОХУЙ __               /
         ╲    (_()             /
     ` + ╲__/  ||       ╲__/  /
    '(*).(xx)  /)       (oo)
    + ╲╲//~~╲╲//       //~~╲╲
       ╲/╲__/╲/   _____╲╲__//_____
         |/╲|    |hackgroup     |
   _____ |||| ___|                |
  ______(_)(_)___|________________|

"""]
print(sisi[0])
print(Fore.GREEN + "Дарова! Скрипт который пиздит группу))) \n Создатель https://vk.com/ultimatescam.\n Если не хотите дядю в масках, юзайте VPN\n 1) Начать пиздилку 2) Инструкция и ошибки. ")
kaka = input("Выбирите цифру ебать: ")

if kaka == "1":
   owner = input("Ид сообщества: ") #ид группы# названия сообщества
   titlse = input('Выбирите названия группы: ')
   zyi = input('Описания группы: ')
   tokense = input(' Ваш Токен от страницы: ')
   toker = input('токен от группы: ')
   print(Fore.RED + "Предоставил Скрипт https://vk.com/ultimatescam. \n Если вы все сделали правильно, то пиздец группе") # Создатель  https://vk.com/ultimatescam 
   try:
      vk_session = vk_api.VkApi(token=tokense)
      api = vk_session.get_api()
      api.groups.edit(group_id=owner,title=titlse,description=zyi,token=toker,message='0',photos='0',audio='0')
   except Exception as er:
      print("ОШИБКА, ТЫ ЕБАНАШКА ЧЕТ НЕ ТО ВВЕЛ! ПЕРЕПРОВЕРЬ ВСЕ.")
if kaka == "2":
  print(Fore.BLUE + "Инструкция по этому прекрасному скрипту!\n 1. Где взять токен страницы????! Отвечу вам здесь: https://vkhost.github.io/ \n Выбираете VK ADMIN, разрешаете, и вставляете.\n 2.Я ввёл все правильно, но у меня ошибка. Что делать?! \n Скорей всего вы выбрали неверный токен страницы. Напоминаю, что надо выбрать VK ADNIN. ")
else:
  print("Ты ебанутый?) Цифру 1 или 2 блять выбери")
# Создатель  https://vk.com/ultimatescam # Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
# Создатель  https://vk.com/ultimatescam 
