from django.shortcuts import render, redirect
from .models import AllDrawing
from .forms import AllDrawingForm
from django.shortcuts import get_object_or_404
# Create your views here.
def all_drawings(request):
     drawings = AllDrawing.objects.all()
     return render(request,'Drawings/all_drawings.html',{'drawings':drawings})
     
def drawing_detail(request, drawing_id):
     draws = get_object_or_404(AllDrawing, pk=drawing_id )
     return render(request,'Drawings/drawing_detail.html',{'draws':draws})

def add_drawing(request):
    if request.method == 'POST':
        form = AllDrawingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_drawing')  # redirect to same page to show updated list
    else:
        form = AllDrawingForm()

    drawings = AllDrawing.objects.all()
    return render(request, 'Drawings/add_drawing.html', {'form': form, 'drawings': drawings})

# edit drawing
def edit_drawing(request, drawing_id):
    drawing = get_object_or_404(AllDrawing, pk=drawing_id)
    if request.method == 'POST':
        form = AllDrawingForm(request.POST, request.FILES, instance=drawing)
        if form.is_valid():
            form.save()
            return redirect('all_drawings')
    else:
        form = AllDrawingForm(instance=drawing)
    return render(request, 'Drawings/edit_drawing.html', {'form': form, 'drawing': drawing})


#  for deleting the drawing

def delete_drawing(request, drawing_id):
    drawing = get_object_or_404(AllDrawing, pk=drawing_id)
    drawing.delete()
    return redirect('all_drawings')  # or 'all_drawings', depending where you want to land


def success_page(request):
    return render(request, 'success.html')



