from django.shortcuts import render, redirect
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = Contact.objects.filter(pk=pk).first()
    if not contact:
        return redirect('contact_list')
    return render(request, 'contact_detail.html', {'contact': contact})

def contact_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        alt_phone = request.POST.get('alt_phone', '')
        image = request.FILES.get('image', None)
        Contact.objects.create(name=name, email=email, phone=phone, alt_phone=alt_phone, image=image)
        return redirect('contact_list')
    return render(request, 'contact_form.html')

def contact_update(request, pk):
    contact = Contact.objects.filter(pk=pk).first()
    if not contact:
        return redirect('contact_list')
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.alt_phone = request.POST.get('alt_phone', '')
        if 'image' in request.FILES:
            contact.image = request.FILES['image']
        contact.save()
        return redirect('contact_detail', pk=pk)
    return render(request, 'contact_form.html', {'contact': contact})

def contact_delete(request, pk):
    contact = Contact.objects.filter(pk=pk).first()
    if contact:
        contact.delete()
    return redirect('contact_list')

def call_contact(request, pk):
    contact = Contact.objects.filter(pk=pk).first()
    if not contact:
        return redirect('contact_list')
    return render(request, 'call_screen.html', {'contact': contact})