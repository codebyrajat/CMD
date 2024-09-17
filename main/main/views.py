from django.shortcuts import render,redirect,HttpResponse
from crud.models import Employee
from datetime import datetime
from django.db.models import Q

def home(request):
    emp = Employee.objects.all()
    data={
        'emp':emp,
    }
    return render(request,'home.html',data)

def add(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client_name = request.POST.get('client_name')
        contact_info = request.POST.get('contact_info')
        received_date = request.POST.get('received_date')
        inventory_received = request.POST.get('inventory_received')
        reported_issues = request.POST.get('reported_issues')
        client_notes = request.POST.get('client_notes')
        assigned_technician = request.POST.get('assigned_technician')
        estimated_amount = request.POST.get('estimated_amount')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        data = Employee(
            client_id = client_id,
            client_name = client_name,
            contact_info =contact_info,
            received_date = received_date,
            inventory_received = inventory_received,
            reported_issues = reported_issues,
            client_notes = client_notes,
            assigned_technician = assigned_technician,
            estimated_amount = estimated_amount,
            deadline = deadline,
            status = status,
        )
        data.save()
        return redirect('home')
    return render(request, 'home.html')

def edit (request):
    emp = Employee.objects.all()
    data = {
        'emp':emp,
    }
    return redirect(request,'home.html',data)

def update(request,id):
    if request.method == "POST":
        client_id = request.POST.get('client_id')
        client_name = request.POST.get('client_name')
        contact_info = request.POST.get('contact_info')
        received_date = request.POST.get('received_date')
        inventory_received = request.POST.get('inventory_received')
        reported_issues = request.POST.get('reported_issues')
        client_notes = request.POST.get('client_notes')
        assigned_technician = request.POST.get('assigned_technician')
        estimated_amount = request.POST.get('estimated_amount')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        data = Employee(
            id = id,
            client_id = client_id,
            client_name = client_name,
            contact_info =contact_info,
            received_date = received_date,
            inventory_received = inventory_received,
            reported_issues = reported_issues,
            client_notes = client_notes,
            assigned_technician = assigned_technician,
            estimated_amount = estimated_amount,
            deadline = deadline,
            status = status,
        )
        data.save()
        return redirect('home')
    return redirect(request, 'index.html')

def delete(request,id):
    emp = Employee.objects.filter(id = id)
    emp.delete()
    data ={
        'emp': emp,
    }
    return redirect('home')


def search(request):
    query = request.GET.get('query')
    if query:
        emp = Employee.objects.filter(
            Q(client_name__icontains=query) | Q(client_id__icontains=query)
        )
    else:
        emp = Employee.objects.all()
    data = {
        'emp': emp,
    }
    return render(request, 'home.html', data)

# def view (request,id):
#     emp = Employee.objects.filter(id=id)
#     data = {
#         'emp':emp,
#     }
#     return redirect(request,'home.html',data)

def view(request, id):
    emp = get_object_or_404(Employee, id=id)
    data = {
        'emp': emp,
    }
    return render(request,'home.html', data)