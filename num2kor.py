import re

txtNum = ' 일 이 삼 사 오 육 칠 팔 구'.split(' ')
txtNum2 = '영 일 이 삼 사 오 육 칠 팔 구'.split(' ')
txtK = ' 십 백 천'.split(' ')
txtM = ' 만 억 조 경 해 서 양 간 정 극 항아사 아승기 나유타 불가사의'.split(' ')

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

def process(num):		
	regex = re.compile('^(\d+)\.(\d+)$')
	
	if (regex.match(str(num))):
		matches = regex.findall(str(num))[0]
		result_str = convert(matches[0]) + '쩜'
		for i in range(len(matches[1])):
			result_str = result_str + ' ' + txtNum2[int(str(matches[1][i]))]
		return result_str
	else:
		return convert(num)

def assertconversion(test, expected, name):
	test = process(test)
	if (test == expected) :
		print('test passed!')
	else :
		print('test case : ' + name + ', has failed!\n test result = ' + test + ', expected result = ' + expected)
	return

if __name__ == "__main__":
	# input as 12345, expected 일만 이천 삼백 사십 오
	test = 12345
	expected = '일만 이천 삼백 사십 오 '

	assertconversion(test, expected, 'test 1')

	# interactive
	userinput = input("Enter a number to convert to korean word : ")
	print(process(userinput))
	
	exit(0)
