from django.contrib import admin
from .models import Stock, Credential, Wallet

# These three statements register the respective models in the database.
# These models can be viewed/managed by the site administrator at localhost:8000/admin

admin.site.register(Stock) # Portfolio model
admin.site.register(Credential) # Login credentials model
admin.site.register(Wallet) # Wallet model 
