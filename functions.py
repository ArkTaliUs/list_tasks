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
		if not task.completed:
			print(f"[{task.id_task}][X]{task.description}")
	for task in tasks:
		if task.completed:
			print(f"[{task.id_task}][√]{task.description}")


#FUNCTIONS
def add_task():
	global last_id
	description = input("""
Назови твою задачу

:""")
	if not description.isspace() and description != '':
		task = Task(description, False, gni())
		tasks.append(task)
		last_id = last_id+1
		save()
		view_list()



def del_task(c=tasks):
	input_id = input("Напишите номер дела(начиная от 0):")
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
	index1 = input("Напишите номер дела(начиная от 0):")
	if validate_id(index1, tasks):
		for index, task in enumerate(tasks):
			if task.id_task == int(index1):
				task.completed = True
				save()
				break
	else:
		print(f"\nЗадачи с номером {index1} не найдено, введите другой номер\n")

	view_list()





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
			file.write(f"{task.id_task};{task.completed};{task.description}\n")


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


