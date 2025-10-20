import numpy as np

def ask_parameter(requirement, prompt):
	'''
	Ask user for a parameter value with requirement.

	Args:
		requirement: a function to decide if the value is valid:
			args
				inp: the input
			returns
				True: inp is valid
				False: inp is invalid
		prompt: a str to hint user what is a valid value.
	
	Returns:
		value: a valid parameter inp as value.
		None: get 'quit'
	'''
	while True:
		inp = input(prompt + '\n>>> ')
		if inp == 'quit':
			return None
		elif requirement(inp):
			return inp
		else:
			print(f'Invalid input: {inp}')



def define_parameters(requirements, ask_parameter):
	'''
	Ask user to difine the scale of game.

	Args:
		requirements: the parameter requiremnt list [{
			'name': parameter_name_str,
			'requirement': requirement_function,
			'prompt': prompt_str_for_valid_value,
			},{}]
		ask_parameter: a loop function to asker user for a parameter value: 
			args 
				requirement: a function to decide if the value valid.
				prompt: a str to hint user what is a valid value.
			returns 
				parameter_value: get a valid value
				None: get 'quit'
		
	Returns::
		parameters: the parameter dict {
			parameter_name_str1: parameter_value1,
			parameter_name_str2: parameter_value2,
			}
	'''
	parameters = {}

	for pointer in range(len(requirements)):
		name = requirements[pointer]['name']
		requirement = requirements[pointer]['requirement']
		prompt = requirements[pointer]['prompt']
		
		# call ask_parameter loop function
		value = ask_parameter(requirement, prompt)
		
		if value == None:
			return None
		else:
			parameters[name] = value

	return parameters


def gaming(parameters, generator):
	'''
	Repeatly generate formula, get input and compare with ans until quit

	Args:
		parameters: the parameter dict {
			parameter_name_str1: parameter_value1,
			parameter_name_str2: parameter_value2,
			}
		generator: a function to generate formula and the answer:
			args:
				parameters: dict for deciding the formula scale
			returns:
				formula: the formula str
				ans: the answer str

	Returns:
		None
	'''
	is_quitting = False

	# record progress
	num_wrong = 0
	num_total = 0
	progress_bar = ''

	while not is_quitting:
		formula, ans = generator(parameters)
			
		# progress bar
		print(f"Total  [{num_total}]\nCorrect[{num_total-num_wrong}]")
		inp = input(f"[<{progress_bar}>] ")
		if inp == 'quit':
			break
		wrong_once = False
		
		while True:
			print(f"\nCalculate:\n{formula}")
			inp = input('= ')
		
			if inp == ans:
				print('Correct!')
				break	
			elif inp == 'quit':
				is_quitting = True
				break
			else:
				if not wrong_once:
					wrong_once = True
				print('Try again!')

		if not is_quitting or wrong_once:
			num_total += 1
			if wrong_once:
				num_wrong += 1
				progress_bar += '*'
			else:
				progress_bar += '='
				

	# print the result
	if num_total:
		acu = round(100*(num_total-num_wrong)/num_total, 2)
		print(f'Total   [{num_total}]\nAccuracy[{acu}]')

	return None


def engine(requirements, generator):
	'''
	Ask parameters from user and enter game.

	Args:
		requirements: the parameter requiremnt list [{
			'name': parameter_name_str,
			'requirement': requirement_function
				args
					inp: the input
				returns
					True: inp is valid
					False: inp is invalid
			'prompt': prompt_str_for_valid_value,
			},{}]
		generator: a function to generate formula and the answer:
			args:
				parameters: dict for deciding the formula scale
			returns:
				formula: the formula str
				ans: the answer str
	
	Returns:
		None
	'''	
	parameters = define_parameters(requirements, ask_parameter)
	if parameters:
		gaming(parameters, generator)
	return None

