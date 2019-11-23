from django.shortcuts import render

from .forms import AgentForm

def add_agent (request):
	if request.method =="POST":
		form = AgentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("list_agents")
		
       	
	else:
	    form = AgentForm
	return render(request,"add_agent.html",{"form":form})
def list_agents(request):
	agents = Agent.objects.all()
	return render(request,"all_agents.html",{"agents":agents})
	
# Create your views here.
