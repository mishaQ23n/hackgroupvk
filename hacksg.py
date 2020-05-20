import time, vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

owner = input('Ид сообщества') #ид группы# названия сообщества
titlse = input('Выбирите названия группы: ')
zyi = input('Описания группы: ')
tokense = input(' Ваш Токен от страницы: ')
toker = input ('токен от группы: ')
print("Предоставил Скрипт https://vk.com/ultimatescam. \n Если вы все сделали правильно, то пиздец группе")
vk_session = vk_api.VkApi(token=tokense)
api = vk_session.get_api()
api.groups.edit(group_id=owner,title=titlse,description=zyi,token=toker,message='0',photos='0',audio='0')

