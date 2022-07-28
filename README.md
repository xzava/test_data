
Create a CSV file with dummy data.

## Getting started

### Start a venv

```
python3 -m venv venv
source venv/bin/activate
```

## Install requirements

`pip install -r requirements.txt`

## Example:

```bash
$ python gen.py '1,string' '2,integer' '3,string' --rows 100 --output_path "test_path"
```

`rows` and `output_path` are optional.

```bash
$ python gen.py '1,string' '2,integer' '3,string'
```

At least one column is needed

```bash
$ python gen.py '1,string'
```


- Default rows is `50`
- Default output_path is `CWD`

Note: Spec suggested rows should be the first column, since it has a default and columns is required,
it makes sense to place `columns` first.

Note: Python 3.9.13 was used, should work on anything 3.6 and up.


## Tests

```bash
make test
```

```
## TEST COLUMNS

## Test missing columns
# python gen.py

## Test columns
# python gen.py '1,string'

## Test broken columns
# python gen.py '1'
# python gen.py '1,string,mistake'


## TEST ROWS
## test missing rows
# python gen.py '1,string'
## test wrong type row
# python gen.py '1,string' --rows "hey"
## test too small row
# python gen.py '1,integer' --rows 0


## TEST PATH

## Test 'output_path'
# python gen.py '1,string' '2,integer' '3,string' --rows 100 --output_path "test_path"

## Test output path that doesn't exist
# python gen.py '1,string' '2,integer' '3,string' --rows 100 --output_path "test_pat"

## Test missing 'output_path'
# python gen.py '1,string' '2,integer' '3,string' --rows 100

```