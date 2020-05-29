import time,vk_api,colorama,datetime
from vk_api.longpoll import VkLongPoll, VkEventType, datetime
from colorama import Fore, Back, Style
colorama.init()

def kaka2():
   owner2 = input("Ид страницы: ") #ид группы# названия сообщества
   titlse2 = input('Названия коменнтария: ')
   tokense2 = input(' Ваш Токен от страницы: ')
   com = input('Скок комментов: ') 
   ssaw = input('Пост где оставить комменты: ')
   ss = 0
   while int(ss) < int(com):
      try:
          vk_session = vk_api.VkApi(token=tokense2)
          api = vk_session.get_api()
          api.wall.createComment(owner_id=owner2,message=titlse2,token=tokense2, post_id=ssaw)
          ss += 1
          time.sleep(3)
      except Exception as er:
         print("ОШИБКА, ТЫ ЕБАНАШКА ЧЕТ НЕ ТО ВВЕЛ! ПЕРЕПРОВЕРЬ ВСЕ.")
def kaka3():
   owner3 = input("Ид страницы: ")
   titlesss = input("Названия беседы: ")
   toss = input("Токен страницы: ")
   sasa = input("кол-во бесед: ")
   sq = 0
   while int(sq) < int(sasa):
      try:
         vk_session = vk_api.VkApi(token=toss)
         api = vk_session.get_api()
         api.messages.createChat(user_ids=owner3,title=titlesss,token=toss)
         sq += 1
         time.sleep(60)
      except Exception as er:
         print("ОШИБКА, ЧЕТ НЕ ТО ВВЕЛ! ПЕРЕПРОВЕРЬ ВСЕ.")
def kaka6():
   owene = str(input("Ид страницы: "))
   posta = str(input("Названия поста: "))
   tokenser = str(input("Токен от страницы"))
   wwwaq = str(input("Сколько постов: "))
   vk_session = vk_api.VkApi(token=str(tokenser))
   api = vk_session.get_api()
   wawaaw = 0
   while int(wawaaw) < int(wwwaq):
      try:
         api.wall.post(owner_id=owene,message=posta)
         wawaaw += 1
         time.sleep(4)
      except vk_api.exceptions.Captcha as captcha:
           continue
def kaka4():
        saer = input("Введите токен: ")
        vk_session = vk_api.VkApi(token=saer)
        vk = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        print("Вечный онлайн запущен")
        print("Версия: 2.0")
        while True:
           try:
              time.sleep(60)
              vk.account.setOnline(voip=0)
              account = vk.account.getBanned()
              getBan = account['count']
              getOnline = len(vk.friends.getOnline())
              stats = "✅ Only Online | 👥 Друзья онлайн: " + str(getOnline) + " | 🚫 ЧС: " + str(getBan) + " | ⌚ Время " + str(datetime.strftime(datetime.now(), "%D, %H:%M"))
              vk.status.set(text=stats)
           except vk_api.exceptions.Captcha as captcha:
              continue
def kaka5():
   dasss = input("Введите ваш ID страинцы: ")
   sasas = input("Введите ваш токен от страницы")
   vk_session = vk_api.VkApi(token=sasas)
   api = vk_session.get_api()
   sqq = input("кол-во групп: ")
   srat = 0
   while int(srat) < int(sqq):
      try:
         api.groups.create(title="misha nvuti33",description="...",type="group")
         time.sleep(30)
      except vk_api.exceptions.Captcha as captcha:
          print("Error скорей всего, вы что-то не то ввели, или же лимит/капча")
for i in range(2000):
   print(Fore.RED + 'Создатель https://vk.com/misha.nvuti33')
sisi = [
"""
               БУДЬ АККУРАТНЕЙ!
                  
                  
     МНЕ ПОФИГ __               /
         ╲    (_()             /
     ` + ╲__/  ||       ╲__/  /
    '(*).(xx)  /)       (oo)
    + ╲╲//~~╲╲//       //~~╲╲
       ╲/╲__/╲/   _____╲╲__//_____
         |/╲|    |vk tools 2.0    |
   _____ |||| ___|                |
  ______(_)(_)___|________________|

"""]
print(sisi[0])
k = Fore.RED + 'Дарова! В этом скрипте множество плюшек, для вк.\nСоздатель https://vk.com/misha.nvuti33.\nЕсли не хотите дядю в масках, юзайте VPN'
sara = Fore.YELLOW + '1) хак группы \n2) Накрутка комментов \n3) Накрутка смс \n4) Накрутка постов \n5) Авто-Статус \n6) Инструкция и ошибки.'
predu = Fore.RED + 'МЫ НЕ НИСЕМ ОТВЕТСТВЕННОСТЬ!'
print(k)
print(sara)
print(predu)
kaka = input("Выбири цифру: ")
if kaka == "1":
   owner = input("Ид сообщества: ") #ид группы# названия сообщества
   titlse = str(input('Выбирите названия группы: '))
   zyi = input('Описания группы: ')
   tokense = str(input(' Ваш Токен от страницы: '))
   toker = str(input('токен от группы: '))
   try:
      vk_session = vk_api.VkApi(token=tokense)
      api = vk_session.get_api()
      api.groups.edit(group_id=owner,title=titlse,description=zyi,token=toker,message='0',photos='0',audio='0')
   except vk_api.exceptions.ApiError:
      print("Ошибка, проверьте правильно ли вы все ввели. Так же может быть флуд контрол или же капча.")
if kaka == "2":
   kaka2()
if kaka == "3":
   kaka3()
if kaka == "4":
   kaka6()
if kaka == "5":
   kaka4()
if kaka == "6":
  print(Fore.BLUE + "Инструкция по этому прекрасному скрипту!\n 1. Где взять токен страницы????! Отвечу вам здесь: https://vkhost.github.io/ \n Выбираете VK ADMIN, разрешаете, и вставляете.\n 2.Я ввёл все правильно, но у меня ошибка. Что делать?! \n Скорей всего вы выбрали неверный токен страницы. Напоминаю, что надо выбрать VK ADNIN. ")
else:
  print("Выбери цирфру от 1 до 4")
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33 575a64a3ee28697c2eaba4275412f83cba3702901e0a26fb1823b62f3f7f9d63d80c97cf62e710af11b82 token 576167340
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
# Создатель   https://vk.com/misha.nvuti33
