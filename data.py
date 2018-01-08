# initialize starting positions

def setGlobals():
	global current_pos
	current_pos = [0,0]

# define sensor positions
# pos_s1 = [0,-105]
# pos_s2 = [0,-210]
# pos_s3 = [0,-315]
# pos_s4 = [110,0]
# pos_s5 = [220,0]
#
# initval_s1 = 15
# initval_s2 = 109
# initval_s3 = 85
# initval_s4 = 112
# initval_s5 = 105


def processData(distances):#, gyro_val):
	if distances[0]-15 not in range(-20,20):
		current_pos[0] = distances[0]
		current_pos[1] = -105

	elif distances[1]-109 not in range(-20,20):
		current_pos[0] = distances[1]
		current_pos[1] = -210

	elif distances[2]-85 not in range(-20,20):
		current_pos[0] = distances[2]
		current_pos[1] = -315

	elif distances[3]-112 not in range(-20,20):
		current_pos[0] = 110
		current_pos[1] = distances[3]

	elif distances[4]-105 not in range(-20,20):
		current_pos[0] = 220
		current_pos[1] = distances[4]

	#else:
	#    scale = 1.5*1.5*9.81
	#    for i in range(0,3):
	#        current_pos[i] = gyro_val[i] * scale
	return current_pos[0],current_pos[1]
