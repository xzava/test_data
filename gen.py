# gen.py
"""
Create a python program using python3 that can take up to three named options and output a
csv file in a local directory of the server we execute it from.

Example:

	$ python gen.py '1,string' '2,integer' '3,string' --rows 100 --output_path "test_path"


Note: Spec suggested rows should be the first column, since it has a default and columns is required,
it makes sense to place `columns` first.

"""

import os
from datetime import datetime
import random
import string

import pandas as pd
import fire
import numpy as np

"""
FUNCTIONS:

	generate_csv()
	create_filename()
	generate_random_data()
	generate_random_string()
"""

def generate_csv(*column, rows=50, output_path=None):
	""" Entrypoint: generate dummy data.

	Note: path should be cleaned. https://stackoverflow.com/questions/13939120/sanitizing-a-file-path-in-python
	Note: Dont accept user defined paths.
	"""
	# Quick checks - Todo create a pydantic mdoel to ensure format and types.
	assert column, "Atleast one 'column' is required ie python gen.py 'first,string' 'second,string'"
	assert type(rows) == int, "'rows' must be a integer ie python gen.py 'first,string' --rows 10"
	assert rows != 0, "'rows' must be at least 1 ie python gen.py 'first,string' --rows 1"

	if output_path:
		assert os.path.isdir(output_path), "Optional arg 'output_path' path location does not exist. Leave blank for current folder."
	
	assert all(len(e)==2 for e in column), "Arg 'column' is not formatted corectly ie python gen.py <COLUMN_NAME>,<COLUMN_TYPE>"
	
	print("rows", rows) # 50
	print("output_path", output_path) # None
	print("column", column) #> column (('first', 'string'), ('second', 'string'))


	filename = create_filename() #> '2022-07-28-15_52_27.csv'
	df = generate_random_data(rows, column)

	filepath = os.path.join(output_path or '.', filename)
	df.to_csv(filepath, index=False)

	print("Dummy data CSV created.")


def create_filename(utc=False):
	""" Generate file name using current datetime, formatted as
		
		EXAMPLES:
			>>> create_filename() 
			'2022-07-28-15_52_27.csv'
			>>> create_filename(utc=True)
			'2022-07-28-03_52_30.csv'
		
		NOTES:
		 	https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

		REQUIRES:
			from datetime import datetime
	"""
	date_format = "%Y-%m-%d-%H_%M_%S" #> '2022-07-28-15_52_27'
	if utc:
		dt = datetime.utcnow()
	else:
		dt = datetime.now()
	return dt.strftime(date_format) + ".csv"


def generate_random_data(rows, columns):
	"""
		>>> generate_random_data(10, (("1", "string"), ("2", "integer"), ("3", "string")))
		      columns
		0   TAjSuonRZ
		1        IfwV
		2         KXe
		3          rG
		4         fwB
		5       iEltB
		6  sovhCvQViB
		7    oXCdTdus
		8           X
		9       PPzuH


		>>> generate_random_data(10, (("1", "string"), ("2", "integer"), ("3")))
		ValueError
	"""
	try:
		column_names = [e[0] for e in columns]
	except ValueError as e:
		print("Arg 'column' is not formatted corectly ie python gen.py <COLUMN_NAME>,<COLUMN_TYPE>")
		raise e	
	# Generate dataframe will all ints
	# df = pd.DataFrame(np.random.randint(0,100,size=(rows, columns)), columns=['A', 'B', "c"])
	df = pd.DataFrame(np.random.randint(0,100,size=(rows, len(columns))), columns=column_names)
	for each in columns:
		col_name, col_type = each
		if col_type == "string":
			df[col_name] = df[col_name].map(lambda x: generate_random_string())
	# Overwrite default value
	return df


def generate_random_string():
	""" Generate a random string min lenth of 1 max length of 10
	>>> generate_random_string()
	'MKNZI'
	>>> generate_random_string()
	'UheSFg'
	>>> generate_random_string()
	'BByRJSwEb'
	"""
	n = np.random.randint(1,11)
	return ''.join(random.choices(string.ascii_letters, k=n))


if __name__ == '__main__':
  fire.Fire(generate_csv)



  # TESTS


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


  """

  Spec.

  Create a python3 script, that when executed from the command line can accept up to three
  named options and output a csv file in a local directory of the server we execute it from.
  The first named option `rows` can only be specified once and is optional otherwise it must have
  a default value of 50. This will dictate the number of rows in the output csv file.
  The second named option `output_path` can only be specified once and is optional, this is to
  specify where we want the file to be saved. If not specified, the file will be saved in the current
  directory.
  The third named option is `column` and MUST be specified at least once but can be specified
  multiple times. The form of the argument must be: column_name,type. Type of the argument
  can be `integer` or `string`.
  If a required option is missing or is invalid you MUST show a message on how to use the
  program.
  The program must output a csv of n rows specified via the `rows` argument, the header
  specified in the `column` option via the column_name must appear in the csv file. We will
  generate different random data for each columns and rows of type integer (eg: 1,2,3000, ...) or
  string (alpha strings with a length between 1 and 10 characters)
  The csv filename must be of the form YYYY-MM-DD-HH_MM_SS.csv (eg:
  2018-04-27-6_50_55), using the time at which we are executing the program.
  Create a python program using python3 that can take up to three named options and output a
  csv file in a local directory of the server we execute it from.

  """



  # NOTES:


  # python gen.py 'first,string' 'second,string' --rows 20 --output_path 100
  # python gen.py

  # python gen.py 'first,string' 'second,string' --rows 20 --output_path 100
  # python gen.py 'first,string' 'second,string' --rows 20 --output_path 100
  # python gen.py '1,string' '2,integer' --rows 20 --output_path 100

  # START: '2022-07-28-15_52_27'
  # STOP:  '2022-07-28-16_39_05'
  # START '2022-07-28-17_26_26'