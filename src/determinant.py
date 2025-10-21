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
		if inp <= 9 and inp >= 2:
			return True
		else:
			return False
	except ValueError:
		return False


determinant_requirements = [
	{
		'name': 'size',
		'requirement': size_requirement, 
		'prompt': 'choose a size'
	}
]


def determinant_generator(parameters):
	size = int(parameters['size'])
	A = np.random.randint(-9, 10, size=(size,size))

	formula = ''
	for line in A:
		formula += '[ '
		for entry in line:
			if entry < 0:
				formula += str(entry)
			else:
				formula += f' {entry}'
			formula += ' '
		formula += ' ]\n'
	
	formula = formula.strip()

	ans = str(round(np.linalg.det(A)))

	return formula, ans


if __name__ == "__main__":
	engine(determinant_requirements, determinant_generator)

