# TopBlog

A blog with all the features you need for blogging, like creating, editing, viewing and deleting articles. There is a rich opportunity to design articles thanks to TinyMCE 4 editor.
TopBlog was fully written on Django - popular Python framework. MySQL was used as a database.

## Getting Started

### Requirements
- `python3.6`
- `mysql`

### Installing

In project folder create virtual environment
```
virtualenv -p python3 venv
```

Activate virtual environment
```
source venv/bin/activate
```

First, install essential packages for correct work django with mysql. 

`sudo apt-get install python3.6-dev libmysqlclient-dev` 

Install dependencies
```
pip install pip==18.0
pip install pipenv
pipenv install
```

## Run app
```
python src/manage.py runserver
```

## Run tests

```
python src/manage.py test
```

## Authors

* **Alex Gorbov** - [foobic](https://github.com/foobic)
* **Vlad Novosadenko** - [v-lad](https://github.com/v-lad)
* **Oleksandr Zhinzher** - [alle-zhinzher](https://github.com/alle-zhinzher)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

