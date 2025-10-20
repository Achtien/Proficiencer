import numpy as np
from engine import engine

'''
def engine(requirements, generator):

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
	
def size_requirement(inp):
	try:
		inp = int(inp)
		if inp <= 9 and inp >= 1:
			return True
	except ValueError:
		return False

def operations_requirement(inp):
	inp = inp.split(' ')
	all_operations = ['+','-','*']
	operations = []
	for ope in inp:
		if ope in all_operations:
			operations.append(ope)
		else:
			return False
		
	if operations:
		return True
	else:
		return False


fundamental_requirements = [
	{
		'name': 'size',
		'requirement': size_requirement, 
		'prompt': 'choose a size'
	},
	{
		'name': 'operations',
		'requirement': operations_requirement,
		'prompt': 'choose operations(+ - *)'
	}
]


def fundamental_generator(parameters):
	size = int(parameters['size'])
	operations = parameters['operations'].split()
	# all_operations dict [(name_str, calculate_function), ()]
	all_operations = {
		'+': lambda a,b:a+b,
		'-': lambda a,b:a-b,
		'*': lambda a,b:a*b
		}
	random_num = lambda size: np.random.randint(-10**size+1, 10**size)
	random_ope = lambda operations: operations[np.random.randint(len(operations))]

	a = random_num(size)
	b = random_num(size)
	ope = random_ope(operations)

	formula = f'{a} {ope} {b}'
	ans = str(all_operations[ope](a, b))


	return formula, ans

if __name__ == "__main__":
	engine(fundamental_requirements, fundamental_generator)

