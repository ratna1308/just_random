1. `git pull origin main`
2. `docker-compose down`
3. `docker-compose up`
4. HTTP POST `http://localhost:8000/api/user/token/` with following payload - 
```text
{
    "email": "prashant@gmail.com",
    "password": "qwerty"
}
```