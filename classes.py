class Task:
	def __init__(self, description, completed, id_task, max_variable=0, variable=0, tag=""):
		self.description = description
		self.completed = completed
		self.id_task = id_task
		self.max_variable = max_variable
		self.variable = variable
		self.tag = tag