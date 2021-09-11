# todolistapp
Multiuser Todo App 

Software Details:
IDE: Pycharm
Frontend: HTML
Backend: Python
Framework: Django


This is basic TODO Application which incorporates CRUD functionalities and as well as has a MULTIUSER login feature which enables users to have their own customized todo lists. This platform would help the users to focus and priotize their task and get things done quickly.

The features provided by the web app are as follows:


SIGNUP PAGE
The signup form asks for user's details to create an account after which they will be directed to the login page.


LOGIN PAGE

Once the user is created the page is redirected to the login page which asks for username and password from the user. if the details are valid and the user exists he/she is redirected to his/her dashboard. The user cannot access the home page until he/she logins which is shown in the message as 'Please login to access the app'.


HOME PAGE

Once the user successfully logins he/she is directed to the home page where they can add their todos by submitting the task form. The Statistics section shows the total number of tasks added by the user and also the number of tasks completed and uncompleted. The recently added tasks are shown first followed by others. As its a multiuser login todo app he/she can only see thier respective todos. When the user gets authenticated then only they can access the logout option.


EDIT TODOS

If the user clicks the Edit button against any of thier todo they will be directed to a Edit Task page where the user can either edit their task or mark the task as completed.



DELETE TODOS

If the user clicks the delete button against any of thier todo, they will be directed to delete page where a confirmation is taken from the user so as to if they really want to delete the task. If the user clicks on submit they will be redirected to the home page with that task not shown in the todo list and if the user clicks on cancel the task is not deleted and they are redirected to the home page.
Here the meeting at 8pm-10pm task is deleted as shown below:

Through all the updates in the task form the statistics also keeps on changing.




