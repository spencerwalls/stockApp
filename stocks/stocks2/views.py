from django.shortcuts import render, redirect
from .models import Stock
from .models import Credential
from .models import Wallet
from .forms import StockForm
from .forms import CredentialForm
from .forms import WalletForm

def addToWallet(request):

    # user is logged in if accessing wallet
    loggedIn = True

    if request.method == 'POST':

        # the database only ever contains one entry for the user's balance which is updated in real-time 
        if Wallet.objects.filter().first():
            currentBalance = float(Wallet.objects.filter().first().balance) 
            Wallet.objects.filter().first().delete()
            amountAdded = float(request.POST['balance']) 
            newBalance = round(currentBalance + amountAdded, 2) 
            updatedWallet = request.POST.copy()
            updatedWallet['balance'] = newBalance

            form = WalletForm(updatedWallet or None)
            if form.is_valid():
                form.save()

        # this else-block is only triggered if the user's wallet is empty
        else:
            updatedWallet = request.POST
            newBalance = request.POST['balance']
            form = WalletForm(updatedWallet or None)
            if form.is_valid():
                form.save()

        return render(request, 'addToWallet.html', {'balance': newBalance, 'loggedIn': loggedIn})

    # this else-block is triggered when the 'add to wallet' page is loaded from a GET request  
    else:
        if Wallet.objects.filter().first():
            currentBalance = float(Wallet.objects.filter().first().balance) 
        else:
            currentBalance = 0.00
        return render(request, 'addToWallet.html', {'loggedIn': loggedIn, 'balance': currentBalance})


def login(request):
    
    if request.method == 'POST':
        form = CredentialForm(request.POST or None)
        if form.is_valid():
            form.save()
            loggedIn = True
            return render(request, 'login.html', {'loggedIn': loggedIn})

    else:
        loggedIn = False
        return render(request, 'login.html', {'loggedIn': loggedIn})


def home(request):

    return render(request, 'home.html', {})


def searchLiveRates(request):

    import requests
    import json
    loggedIn = True

    if request.method == 'POST':
        ticker = request.POST['ticker']

        # this is the request made to the api which provides live stock rates
        liveRatesRequest = requests.get('https://cloud.iexapis.com/stable/stock/' + ticker + '/quote?token=pk_40aa5a1d6ca64c9b8392326cc8275b11')

        try:
            data = json.loads(liveRatesRequest.content) 
        except Exception as e:
            data = "Error"

        return render(request, 'searchLiveRates.html', {'data': data, 'loggedIn': 'loggedIn'})
        
    else:
        return render(request, 'searchLiveRates.html', {'loggedIn': loggedIn})


def buyStock(request):

    import requests
    import json
    loggedIn = True

    # if a new stock is being purchased, this adds it to the portfolio
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('buyStock')

    # otherwise the 'portfolio / buy stocks' page is simply loaded, displaying the user's portfolio 
    else:        
        allStocks = Stock.objects.all()
        for ticker in allStocks:

            liveRatesRequest = requests.get('https://cloud.iexapis.com/stable/stock/' + str(ticker) + '/quote?token=pk_40aa5a1d6ca64c9b8392326cc8275b11')

            try:
                data = json.loads(liveRatesRequest.content) 
            except Exception as e:
                data = "Error"

        return render(request, 'buyStock.html', {'allStocks':  allStocks, 'loggedIn': loggedIn})


def sellStock(request, stockId):

    # users can sell their stocks on the portfolio page 
    stock = Stock.objects.get(pk=stockId)
    stock.delete()
    return redirect(buyStock)