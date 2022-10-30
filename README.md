# Dream Planner
Everyone has a dream vacation in their bucketlist.  We're here to bring those dreams closer to reality with a budget tracker.  Users can post and share their dream vacation and calculate how much they need to save each week.  Once the user goes on their vacation, they can add actual expenses to the trips.


## Team Members
- VSPD - Valerie, Sean, Prija, Devin

## User Stories
* User can create, read, update, delete profile
* User can create, read, update, delete destination details.
* User can create, read, update, delete expense from a destination.
* User can estimate how much to save weekly based on budget and expected travel dates
* User can add expenses to each destination and view actuals vs budget and expenses by category charts
* User can mark/unmark trips as completed
* User can search cities for hotel deals
* User can access the app on any device

## Snapshot 
![Main Layout](/img/dreammain.png)
![Sign Layout](/img/destinations.png)
![Dashboard Layout](/img/dashboard.png)

## Wireframes
![Route](/img/hierarchy1.png) 
![Route](/img/hierarchy2.png) 
![Route](/img/hierarchy3.png) 

## ERDs
![ERD](/img/erdlayout.png)

## RESTful Routes

### User
| HTTP METHOD | URL              | CRUD    | Response                              |
| ----------- | ---------------- | ------- | ------------------------------------- |
| GET | `/users/:userId` | READ | Return a specific user profile |
| POST | `/users/register` | CREATE | Create a user profile |
| PUT | `/users/:userId` | UPDATE | Update a user profile in the database |
| DELETE | `/users/:userId` | DESTROY | Delete a user profile |


### Dream Destination
| HTTP METHOD | URL              | CRUD    | Response                              |
| ----------- | ---------------- | ------- | ------------------------------------- |
| GET | `/destinations` | READ | See a specific destination |
| POST | `/destinations/:destinationId` | CREATE | Add destination to profile |
| PUT | `/destinations/:destinationId/edit` | UPDATE | Ability to edit destination |
| DELETE | `/destinations/:destinationId/edit` | DESTROY | Delete destination details |


### Expense
| HTTP METHOD | URL              | CRUD    | Response                              |
| ----------- | ---------------- | ------- | ------------------------------------- |
| GET | `/destinations/:destinationId` | READ | Return expenses for a destination |
| POST | `/destinations/:destinationId/expenses/new` | CREATE | Create an expense |
| PUT | `/destinations/:destinationId/expense/:expenseId/edit` | UPDATE | Update an expense | 
| DELETE | `/destinations/:destinationId/` | DESTROY | Delete an expense  |

## Installation Instruction
* Fork and clone this repository to your local directory
* Navigate to the directory in your terminal and run ` python3 -m venv .env ` to create a virtual environment
* Run ` source .env/bin/activate ` to start a virtual environment
* Run ` pip3 install django ` to install django
* Run ` pip3 install psycopg2-binary ` to install psycopg2
* Run ` pip3 install djangorestframework django-cors-headers ` to install djangorestframework and django-cors-headers 
* Run ` pip3 install pip3 install djangorestframework-simplejwt ` to install djangorestframework-simplejwt
* CD to backend folder ` cd backend ` 
* Run ` python3 manage.py loaddata users.json ` to load user data
* Run ` python3 manage.py loaddata destinations.json ` to load destination data
* Run ` python3 manage.py runserver  ` to start the server
* Go to the <a href="https://github.com/devin-lynch/dreamplanner-client" target="_blank">client repository</a> and folow the installation instruction
* Once finished, use `npm start` in the client terminal to start your application

## Our Approach Used
We used the Miro to create the User Stories and mapped out the RESTful Routes.  We implemented a SCRUM dashboard using sticky notes.  

We set up the backend and designed a rough draft of how we wanted our site to look.  Then we tackled the front end routes to reach MVP.  After we got the site functional, we styled it with Tailwind.

We had daily stand ups with a checklist of Big Milestones and daily goals.  We ranked each item from high to low priority.  We tested and dedugged daily to polish the site until we were satisfied. 

## Tech Stack Used
- Django
- React
- Python
- PostgreSQL
- JavaScript
- Git and GitHub
- Tailwind
- Axios

## MVP goals
- [X] User can create, read update, delete profile
- [X] User can create, read, update, delete destination details.
- [X] User can create, read, update, delete expense from a destination.
- [X] Learn Django for react
- [X] Wire Framing
- [X] Task Tracking
- [X] CSS - Tailwind 

## Stretch Goals
- [X] API 
- [X] Expense Dashboard
- [ ] Social Page (view friends)
- [ ] Profile Photo
- [ ] Comments


## Major Hurdles 
A major hurdle we had to overcome was installing the backend with the jwt token.  We also learned how to use json fixtures with python.  We were able to implement the dashboard using an npm package & tailwind.  We're really proud of the last few days of styling with tailwind.   
