# Installation

1. Clone this repository: `git clone https://github.com/spencerwalls/stockApp.git`

2. `cd` into `stockApp/`: `cd stockApp/`

3. Create a Python virtualenv called `venv` (this step assumes that Python is installed): `python -m venv venv` 

4. Activate the Python virtualenv: `source venv/Scripts/activate`

5. Install the dependencies located in `requirements.txt`: `pip install -r requirements.txt`

6. Launch the application: `python stocks/manage.py runserver`

# About

- This is a basic stock-tracking app that allows users to login, search live stock rates,
add balance to their wallet, and buy/sell stocks in their portfolio. Still a work in progress. 

- Most of the important functionality may be found in the `views.py` file. This file is located in the `stockApp/stocks/stocks2` directory. The `stocks2` directory also contains the `templates` directory, which includes all
`html` files, and the `migrations` directory, which includes all files relevant to database updates.

- Database administration may be accessed via `localhost:8000/admin', whereby the administrator may add/delete objects to/from the database manually if need be. 
