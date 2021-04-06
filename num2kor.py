txtNum = ' 일 이 삼 사 오 육 칠 팔 구'.split(' ')
txtK = ' 십 백 천'.split(' ')
txtM = ' 만 억 조 경 해 서 양 간 정 극 항아사 아승기 나유타 불가사의'.split(' ')
txtDigit = ' 십 백 천 만 십만 백만 천만 억 십억 백억 천억 조 십조 백조 천조 경 십경 백경 천경 해 십해 백해 천해 서 십서 백서 천서 양 십양 백양 천양 구 십양 백양 구양 간 십간 백간 천간 정 십정 백정 천정 재 십정 백재 천재 극 십극 백극 천극 만극 항아사 십항아사 백항아사 천항아사 만항아사 아승기 십아승기 백아승기 천아승기 나유타 십나유타 백나유타 천나유타 불가사의'.split(' ')

#TODO: ADD conversion for decimals
txtPoint = '쩜'

def convert_helper(num):
	token = []
	# given integer num, convert it to string, then reverse it.
	revstr = str(num)[::-1]
	# tokenize each digit, process it, then put them together in reversed order.
	# reverse the tokens then put them together.
	# when special digits have 1 in front of them, remove it.
	for i in range(len(revstr)):
		special = txtNum[int(revstr[i])]
		if (special == '일' and i != 0):
			token.insert(0, txtK[i])
		else :	
			token.insert(0, txtNum[int(revstr[i])] + txtK[i])
	
	return (' ').join(token)
		
	

def convert(num):
	# split, 4 characters in each segment, perofrm convert_helper on them.
	# put them together, but make sure to have special digits between them.
	
	token = []
	result_str = ''
	index = 0
	revstr = str(num)[::-1]
	for i in range(int(len(str(num))/4) + 1):
		temp_str = str(revstr)[(4*i):(4*i+4)]
		temp_str = temp_str[::-1]
		result_str = convert_helper(temp_str)+txtM[i] + ' ' + result_str
	
	return result_str
		
		

def assertconversion(test, expected, name):
	test = convert(test)
	if (test == expected) :
		print('test passed!')
	else :
		print('test case : ' + name + ', has failed!\n test result = ' + test + ', expected result = ' + expected)
	return

if __name__ == "__main__":
	# input as 12345, expected 일만 이천 삼백 사십 오
	test = 12345
	expected = '일만 이천 삼백 사십 오'

	assertconversion(test, expected, 'test 1')

	# interactive
	userinput = input("Enter a number to convert to korean word : ")
	print(convert(userinput))
	
	exit(0)
