from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.

def home(request):
    itesm = TodoItem.objects.all()
    return render(request, "base.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos":items})

def assign_message(box_value):
    """ Function to assign a message based on box value """
    if box_value in ["Box 1 Value", "Box 2 Value"]:
        return "You clicked one of the first two boxes!"
    elif box_value in ["Box 3 Value", "Box 4 Value"]:
        return "Middle boxes are your choice!"
    elif box_value in ["Box 5 Value", "Box 6 Value"]:
        return "You seem to like the last boxes!"
    else:
        return "Unknown box!"

def boxes_view(request):
    message = None
    if request.method == 'POST':
        # Retrieve the box value from the posted data
        box_value = request.POST.get('box_value')
        # Process the box_value to get the associated message
        message = assign_message(box_value)
    return render(request, 'boxes.html', {'message': message})
