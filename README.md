# Post List Page Development

## Project structure

I structure this project because of the following reasons:

1. We have both server pages and APIs. I want to separate them so we can easily 
extend or move them to different services.
2. `models` can be shared packages when this project grows.
3. We can have multiple `*-pages` packages such `crm-pages`, `admin-pages`, etc.


```
src
    /conf
        /settings
            # This is base settings for whole project. 
            # It will get real value from environment variable.
            base.py
            
            # Developer can set whatever they want in this file.  
            local.py
            
            # If we need to set anything special for production, we can set it here.
            # This file does not include in the source code
            production.py
            
            # Configurations for unit test environment  
            test.py
         
        asgi.py
        wsgi.py
         
        # Root url for this project
        urls.py
         
    # Contains models.py of apps
    /models
        /comment
        /post
       
    # Contains API set of apps
    /apis
        /post
       
    # This is for public pages, we can have admin-pages, cms-pages, etc.
    /pages
        # Contains page set of apps
        /post
       
    # Contains HTML pages for apps    
    /templates
   
    # Contains static files for apps
    /assets
   
    manage.py
   
.gitignore
Pipfile
Pipfile.lock
README.md
```

## Front End

I use VueJS for handling action

## Usage Instruction

At root project

```
pip install pipenv
pipenv install

cd src

# Migrate database (sqlite in this case)
python manage.py migrate --settings=conf.settings.dev

# Feed sample data. It will create 50 posts and 5 comments for first and last posts.
python manage.py feeddata --settings=conf.settings.dev

# Run project
python manage.py runserver --settings=conf.settings.dev

# Run unit test
python manage.py test --settings=conf.settings.test
```