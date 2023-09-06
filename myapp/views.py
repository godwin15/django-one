from django.shortcuts import render, HttpResponse
from .models import TodoItem
# Create your views here.

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

def home(request):
    message = None
    box_descriptions = ["money coming with 50 posts", "more-money", "even-more-money", "plenty", "plenty-money", "puff", "puff-money", "yes-money"]
   
    if request.method == 'POST':
        # Retrieve the box value from the posted data
        box_value = request.POST.get('box_value')
        # Process the box_value to get the associated message
        message = assign_message(box_value)
        
    context = {
        'box_descriptions': box_descriptions,
        'message':message,
    }
    return render(request, 'boxes.html', context)
