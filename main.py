from a2 import Todolist
while True:
	print("MY TO DO LIST")


	print("-"*50)
	ch=input("enter your choice:\n1.to do\n2.done\n3.entire list")
	if ch==1:
		Todolist.add()

	if ch==2:
		Todolist.mark_done()
	if ch==3:
		Todolist.see_tasks()
	else:
		break	 	
