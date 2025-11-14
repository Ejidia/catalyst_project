from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.template.loader import get_template
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from .filters import StockFilter


def index(request):
    return render(request, 'ebook/index.html')


@login_required
def home(request):
    products = Stock.objects.all().order_by('-id')
    product_filters = StockFilter(request.GET, queryset=products)
    products = product_filters.qs
    return render(request, "ebook/home.html", {
        'products': products,
        'product_filters': product_filters,
        'is_admin': getattr(request.user, 'is_administrator', False)
    })

@login_required
def register(request):
    return render(request, "ebook/register.html")


@login_required
def logout(request):
    return render(request, "ebook/logout.html")


@login_required
def log_out(request):
    django_logout(request)
    return redirect('/')


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Stock, id=product_id)
    return render(request, "ebook/product_detail.html", {'product': product})


@login_required
def delete_detail(request, product_id):
    if not request.user.is_manager:
        return HttpResponseForbidden("You are not allowed to delete products.")
    
    # rest of the code...

    """if getattr(request.user, 'is_administrator', False):
        return HttpResponseForbidden("Admins are not allowed to delete products.")"""
    
    product = get_object_or_404(Stock, id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required
def edit_detail(request, product_id):
    if not request.user.is_manager:
        return HttpResponseForbidden("You are not allowed to edit products.")
    
    # rest of the code...

    """if getattr(request.user, 'is_administrator', False):
        return HttpResponseForbidden("Admins are not allowed to edit products.")"""
    
    
    product = get_object_or_404(Stock, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, "ebook/edit_product.html", {'form': form, 'product': product})


"""@login_required
def add_product(request):
    if getattr(request.user, 'is_administrator', False):
        return HttpResponseForbidden("Admins are not allowed to add products.")
"""
@login_required
def add_product(request):
    if not request.user.is_manager :
        return HttpResponseForbidden("You are not allowed to add products.")
    
    # rest of the code...

    
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StockForm()
    return render(request, 'ebook/add_product.html', {'form': form})


@login_required
def issue_item(request, pk):
    issued_item = get_object_or_404(Stock, id=pk)
    sales_form = SaleForm(request.POST)

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()

            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('receipt')

    return render(request, 'ebook/issue_item.html', {'sales_form': sales_form})


@login_required
def receipt(request):
    sales = Sales.objects.all().order_by('-id')
    return render(request, 'ebook/receipt.html', {'sales': sales})


@login_required
def receipt_detail(request, receipt_id):
    receipt = get_object_or_404(Sales, id=receipt_id)
    return render(request, 'ebook/receipt_detail.html', {'receipt': receipt})


@login_required
def all_sales(request):
    sales = Sales.objects.all().order_by('-id')
    total_expected = sum([items.get_total() or 0 for items in sales])
    total = sum([items.amount_received or 0 for items in sales])
    total_change = sum([items.get_change() or 0 for items in sales])
    net = total_expected - total
    return render(request, 'ebook/all_sales.html', {
        'sales': sales,
        'total': total,
        'total_change': total_change,
        'net': net,
        'total_expected': total_expected
    })

@login_required
def deffered_payments(request):
    if request.method == 'POST':
        form = Deffered_paymentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Deffered_paymentsForm()
    return render(request, 'ebook/deffered_payments.html', {'form': form})

@login_required
def deffered_payments_list(request):
    payment = Deffered_payments.objects.all().order_by('-id')
    return render(request, 'ebook/deffered_payments_list.html', {'payments': payment})


@login_required
def record_sales(request):
    if request.method == 'POST':
        sales_form = SaleForm(request.POST)
        if sales_form.is_valid():
            item_id = request.POST.get('item')
            issued_item = get_object_or_404(Stock, id=item_id)

            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()

            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('all_sales')

    else:
        sales_form = SaleForm()

    return render(request, 'ebook/record_sales.html', {'sales_form': sales_form})


@login_required
def add_to_stock(request, pk):
    issued_item = get_object_or_404(Stock, id=pk)
    form = AddForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['total_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            return redirect('home')
    return render(request, 'ebook/add_to_stock.html', {'form': form})

@login_required
def signup(request):
    if not getattr(request.user, 'is_administrator', False):  # assuming admin = owner
        return HttpResponseForbidden("Only the owner can add users.")
    ...

    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreation()
    return render(request, 'ebook/signup.html', {'form': form})

@login_required
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_administrator:
            login(request, user)
            return redirect('/owner_dashboard')

        if user is not None and user.is_manager:
            login(request, user)
            return redirect('/manager_dashboard')

        if user is not None and user.is_salesagent:
            login(request, user)
            return redirect('/salesagent_dashboard')

        print("Sorry!, something went wrong")

    form = AuthenticationForm()
    return render(request, 'ebook/login.html', {"form": form})


@login_required
def owner_dashboard(request):
    receipts = Receipt.objects.all().order_by('-date')
    total_sales = receipts.aggregate(total=Sum('amount_received'))['total'] or 0
    return render(request, 'ebook/owner_dashboard.html', {
        'receipts': receipts,
        'total_sales': total_sales
    })


@login_required
def manager_dashboard(request):
    return render(request, 'ebook/manager_dashboard.html')


@login_required
def salesagent_dashboard(request):
    return render(request, 'ebook/salesagent_dashboard.html')


@login_required
def final_receipt(request, receipt_id):
    if not (request.user.is_administrator or
            (hasattr(request.user, 'profile') and request.user.profile.role == 'owner')):
        return HttpResponseForbidden("You are not authorized to view this receipt.")

    receipt = get_object_or_404(Receipt, id=receipt_id)
    return render(request, 'ebook/receipt_detail.html', {'receipt': receipt})


