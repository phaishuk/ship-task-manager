## [Ship-task-manager](https://github.com/phaishuk/ship-task-manager)

Imagine a time when we didn't have a cutting edge technologies and we have to organize our time efficiently.
This is a small web TODO application where we try to make easier life for sailors, and agregate their tasks in one place.

Here you have a general opportunities:
- **Create** new sailors simple profile, tasks on the board, positions for sailors, with a name and description.
- **Update** some existing sailors profiles, tasks by editing their title or description, and completed status.
- **Delete** tasks when they are no longer needed.
- **View** a list of all tasks, including their title, description, and completion status.

## Installation

**Important!** Asure that you receive `.env` file from me before installation. 
This file has all necessary sensitive data for project. Allocate it on the root folder, because without this project 
doesn't work. If we agree your review of this project, but you haven't received
`.env` yet please contact me on my telegram messenger (`@phaishuk`), or other available way.

> 👉 Download the code 

```angular2html
git clone https://github.com/phaishuk/ship-task-manager
cd ship-task-manager
```

> 👉 Install modules via `VENV`  

```angular2html
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

> 👉 Set Up Database

```angular2html
python manage.py migrate
```

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

Utilizing this app you can use next credentials auth: <br/>
username: `mr_sailor` <br/>
password: `12qwaszx` <br/>

<i>Hope you have a pleasure using this app!</i>

