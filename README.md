# Django learning concepts.

## Study purpose. 

<br> Not in production. </br>

Language: Python
Framework: Django
Database: PostgreSQL


#### _1 - API's_

`Blog`
- Blog api to post questions and store it to database.

`Car`
 - Insert a driver and license and store it.

`Question`
- Post questions and manage it the way you want.

`UserMain`
-  User management. Create users, GET users and UPDATE users.

#### _2. Following the order above, URLS:_

`Blog`
- `blog/` 📰 will show the list of post made by people;
- `blog/post/` will create your post (requirements: Title, content, author(ForeignKey with CustomUser));
- `blog/id/` will get the post by its ID.

`Car`
- `cars/` will return a template html with all drivers and cars related to him;
-  `cars/create/` will create a driver/Car (Requirements: For driver: Name and License. <br>For car: );
-  `cars/id` will get the driver by their id and cars related to him;

`Questions`
- *TODO `questions/` will return all questions made and their authors;
- `questions/create/` Will create your question (Requirements: question)

`UserMain`
- `users/` will show all users created on db.
- `users/create/` this will create your user. (Requirements: username, password and email)