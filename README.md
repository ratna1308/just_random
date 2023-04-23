
### Project structure
```
aggregproject1    ( project root )
├── Dockerfile    ( docker image configuration )
├── README.md     ( project documentation )
├── app           ( django project root - created using django-admin command )
│   ├── app
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py   ( django project settings )
│   │   ├── urls.py       ( django default root url conf )
│   │   └── wsgi.py
│   ├── core              ( django application 1 )
│   │   ├── __init__.py
│   │   ├── admin.py      ( auto-created when you start app )
│   │   ├── apps.py       ( auto-created when you start app )
│   │   ├── management    ( creating custom commands using django-admin interface ) 
│   │   │   ├── __init__.py
│   │   │   └── commands
│   │   ├── migrations    ( auto-created whenever DB migrations are performed )
│   │   │   └── __init__.py
│   │   ├── models.py     ( DB table DDLs - ORM way )
│   │   └── tests         ( directory for writing unit-tests )
│   │       ├── __init__.py
│   │       └── test_commands.py
│   └── manage.py
├── docker-compose.yml
├── requirements.dev.txt
├── requirements.txt

```


# STEPS

1. Go and create account on hub.docker.com
2. Complete docker installation 
3. Login to Docker Hub and click on Account Setting → Security → New Access
Token
4. Copy and store the access token at some safe place.
5. Go to https://github.com/prashant5nov/project1/ and fork project into your account
6. With above step project repository will reflect into your account
7. `git clone <https-url-copied-from-git-repo>`