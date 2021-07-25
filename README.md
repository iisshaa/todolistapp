# todolistapp
Multiuser Todo App Using HTML, CSS, Bootstrap, Python, Django

This is basic TODO Application which incorporates CRUD functionalities and as well as has a MULTIUSER login feature which enables users to have their own customized todo lists. This platform would help the users to focus and priotize their task and get things done quickly.

The features provided by the web app are as follows:


SignUp Page

![Screenshot (195)](https://user-images.githubusercontent.com/69718746/126900985-4a0487cd-cb77-4435-82e5-55a8caf50311.png)

The signup form asks for user's details to create an account after which they will be directed to the login page.


Login Page

![Screenshot (196)](https://user-images.githubusercontent.com/69718746/126901044-9be0c1c7-e909-4f37-9dbd-41bfaf2e7f88.png)

Once the user is created the page is redirected to the login page which asks for username and password from the user. if the details are valid and the user exists he/she is redirected to his/her dashboard. The user cannot access the home page until he/she logins which is shown in the message as 'Please login to access the app'.


Home Page

![Screenshot (203)](https://user-images.githubusercontent.com/69718746/126902503-ba1ed061-e393-447a-92dc-2d770bc45de3.png)

Once the user successfully logins he/she is directed to the home page where they can add their todos by submitting the task form. The Statistics section shows the total number of tasks added by the user and also the number of tasks completed and uncompleted. The recently added tasks are shown first followed by others. As its a multiuser login todo app he/she can only see thier respective todos. When the user gets authenticated then only they can access the logout option.


Edit Todos

![Screenshot (204)](https://user-images.githubusercontent.com/69718746/126902568-da8fbb4d-54b6-4c77-b004-6417893be2b9.png)

If the user clicks the Edit button against any of thier todo they will be directed to a Edit Task page where the user can either edit their task or mark the task as completed.


The updated details are seen as:

![Screenshot (205)](https://user-images.githubusercontent.com/69718746/126902735-8a55e206-8dce-4b98-9650-855afe79f053.png)


Delete Tasks
![Screenshot (206)](https://user-images.githubusercontent.com/69718746/126902850-48145988-1b1c-4ccb-b9e6-223bbf9a84da.png)
If the user clicks the delete button against any of thier todo, they will be directed to delete page where a conformation is taken from the user so as to if they really want to delete the task if the user clicks on submit they will be redirected to the home page with that task not shown in the todo list and if the user clicks on cancel the task is not deleted and they are redirected to the home page.
Here the meeting at 8pm-10pm task is deleted as shown below:
![Screenshot (207)](https://user-images.githubusercontent.com/69718746/126903014-bc9ab95b-324d-41ee-9c2d-2e6ecea0c2c5.png)

Through all the updates in the task form the statistics also keeps on changing as seen above.


DJANGO ADMIN PAGE



