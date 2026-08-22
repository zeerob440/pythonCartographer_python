# pythonCartographer

pythonCartographer is a continuously developed Python learning application. That allows users to add Python notes as they learn more about Python architecture and syntax. Software structure and syntax can be tricky to understand by reading textbooks alone. pythonCartographer takes sometimes aloof textbook information and allows the user to develop their own working model of the language with simple examples and plain language, thus supporting individual cognition. 

## Use case & Objectives

pythonCartographer is intended to be run in a terminal while an engineer develops other software programs. It is intended to act as a reference as the engineer writes system architecture, it is an interactive notebook essentially. 

## Features

- pythonCartographer is an interactive application.
- pythonCartographer can be run from a terminal.

## Tech Stack

pythonCartographer is written entirely in the Python programming language.

### Framework

No frameworks are intended to ever be used for pythonCartographer

### Libraries

As of pythonCartographer delta, no libraries are currently present. Several libraries will eventual be added such as:

- re
- math
- platform
- cryptography
- random
- sqlite3

### datatbase

As of pythonCartographer delta no databases exist. However, future development will include DB Browser

## Architecture

pythonCartographer is a minimalistic OOP program that uses @staticmethods that contain instructional programs for the user to interact with. Theses methods contain examples of Python structures and syntax. entry to the program is __main__.py, it provides the root menu fort he user to select topics they need to review. navigation.py serves as the orchestrator, and menu input sanitation. The other programs are instructional programs that cover Python architecture.

```
pythonCartographer/
├── __init__.py       ← establishes the package
├── __main__.py       ← executable package entry point
│
├── basics.py         ← module
├── depopulate_list.py
├── dicts.py
├── for_loops.py
├── functions.py
├── input_validation.py
├── inputs.py
├── lists.py
├── navigation.py
├── selections.py
├── while_loops.py
│
├── README.md
├── LICENSE
└── .gitignore
```

## Software Dependencies

None currently.

## Development

pythonCartographer started out as brutalist monolithic program that helped me learn Python, Git operations, and software design, it has been improved for four version (alpha - delta) and with each version as my understanding of python resolved, the program was refined, the examples were refined and "charted".

pythonCartographer delta broke the monolithic program into modules containing static methods to allow for a minimist OOP structure that is much easier to maintain.

pythonCartographer delta is the current version delta - delta IX will be used to add more Python lessons. Echo will convert the program to an installable package.

## Author

Proudly engineered by Zachary Roberts