from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a thank you page here.
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
