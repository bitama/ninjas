from django.shortcuts import render,redirect
import random
from time import gmtime,strftime

def index(request):
    if "gold" not  in request.session:
        request.session['gold']=0
        request.session["activities"] = []
    return render(request,"index.html")
def process(request):
    print(request.POST["location"])
    amountToAdd=0
    time = strftime("%Y-%m-%d %H:%M:%S",gmtime())
    if request.POST["location"]=="Farm":
        amountToAdd=random.randint(10,20)
        activity =f"Earned {amountToAdd} from Farm at {time}"
    elif request.POST["location"]=="House":
        amountToAdd=random.randint(5,10)
        activity =f"Earned {amountToAdd} from House at {time}"
    elif request.POST["location"]=="Cave":
        amountToAdd=random.randint(2,5)
        activity =f"Earned {amountToAdd} from Cave at {time}"
    elif request.POST["location"]=="Cassino":
        amountToAdd=random.randint(0,50)
        if amountToAdd < 0:
            activity = f"Lost {amountToAdd} from Cassino at {time}"
        else:
            activity = f"Earned {amountToAdd} from Cassino at {time}"
    request.session["gold"]+=amountToAdd
    request.session["activities"].append(activity)
    return redirect("/")

    
    
