from functions import *
from classes import *

#code
global file_w
global parameters_file

if not retry():
	choose()
else:
	load_g()

def us():
	choose = input("""
Выберите действие: 

1)Добавить дело
2)Удалить дело	
3)Пометить как выполненное
4)Просмотреть лист задач
5)Изменить файл 
6)Добавить часть значения задачи
7)Присвоить тэг к задаче
8)Выписать задачи с тэгом

:""")

	if choose == "1":
		add_task()


	elif choose == "2":
		del_task()


	elif choose == "3":
		completed_task()


	elif choose == "4":
		view_list()

	elif choose == "5":
		change_file()

	elif choose == "6":
		add_to_variable()

	elif choose == "7":
		tag()

	elif choose == "8":
		tags_tasks()

	us()



us()

