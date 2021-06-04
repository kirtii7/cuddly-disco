from django.shortcuts import render
from .models import Todolist
# Create your views here.
task_no=0 
def index(request):
	global task_no
	if request.method == "POST":
		Newtask = request.POST["new_task"]
		if Newtask!="":
			try:
				x=Todolist.objects.get(Info=Newtask)
			except:
				task_no+=1
				x=Todolist(Info=Newtask, status=False, Sno=task_no)
				x.save()
	return render(request,"tasks/index.html",{
		"data":Todolist.objects.all()
		})
def Status(request):
	if request.method == "POST":
		task_no=request.POST["toggle"]
		try:
			Todolist.objects.get(Sno=task_no , status=True)
			Todolist.objects.filter(Sno=task_no).update(status=False)
		except:
			Todolist.objects.filter(Sno=task_no).update(status=True)
	return render(request,"tasks/index.html",{
		"data":Todolist.objects.all()
		})	
def Clearall(request):
	Todolist.objects.all().delete()
	return render(request,"tasks/index.html",{
		"data":Todolist.objects.all()
		})	

def Delete(request):
	if request.method == "POST":
		task_no=request.POST["Delete"]
		Todolist.objects.filter(Sno=task_no).delete()
	return render(request,"tasks/index.html",{
		"data":Todolist.objects.all()
		})	
