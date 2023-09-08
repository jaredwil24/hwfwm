# Postgresql/strawberry/graphql - He Who Fights With Monsters

Test project exploring the use of an API backend (strawberry) for postgress database connected to graphql. 

## Statup

Build the database
```
python3 build_db.py
```
Start graphql api
```
uvicorn main:app --reload
```


### Desired Endstate

Create a website which hosts a quiz that will tell users what their confluent essence is + essence combination
