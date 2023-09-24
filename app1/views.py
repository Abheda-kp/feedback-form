# views.py
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyModel

def input_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the data to the database
            MyModel.objects.create(name=name, email=email, message=message)

            # Redirect to a success page or do something else
            #return redirect('success_page')  # Replace 'success_page' with your actual success page URL name
    else:
        form = MyForm()

    return render(request, 'input.html', {'form': form})


