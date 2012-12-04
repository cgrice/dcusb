def convert(char):
	return alphabet[char]

alphabet = {
	
	' ' : {
		1 : [1, 1, 1],
		2 : [1, 1, 1],
		3 : [1, 1, 1],
		4 : [1, 1, 1],
		5 : [1, 1, 1],
		6 : [1, 1, 1],
		7 : [1, 1, 1],
	},

	':' : {
 		1 : [1, 0, 1],
		2 : [1, 0, 1],
		3 : [1, 1, 1],
		4 : [1, 1, 1],
		5 : [1, 1, 1],
		6 : [1, 0, 1],
		7 : [1, 0, 1],
	},

	'1' : {
		1 : [1, 1, 0, 1],
		2 : [1, 0, 0, 1],
		3 : [1, 1, 0, 1],
		4 : [1, 1, 0, 1],
		5 : [1, 1, 0, 1],
		6 : [1, 1, 0, 1],
		7 : [1, 0, 0, 0],
	},

	'2' : {
		1 : [1, 0, 0, 1],
		2 : [0, 1, 1, 0],
		3 : [1, 1, 1, 0],
		4 : [1, 1, 0, 1],
		5 : [1, 0, 1, 1],
		6 : [0, 1, 1, 1],
		7 : [0, 0, 0, 0],
	},

	'3' : {
		1 : [1, 0, 0, 1],
		2 : [0, 1, 1, 0],
		3 : [1, 1, 1, 0],
		4 : [1, 0, 0, 1],
		5 : [1, 1, 1, 0],
		6 : [0, 1, 1, 0],
		7 : [1, 0, 0, 1],
	},

	'4' : {
		1 : [1, 1, 0, 1],
		2 : [1, 0, 0, 1],
		3 : [0, 1, 0, 1],
		4 : [0, 0, 0, 0],
		5 : [1, 1, 0, 1],
		6 : [1, 1, 0, 1],
		7 : [1, 1, 0, 1],
	},

	'5' : {
		1 : [0, 0, 0, 0],
		2 : [0, 1, 1, 1],
		3 : [0, 0, 0, 1],
		4 : [1, 1, 1, 0],
		5 : [1, 1, 1, 0],
		6 : [0, 1, 1, 0],
		7 : [1, 0, 0, 1],
	},

	'6' : {
		1 : [1, 0, 0, 1],
		2 : [0, 1, 1, 0],
		3 : [0, 1, 1, 1],
		4 : [0, 0, 0, 1],
		5 : [0, 1, 1, 0],
		6 : [0, 1, 1, 0],
		7 : [1, 0, 0, 1],
	},

	'7' : {
		1 : [0, 0, 0, 0],
		2 : [1, 1, 1, 0],
		3 : [1, 1, 1, 0],
		4 : [1, 0, 0, 1],
		5 : [1, 0, 1, 1],
		6 : [1, 0, 1, 1],
		7 : [1, 0, 1, 1],
	},

	'8' : {
		1 : [1, 0, 0, 1],
		2 : [0, 1, 1, 0],
		3 : [0, 1, 1, 0],
		4 : [1, 0, 0, 1],
		5 : [0, 1, 1, 0],
		6 : [0, 1, 1, 0],
		7 : [1, 0, 0, 1],
	},

	'9' : {
		1 : [1, 0, 0, 1],
		2 : [0, 1, 1, 0],
		3 : [0, 1, 1, 0],
		4 : [1, 0, 0, 1],
		5 : [1, 1, 1, 0],
		6 : [0, 1, 1, 0],
		7 : [1, 0, 0, 1],
	},

	'0' : {
		1 : [1, 0, 0, 1],
		2 : [0, 1, 1, 0],
		3 : [0, 1, 1, 0],
		4 : [0, 1, 0, 0],
		5 : [0, 0, 1, 0],
		6 : [0, 1, 1, 0],
		7 : [1, 0, 0, 1],
	},

	'a' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [0, 0, 0, 1, 1],
		4 : [1, 1, 1, 0, 1],
		5 : [1, 0, 0, 1, 1],
		6 : [0, 1, 1, 0, 1],
		7 : [1, 0, 0, 0, 1],
	},
	
	'b' : {
		1 : [0, 1, 1, 1, 1],
		2 : [0, 1, 1, 1, 1],
		3 : [0, 1, 1, 1, 1],
		4 : [0, 0, 0, 1, 1],
		5 : [0, 1, 1, 0, 1],
		6 : [0, 1, 1, 0, 1],
		7 : [1, 0, 0, 1, 1],
	},
	
	'c' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 0, 0, 1, 1],
		4 : [0, 1, 1, 0, 1],
		5 : [0, 1, 1, 1, 1],
		6 : [0, 1, 1, 0, 1],
		7 : [1, 0, 0, 1, 1],
	},
	
	'd' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	
	'e' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	
	'f' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	
	'g' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	
	'h' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	
	'i' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	
	'j' : {
		1 : [1, 1, 1, 1, 1],
		2 : [1, 1, 1, 1, 1],
		3 : [1, 1, 1, 1, 1],
		4 : [1, 1, 1, 1, 1],
		5 : [1, 1, 1, 1, 1],
		6 : [1, 1, 1, 1, 1],
		7 : [1, 1, 1, 1, 1],
	},
	


}