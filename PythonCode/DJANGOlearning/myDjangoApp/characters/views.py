from django.shortcuts import render
from django.http import HttpResponse
from characters.models import Character
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, Template
import json

# Create your views here.

def updatepage(request):
	return render(request, "characters/update.html")


def updateChar(request):
    request_str = request.body
    body_obj = json.loads(str(request_str, 'UTF-8'))
    print(body_obj)
    character = Character(firstname = body_obj['charId']['firstName'], 
                            lastname = body_obj['charId']['lastName'], 
                            curr_time = body_obj['charId']['curr_time'], 
                            ability = body_obj['ability'], 
                            role = body_obj['role'], 
                            description = body_obj['description'], 
                            items = body_obj['items'], 
                            relations = body_obj['relations']
                            )
    character.save()
    
    template = Template("{{testdata}}:{{mydata}}")
    context = RequestContext(request, {"test":"this worked"})
    return HttpResponse(template.render(context))
    
