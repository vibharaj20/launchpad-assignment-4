

class Todolist:
	
	def __init__(self):
		self.list_name="my day"
		self.to_do=[]
		self.done=[]


	def add(self,task):
		for task in to_do:
			self.to_do.append(task)
			print("TO DO:"+str(to_do))
			

	def mark_done(self,done,task):
		for task in done:
			self.done.append(task)
			print("DONE:"+str(done))

	def see_tasks(self):
		print("TO DO:"+str(to_do))
		print("DONE:"+str(done))

to_do=["execrise","practice dance","study","clean my room","attend class","water plants"]
done=["take a shower","shopping","read a book"]
lists=to_do+done
t1=Todolist()
t1.add(to_do)
t1.see_tasks()





		

