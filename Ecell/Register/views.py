from django.contrib.auth import login, logout
from django.shortcuts import render
from .models import User


# Create your views here.

def index(request):
	if request.method == "POST":
		u_name = request.POST["username"]
		p_word = request.POST["password"]
		try: 
			x=User.objects.get(username=u_name)
			try:
				y=User.objects.get(password=p_word)
				return render(request,"Register/user.html",{
					"data":y #gets data in that row
				}) 
			except:
				return render(request,"Register/login.html",{
					"message":"Invalid password"
					})
		except:
			return render(request,"Register/login.html",{
					"message":"User does not exist, kindly register"
					})
	return render(request,"Register/login.html")
def register(request):
	if request.method == "POST": 
		u_name = request.POST["username"]
		try:
	 		x=User.objects.get(username=u_name)
	 		return render(request,"Register/register.html",{
			"message":"User already exists"
			})
		except:
	 		p_word = request.POST["password"]
	 		name = request.POST["name"]
	 		email = request.POST["email"]
	 		x=User(name=name ,email=email, password= p_word, username=u_name)
	 		x.save()
	 		return render(request,"Register/login.html")
	return render(request,"Register/register.html")

