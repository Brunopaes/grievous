## Grievous

Optimized for python 3.6

Project aimed in spam a text on whatsapp web. Better used with 
[Kenobi](https://github.com/caiorulli/kenobi).

----------------------

### Dependencies

For developers, python requirements could be find in the project's root. For installing the requirements, 
in your ___venv___ or ___anaconda env___, just run the following command:

`pip install -r requirements.txt`

----------------

### Project's Structure

```bash 
.
└── grievious
    ├── data
    │   ├── chromedriver
    │   └── settings.json
    ├── docs
    │   ├── reference_articles
    │   ├── ...
    │   └── CREDITS
    ├── src
    │   ├── __init__.py
    │   └── general_kenobi.py
    ├── tests
    │   └── unittests
    │       ├── data
    │       ├── test_general_kenobi.py
    │       └── __init__.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt
```

#### Directory description

- __data:__ The data dir. Group of non-script support files.
- __docs:__ The documentation dir.
- __src:__ The scripts & source code dir.
- __tests:__ The unittests dir.

-----------------------

### Usage Notes

#### Running

For running it, on the `~/src` directory just run the follow command:

`python general_kenobi.py` 

#### Notes

Better used with [Kenobi](https://github.com/caiorulli/kenobi).

---------------

### Versioning

This project is complete.

--------------