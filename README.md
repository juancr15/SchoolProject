# School Project
### Top Gun Lab 2022
- Juan Diego Cruz
- Mauricio Henao

### Jump to...
1. Class Model
2. Project Set Up
3. Run project


## Class Model
![The School](https://user-images.githubusercontent.com/78455296/176267613-82bc8088-742d-461c-9e33-fffa72b6ff7b.png)

## Project Set Up

### Database
- [SQL Query](https://github.com/juancr15/SchoolProject/blob/master/DB/query.sql)
  > Before excecuting the query, you must create the database '**school**' or change the db name in the [Connection Script](https://github.com/juancr15/SchoolProject/blob/master/DB/connection.py#L17)
  
- [Connection script](https://github.com/juancr15/SchoolProject/blob/master/DB/connection.py)

### Python Virtual Environment

This project works with a Virtual Environment. You can activate the environment by executing the next script in the Windows PowerShell:
```
PS> env\Scripts\Activate.ps1
```

If you have trouble doing the previous step, install the next packages instead so the project can run correctly.
- **MySQL Connector**
```
pip install mysql-connector-python
```
- **Tabulate**
```
pip install tabulate
```

## Run project
Run the [main.py](https://github.com/juancr15/SchoolProject/blob/master/App/main.py) File in the App folder.
