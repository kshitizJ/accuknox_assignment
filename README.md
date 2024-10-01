# AccuKnox assignment

## To run the assignment follow these steps:

1. Clone the project
- `git clone https://github.com/kshitizJ/accuknox_assignment.git`

2. Create a python virtual environment
- `python3 -m venv env`

3. Activate the python environment
- `source env/bin/activate`

4. Install the project requirements
- `pip3 install -r requirements.txt`

5. Now to run the project go to signal_assignment folder
- `cd signal_assignment/`

6. Now make migrations
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

7. Run the django project
- `python3 manage.py runserver`

8. When you open the localhost url in the browser you will see there is a delay this is where the signals start working.

9. I'm attaching the code output from my console here.

- Signals are executed synchronously
(https://raw.githubusercontent.com/kshitizJ/accuknox_assignment/refs/heads/master/images/Screenshot%20from%202024-10-01%2012-05-48.png)

- Signals run in the same thread of the caller function
(https://raw.githubusercontent.com/kshitizJ/accuknox_assignment/refs/heads/master/images/Screenshot%20from%202024-10-01%2012-21-14.png)

- Signals can run before or after the transaction in the database. Here in my case signal ran during the transaction was executed so we get the value `true`
(https://raw.githubusercontent.com/kshitizJ/accuknox_assignment/refs/heads/master/images/Screenshot%20from%202024-10-01%2012-25-18.png)

- I ran the `rectangle.py` file and got the following output
(https://raw.githubusercontent.com/kshitizJ/accuknox_assignment/refs/heads/master/images/Screenshot%20from%202024-10-01%2012-36-54.png)
