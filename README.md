# **Django REST API**

## Social network 

## Routes:

- register/             register page           {POST}

- auth/
  - login/              login page              {POST}
  - logout/             logout page             {POST}

- api/ 
  - post/               list of all posts       {GET, POST}
  - post/<int:pk>/      info about one post     {GET, PUT, PATCH, DELETE}
  - my_post/            info about user posts   {GET}
  - like/               list of all likes       {GET, POST}
  - like/?post_id=      list of all likes       {GET, POST, DELETE}


