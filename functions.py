from classes import *
import os

default_file = "save.txt"
file_w = ""
parameters_file = "save_admin.txt"

def save_admin_edit(info):
	with open(parameters_file, "w") as file:
		file.write(info)

last_id = 0
tasks = []





#Main Function
def view_list():
	for task in tasks:
		if not task.completed and task.max_variable != "":
			print(f"[{task.id_task}][X]{task.description} {task.variable}/{task.max_variable}")
		elif not task.completed and task.max_variable == "":
			print(f"[{task.id_task}][X]{task.description}")
	for task in tasks:
		if task.completed and task.max_variable != "":
			print(f"[{task.id_task}][√]{task.description} {task.variable}/{task.max_variable}")
		elif task.completed and task.max_variable == "":
			print(f"[{task.id_task}][√]{task.description}")


#FUNCTIONS
def add_task():
	global last_id
	description = input("""
Назови твою задачу

:""")
	chh = input("""

Нужно ли вам значение выполненной части задачи?


1)Да
2)Нет

""")

	if chh == "1":
		max_v = input("""

:

""")
	elif chh == "2":
		pass

	if not description.isspace() and description != '':
		if chh == "1":
			task = Task(description, False, gni(), max_v, 0)
			last_id = last_id+1
		if chh == "2":
			task = Task(description, False, gni())
			last_id = last_id+1
		tasks.append(task)

		save()
		view_list()



def del_task(c=tasks):
	input_id = input("Напишите номер дела:")
	if validate_id(input_id, tasks):
		for index, task in enumerate(tasks):
			if task.id_task == int(input_id):
				c.pop(index)
				save()
				break
	else:
		print(f"\nЗадачи с номером {input_id} не найдено, введите другой номер\n")


	view_list()


def completed_task(c=tasks):
	index1 = input("Напишите номер дела:")
	if validate_id(index1, tasks):
		for index, task in enumerate(tasks):
			if task.id_task == int(index1):
				task.completed = True
				save()
				break
	else:
		print(f"\nЗадачи с номером {index1} не найдено, введите другой номер\n")

	view_list()


def add_to_variable():
	number=''
	choose = input("""

'ДОБАВИТЬ' или 'УСТАНОВИТЬ'? 

1)Добавить
2)Устновить

: """)
	if choose == "1":
		number == int(input("""

Напишите номер дела:

"""))
		add = input("""

Сколько добавить?

:
""")
		for task in tasks:
			if task.id_task == int(number):
				task.variable = task.variable + add
				print(task.variable)
				save()

					

				



#########

#########test functions


def validate_id(id_, list1):
	if id_.isnumeric() and int(id_) >= 0:
		for index, task in enumerate(tasks):
			if task.id_task == int(id_):
				return True

		return False
	else:
		return False


def gni(lt=last_id): #gni - get new id 
	global last_id
	return last_id


def save():
	global fail_w
	with open(file_w, "w") as file:
		for task in tasks:
			if task.max_variable == "":
				file.write(f"{task.id_task};{task.completed};{task.description}\n")
			else:
				file.write(f"{task.id_task};{task.completed};{task.description};{task.max_variable};{task.variable}\n")

def load():
	global last_id
	global file_w
	last_id = 0
	with open(file_w, "r") as file:
		alls = file.read()
		lines = alls.split("\n")
		for line in lines:
			if line != "":
				elements = line.split(";")
				if len(elements) == 5:
					ids = int(elements[0])
					descr = str(elements[2])
					max_v = int(elements[3])
					v = int(elements[4])
					if elements[1] == "True":
						task = Task(descr, True, ids, max_v, v)
					else:
						task = Task(descr, False, ids, max_v, v)
					tasks.append(task)
					last_id=last_id+1
				elif len(elements) == 3:
					ids = int(elements[0])
					descr = str(elements[2])
					if elements[1] == "True":
						task = Task(descr, True, ids)
					else:
						task = Task(descr, False, ids)
					tasks.append(task)
					last_id=last_id+1
	view_list()


def change_file():
	global file_w
	global tasks
	tasks = []
	file_w = input("Назовите путь или имя файла: \n") + ".txt"
	if os.path.isfile(file_w):
		with open(parameters_file, "w") as file:
			file.write(file_w)
		load()
	else: 
		save()


def retry():
	if os.path.isfile(parameters_file):
		with open(parameters_file, "r") as file:
			if file.read() != "":
				return True
			else:
				return False

#########


def choose():
	global file_w

	ch = input("""
Нужен ли вам default файл?

1)Да
2)Свой

""")

	if ch == "1":
		global file_w
		global default_file

		file_w = default_file
	else:
		file_w = input("Назовите путь или имя файла: \n") + ".txt"

	with open("save_admin.txt", "w") as file:
		file.write(file_w)

	if os.path.isfile(file_w):
		load()
	else: 
		save()



def load_g():
	global file_w
	global parameters_file

	with open(parameters_file, "r") as file:
		g = file.read()
		file_w = g
		load()


##################################

