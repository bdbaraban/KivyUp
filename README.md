# KivyUp

A MarkDown text parser with simple, more intuitive syntax providing a much cleaner experience with writing markdown files, such as README's like this one! The GUI is inviting and clean supplying a much more pleasing experience for the inexperienced software engineer, especially during the undertaking of documentation. Hopefully this documentation equally illuminates and demarcates the capabilities of KivyUp.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for stable usage.

## Parsing

An interesting project because of the language parsing aspect and algorithmic thinking involved in accomplishing this efficiently. Working with the mutability of lists in python, the time complexity of parsing and translating strings, and nested formatting challenged our algorithmic thinking.

### Prerequisites

```
Python3
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the repo

```
git clone https://github.com/christopherchoe/KivyUp.git
```

Run the app in the home directory of the git repo

```
python3 main.py
```

You should see the GUI come up. You may then start to type in the KivyUp syntax:

## Headers
Input:
```
biggest: My Project Is This
```
Output
```
# My Project Is This
```

Input:
```
smaller: this is a smaller header
```
Output:
```
##### this is a smaller header
```

Input:
```
bold(THIS)
```
Output:
```
**THIS**
```

Input:
```
italics(THAT)
```
Output:
```
*THAT*
```


## Authors

* **Brennan Baraban** - *Kivy App Development* - [bdbaraban](https://github.com/bdbaraban)
* **Christopher Choe** - *Kivy App Development* - [christopherchoe](https://github.com/christopherchoe)
* **Wendy Leung** - *Kivy App Development* - [wendyiscoding](https://github.com/wendyiscoding)
* **Athena Deng** - *Kivy App Development* - [ad-egg](https://github.com/ad-egg)
* **Samie Azad** - *Kivy App Development* - [sazad44](https://github.com/sazad44)
