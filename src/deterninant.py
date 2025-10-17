import numpy as np

if __name__ == '__main__':
	inp = 0
	size = 0
	flag_cal = 0



	while True:

		inp = input('(choose a size)>>> ')
		try:
			inp = int(inp)
		except ValueError:
			pass
		
		if inp in range(2, 9):
			size = inp
			flag_cal = 1
			num_wrong = 0
			num_total = 0
			progress_bar = ''

			while flag_cal:
				A = np.random.randint(-9, 10, size=(size, size))
				det_A = str(round((np.linalg.det(A))))
				wrong_once = False

				print(f"Total  [{num_total}]\nCorrect[{num_total-num_wrong}]")
				inp = input(f"[<{progress_bar}>]")
				if inp == 'quit':
					break

				while True:
					print("\nCalculate: ")
					for line in A:
						f_line = '[ '
						for entry in line:
							if entry < 0:
								f_line += str(entry)
							else:
								f_line += f' {entry}'
							f_line += ' '

						f_line += ' ]'
						print(f_line)

					inp = input('>>> ')

					if inp == det_A:
						break
					elif inp == 'quit':
						flag_cal = 0
						break
					else:
						if not wrong_once:
							wrong_once = True
						print("Try again!")
				
				if flag_cal or wrong_once:
					num_total += 1
					if wrong_once:
						num_wrong += 1
						progress_bar += '*'
					else:
						progress_bar += '='

		elif inp == 'quit':
			break
		else:
			print(f'Invalid input: {inp}')
		
		if num_total:
			acu = round(100*(num_total-num_wrong)/num_total, 2)
			print(f'Total: {num_total}')
			print(f'Accuracy: {acu}%\n')
			
