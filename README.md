# Django learning concepts.

## Study purpose. 

<br> Not in production. </br>

1 - API's

    -Blog
        >blog api to post questions and store it to database.
    -car
        >Insert a driver and license and store it.
    -question
        >Post questions and manage it the way you want.
    -userMain
        >User management. Create users, GET users and UPDATE users.

2. Following the order above, URLS:
    @Blog
        * 'blog/' 📰 will show the list of post made by people
        * 'blog/post/' will create your post
            >Requirements: Title, content, author(ForeignKey with CustomUser)
        * 'blog/id/' will get the post by its ID.
    @Car
        * 'cars/' will return a template html with all drivers and cars related to him.
        * 'cars/create' will create a driver/Car
            >Requirements: For driver: Name and License. <br>For car:
        * 'cars/id' will get the driver by their id and cars related to him.
    @Questions