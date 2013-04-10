
f = open('data_compare_without_under_coma_dot_bracket.csv','r')
foo =open('finaldata.csv','a')
count = 0
for line in f:
	x = line
	words = x.split()

	for word in words:
		if word == 'in' or word == 'of' or word == 'is' or word == 'the' or word == 'a' or word == 'to' or word == 'for' or word == 'with' or word == 'and' or word == '0' or word == '1' or word == '2' or word == '3' or word == '4' or word == '5' or word == '6' or word == '7' or word == '8' or word == '9':
			count = count + 1

		else:
			foo.write(word + ' ')


	foo.write('\n')

print count
f.close()
foo.close()


