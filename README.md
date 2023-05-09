# Installation Guide

  - Create a virtual environment
  - Download the code
  - Navigate to <code>/elite102Bankapp/</codecode>
  - Run the following command:
      - Windows: <code>py -m venv .venv</code>
      - Mac: <code>python -m venv .venv</code>
  
  - Navigate to <code>/elite102Bankapp/.venv</code>
  - Activate the virtual environment:
      - Windows: Navigate to /elite102Bankapp/.venv/scripts and run the command: <code>activate</code>
      - Mac: Navigate to /elite102Bankapp/.venv/bin and run the command: <code>source activate</code>
  - Install the following packages with your package manager (<code>pip</code> by default):
      - Django <code>pip install Django</code>
      - mysqlclient <code>pip install mysqlclient</code>
      
  - Navigate to <code>/elite102Bankapp/bankapp/bankapp</code>
  - Open <code>settings.py</code>
  - Find the <code>DATABASES</code> dictionary and change the following values from <code>'default</code>:
      - <code>ENGINE</code>: Don't change this unless you know what you're doing!
      - <code>NAME</code>: Change to your desired schema name (Don't make a schema, Django will handle that later)
      - <code>USER</code>: Change to the username of your MySQL root user
      - <code>PASSWORD</code>: Change to the password the afforementioned user
      - <code>URL</code>: Change to the IP that your MySQL server is hosted on. This default should work, but if it doesn't, try: <code>localhost</code> or <code>0.0.0.0</code>
      - <code>PORT</code>: Change to the port that your MySQL server is open to. You shouldn't have to change this unless you've done something special to your MySQL server.
  
  - Save & close <code>settings.py</code>
  - Navigate to <code>elite102Bankapp/bankapp/</code>
  - Run the following command -- These commands are similar to committing changes to a github repo:
      - Windows: <code>py manage.py makemigrations</code>
      - Mac: <code>python manage.py makemigrations</code>
      - If these don't work, ensure you've set up your virtual environment properly, and that you have an active MySQL server open.

  - Run the following command -- These commands are similar to pushing changes to a github repo:
			- Windows: <code>py manage.py migrate</code>
			- Mac: <code>python manage.py migrate</code>

	- Run the server:
			- Windows: <code>py manage.py runserver</code>
			- Mac: <code>python manage.py runserver</code>
	
	- Access the web server:
			- Open any browser and go to <code>127.0.0.1:8000</code>

	- You're running the app!
