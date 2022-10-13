# AirBnB clone - The console #  :hotel:
![hbnb-logo](https://github.com/klmana/holbertonschool-AirBnB_clone/blob/356d9e5e0ed726c8559f1899a3e6fc31650da0fd/Image%2013-10-2022%20at%203.02%20pm.jpg)

## Description  :telescope:

This team project is part of the Holberton School Full-Stack Software Engineer program.
It's the first step towards building a first full web application: an AirBnB clone.
This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.
![programme](https://github.com/klmana/holbertonschool-AirBnB_clone/blob/356d9e5e0ed726c8559f1899a3e6fc31650da0fd/Image%2013-10-2022%20at%202.52%20pm.jpg)
![project](https://github.com/klmana/holbertonschool-AirBnB_clone/blob/356d9e5e0ed726c8559f1899a3e6fc31650da0fd/Image%2013-10-2022%20at%202.53%20pm.jpg)

## Compilation / Installation :wrench:

Clone this repository
```bash

git clone {repository}
```

Run the console
```bash
./console.py
```

Run any of the allowed commands (see table below)


## Requirements :raising_hand:
![requs](https://github.com/klmana/holbertonschool-AirBnB_clone/blob/356d9e5e0ed726c8559f1899a3e6fc31650da0fd/Image%2013-10-2022%20at%202.54%20pm.jpg)


## Examples
The console is executable both in interactive mode and non-interactive mode.
Displays a prompt **(hbnb)** and waits for the user input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

Non-interactive mode example

```bash
$ echo "help" | ./console.py
(hbnb)
```

## Testing :bomb:

Unittests for the AirBnB_clone project are listed in the [tests](./tests) 
folder. To run the entire test suite at once, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```



## Bugs :bug:
No known bugs at this time. 

## Authors
Hamish ROSS - [Github](https://github.com/Gotmished)  
Gem PHAN - [Github](https://github.com/RainInApril)
Karren NONYTA - [Github](https://github.com/klmana)
