# NaNLABS-challange

### How to run
1. Install flask ``pip install flask``
2. Run the app on port `5000` with `py ./TestTrello.py`
3. Open [Postman](http://postman.com)
4. Sign up into this [Trello board](https://trello.com/b/doVjUQRM/test)
5. Create a POST request to `http://localhost:5000/` with one of the following body:  

```json 
// To create a task
{
    "type": "task",
    "title": "test descripcion",
    "category": "maintenance"
}
```


```json 
// To create a bug
{
    "type": "bug",
    "description": "test descripcion"
}
```


```json 
// To create a issue
{
    "type": "issue",
    "title": "title issue",
    "description": "test descripcion"
}
```


