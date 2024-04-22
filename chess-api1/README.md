
# REST Chess solver

## Table of contents

- Description

- Requirements

- Installation

## Description

The project consists in creating a simple REST application supporting the game of chess





The algorithm, after completing the appropriate fields, gives us a list of possible moves or checks whether a move to a given field is possible

## Requirements

1. cd to the directory where requirements.txt is located
2. activate your virtualenv
3. run: **pip install -r requirements.txt** in your shell
## Instalation

To run the application you need:

1. cd to the directory where app.py is located

2. run: 
- export **FLASK_APP=hello.py**  
- set **FLASK_APP=hello.py** on Windows

3. run **flask run**

## Sample queries and answers

### Inquiry

*http://127.0.0.1:5000/api/v1/rook/A1/*

### answer

*{"availableMoves":["B1","C1","D1","E1","F1","G1","H1","A2","A3","A4","A5","A6","A7","A8"],
"currentField":"A1",
"error":null,
"figure":"rook"}*

### Inquiry

*http://127.0.0.1:5000/api/v1/rook/A1/A5/*

### answer

*{"currentField":"A1",
"destField":"A5",
"error":null,
"figure":"rook",
"move":"valid"}*

### Inquiry

*http://127.0.0.1:5000/api/v1/rook/A1/B3/*

### answer

*{"currentField":"A1",
"destField":"B3",
"error":"Current move is not permitted.",
"figure":"rook",
"move":"invalid"}*

