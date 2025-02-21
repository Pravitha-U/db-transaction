
# Django Signals - Using Database Transactions  

## Overview  
This project demonstrates how to use *Django's signals* with *database transactions* to ensure data consistency.  

## Steps to Run  

1. *Clone the Repository*  
   ```sh
   git clone <your-repo-url>
   cd <your-project-folder>

2. Setup Virtual Environment & Install Dependencies

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
pip install -r requirements.txt


3. Run Migrations & Start Server

python manage.py migrate  
python manage.py runserver


4. Test in Django Shell

python manage.py shell

Create a Transaction

from myapp.models import MyModel  
from django.db import transaction  

with transaction.atomic():  
    obj = MyModel.objects.create(name="Transaction Test")  
print("Transaction successful")




Expected Output

The transaction will be successfully committed, and the signal will execute.

If an error occurs inside the transaction block, changes will not be saved.


Files Modified

models.py → Defines the model

signals.py → Connects signal with the transaction

views.py → A test view to check transaction behavior



---
