# random-dog

random-dog is a module for getting dog images, it uses dogAPI: https://dog.ceo/dog-api/
The module creation was inspired by random-cat module (https://github.com/gravmatt/random-cat)

**Python 2 and 3 compatible**

## Installation

Install through **pip**.

```
$ pip install random-dog
```

or get from source

```
$ git clone https://github.com/Prasnal/random-dog
$ cd random-dog
$ python setup.py install
```

## Usage

The dog module has just one function **getDog()** with two optional arguments.

### Arguments

**directory** - default is the current directory

**filename** - default is a unique id

```
import dog

# dog.getDog(directory=None, filename=None)

dog.getDog(directory='/users/tor', filename='dog')

# /users/tor/dog.jpg
```

The function return the image name (absolute path if directory is specified) of the image.

### Command Line

You can also request an image on the terminal.

```
$ randomdog [format] [file]

# Example:

$ randomdog /users/tor/dog.jpg
```

The argument _file_ is optional.

The command return the filename/absolute path of the image to the standard output (stdout).

### Licence

The MIT License (MIT)
