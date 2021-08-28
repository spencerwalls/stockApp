from django import forms
from .models import Stock
from .models import Credential
from .models import Wallet

# These classes represent forms present in the application

class CredentialForm(forms.ModelForm):
    class Meta:
        model = Credential
        fields = ["email", "password"]
    
class StockForm(forms.ModelForm):
   class Meta:
       model = Stock
       fields = ["ticker"] 

class WalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ["balance"]