import sys
import random
import string
from math import floor, ceil, atan2, pi

DEBUG = False

SCALE = 20
SCALE_UP = 8

color_black            = 0
color_blue             = 1
color_green            = 2
color_red              = 4
color_brown            = 6
color_yellow           = 14
color_white            = 15
color_orange           = 25
color_lime             = 27
color_trans_light_blue = 43
color_light_bley       = 71
color_dark_bley        = 72


part_baseplate_32x32   = '3811'

part_plate_8x8         = '41539'
part_plate_6x6         = '3958'
part_plate_8x4         = '3035'
part_plate_4x4         = '3031'
part_plate_8x2         = '3034'
part_plate_6x2         = '3795'
part_plate_4x2         = '3020'
part_plate_2x2         = '3022'
part_plate_4x1         = '3710'
part_plate_2x1         = '3023'
part_plate_1x1         = '3024'

part_brick_4x2         = '3001'
part_brick_2x3         = '3002'
part_brick_4x1         = '3010'
part_brick_3x1         = '3622'
part_brick_2x2         = '3003'
part_brick_2x1         = '3004'
part_brick_1x1         = '3005'

part_tile_1x2          = '3069b'
part_tile_2x2          = '3068b'
part_tile_2x4          = '87079'
part_tile_1x6          = '6636'
part_tile_1x8          = '4162'

part_corner_2x2        = '2357'

part_arch_1x3          = '4490'
part_arch_1x4          = '3659'
part_arch_1x6          = '3455'
part_arch_1x8x2        = '3308'
part_arch_1x3x2        = '88292'

part_portcullis        = '89513'


part_sizes = {}

part_sizes[part_baseplate_32x32]   = ( 32, 32,  0 )

part_sizes[part_plate_8x8]         = (  8,  8,  1 )
part_sizes[part_plate_6x6]         = (  6,  6,  1 )
part_sizes[part_plate_8x4]         = (  8,  4,  1 )
part_sizes[part_plate_4x4]         = (  4,  4,  1 )
part_sizes[part_plate_8x2]         = (  8,  2,  1 )
part_sizes[part_plate_6x2]         = (  6,  2,  1 )
part_sizes[part_plate_4x2]         = (  4,  2,  1 )
part_sizes[part_plate_2x2]         = (  2,  2,  1 )
part_sizes[part_plate_4x1]         = (  4,  1,  1 )
part_sizes[part_plate_2x1]         = (  2,  1,  1 )
part_sizes[part_plate_1x1]         = (  1,  1,  1 )

part_sizes[part_brick_4x2]         = (  4,  2,  3 )
part_sizes[part_brick_2x3]         = (  2,  3,  3 )
part_sizes[part_brick_4x1]         = (  4,  1,  3 )
part_sizes[part_brick_3x1]         = (  3,  1,  3 )
part_sizes[part_brick_2x2]         = (  2,  2,  3 )
part_sizes[part_brick_2x1]         = (  2,  1,  3 )
part_sizes[part_brick_1x1]         = (  1,  1,  3 )

part_sizes[part_tile_1x2]          = (  1,  2,  1 )
part_sizes[part_tile_2x2]          = (  2,  2,  1 )
part_sizes[part_tile_2x4]          = (  2,  4,  1 )
part_sizes[part_tile_1x6]          = (  1,  6,  1 )
part_sizes[part_tile_1x8]          = (  1,  8,  1 )

part_sizes[part_corner_2x2]        = (  2,  2,  3 )

part_sizes[part_arch_1x3]          = (  1,  3,  3 )
part_sizes[part_arch_1x4]          = (  1,  4,  3 )
part_sizes[part_arch_1x6]          = (  1,  6,  3 )
part_sizes[part_arch_1x8x2]        = (  1,  8,  6 )
part_sizes[part_arch_1x3x2]        = (  1,  3,  6 )

part_sizes[part_portcullis]        = (  1,  9, 31 )


part_offsets = {}

part_offsets[part_brick_2x3]       = [(  10, -10,  0 ), ( -10,  10,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_tile_1x2]        = [(  10, -10,  0 ), ( -10,  10,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_tile_2x4]        = [(  20, -20,  0 ), ( -20,  20,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_tile_1x6]        = [(  50, -50,  0 ), ( -50,  50,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_tile_1x8]        = [(  70, -70,  0 ), ( -70,  70,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_corner_2x2]      = [( -10, -10,  0 ), (  10, -10,  0 ), ( 10,  10, 0 ), ( -10, 10, 0 )]
part_offsets[part_arch_1x3]        = [(  20, -20,  0 ), ( -20,  20,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_arch_1x4]        = [(  30, -30,  0 ), ( -30,  30,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_arch_1x6]        = [(  50, -50,  0 ), ( -50,  50,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_arch_1x8x2]      = [(  70, -70,  0 ), ( -70,  70,  0 ), (  0,   0, 0 ), (   0,  0, 0 )]
part_offsets[part_arch_1x3x2]      = [(   0, -20,  0 ), ( -20,   0,  0 ), (  0, -20, 0 ), ( -20,  0, 0 )]
part_offsets[part_portcullis]      = [(  80, -80, 28 ), ( -80,  80, 28 ), (  0,   0, 0 ), (   0,  0, 0 )]

part_rotations = {}
part_rotations[part_arch_1x3x2]    = [3, 0, 1, 2]

rotate_table_xy = [None for n in range(4)]
rotate_table_xy[0] = [1,0,0,0,1,0,0,0,1]
rotate_table_xy[1] = [0,0,-1,0,1,0,1,0,0]
rotate_table_xy[2] = [-1,0,0,0,1,0,0,0,-1]
rotate_table_xy[3] = [0,0,1,0,1,0,-1,0,0]

parts_plates = [part_plate_8x8, part_plate_8x4, part_plate_4x4, part_plate_8x2, part_plate_6x2, part_plate_4x2, part_plate_2x2, part_plate_4x1, part_plate_2x1, part_plate_1x1]
parts_bricks = [part_brick_4x2, part_brick_4x1, part_brick_3x1, part_brick_2x1, part_brick_1x1]

class Cell:
	WALL       = 1
	WINDOW     = 2
	DOOR       = 3
	PORTCULLIS = 4

def create_matrix(size):
	return [[False for x in range(size)] for x in range(size)] 

def copy_matrix(size, matrix):
	result = create_matrix(size)
	for y in range(size):
		for x in range(size):
			result[x][y] = matrix[x][y]
	return result

def combine_matrix(size, a, b):
	result = create_matrix(size)
	for y in range(size):
		for x in range(size):
			va = a[x][y]
			vb = b[x][y]
			result[x][y] = max(va, vb)
	return result

def points_to_matrix(size, points):
	matrix = create_matrix(size)
	for point in points:
		matrix[point[0]][point[1]] = True
	return matrix

def print_points(size, points, back, fore):
	for y in range(size):
		for x in range(size):
			if (x, y) in points:
				sys.stdout.write(fore)
			else:
				sys.stdout.write(back)
		sys.stdout.write('\n')

def print_matrix(size, matrix):
	for y in range(size):
		for x in range(size):
			value = matrix[x][y]
			if isinstance(value, bool):
				value = 1 if value else 0
			sys.stdout.write(str(value))
		sys.stdout.write('\n')

def filter_matrix(matrix, filter):
	size = len(matrix)
	result = create_matrix(size)
	for y in range(size):
		for x in range(size):
			result[x][y] = filter(x, y, matrix[x][y])
	return result

def emit_part(f, color, part, x, y, z, rxy = 0):
	size = part_sizes[part]
	x = SCALE * x + SCALE * size[0 if rxy % 2 == 0 else 1] / 2
	y = SCALE * y + SCALE * size[1 if rxy % 2 == 0 else 0] / 2
	z = SCALE_UP * -z - SCALE_UP * size[2]
	if part in part_offsets:
		offsets = part_offsets[part]
		x = x + offsets[rxy][0]
		y = y + offsets[rxy][1]
		z = z + offsets[rxy][2]
	if part in part_rotations:
		rxy = part_rotations[part][rxy]
	rxy = rotate_table_xy[rxy]
	f.write('1 %s %s %s %s %s %s %s %s %s %s %s %s %s %s.dat\n' % (color, x, z, y, rxy[0], rxy[1], rxy[2], rxy[3], rxy[4], rxy[5], rxy[6], rxy[7], rxy[8], part))

def export_header(f, file):
	f.write('0 Procedural Castle\n')
	f.write('0 Name: ' + file + '\n')
	f.write('0 Author: wlievens\n')
	f.write('0 ROTATION CENTER 0 0 0 1 "Custom"\n')
	f.write('0 ROTATION CONFIG 0 0\n')

def lay_bricks(size, matrix, parts):
	result = []
	repeat = True
	studmap = create_matrix(size)
	for y in range(size):
		for x in range(size):
			studmap[x][y] = 1 if matrix[x][y] else 0
	input_states = 1
	output_states = 2
	while repeat:
		repeat = False
		for x in range(size):
			for y in range(size):
				stud = studmap[x][y]
				if ((stud & input_states) != 0) and ((stud & output_states) == 0):
					for part in parts:
						part_size = part_sizes[part]
						if part_size[0] == part_size[1]:
							rotations = [False]
						else:
							rotations = [False, True]
						for rotated in rotations:
							part_width = part_size[1 if rotated else 0]
							part_height = part_size[0 if rotated else 1]
							ok = True
							for nx in range(x, x + part_width):
								for ny in range(y, y + part_height):
									if nx >= 0 and ny >= 0 and nx < size and ny < size and ((studmap[nx][ny] & input_states) != 0) and ((studmap[nx][ny] & output_states) == 0):
										continue
									ok = False
							if ok:
								for nx in range(x, x + part_width):
									for ny in range(y, y + part_height):
										studmap[nx][ny] |= output_states
								element = {}
								element['x'] = x
								element['y'] = y
								element['rotated'] = rotated
								element['part'] = part
								result.append(element)
								repeat = True
								break
	return result

	
def emit_part_list(f, z, color, list):
	for brick in list:
		emit_part(f, color, brick['part'], brick['x'], brick['y'], z, 1 if brick['rotated'] else 0)

		
def emit_step(f, name):
	f.write('0 STEP\n')
	f.write('0 WRITE %s\n' % name)


def fill_merlons_x(f, x1, x2, y, h, color):
	start = x1 + 1
	length = x2 - x1
	parts = length / 3
	remainder = length - parts * 3
	if remainder == 1:
		if parts > 0:
			emit_part(f, color, part_brick_1x1, x2, y, h, 0)
	if remainder == 2:
		start = start + 1
		emit_part(f, color, part_brick_1x1, x1, y, h, 0)
		emit_part(f, color, part_brick_1x1, x2, y, h, 0)
	for x in range(parts):
		emit_part(f, color, part_brick_2x1, start + x * 3, y, h, 0)
	if DEBUG:
		emit_part(f, color_black, part_brick_1x1, x1, y, h+3, 0)
		emit_part(f, color_black, part_brick_1x1, x2, y, h+3, 0)
	pass

def fill_merlons_y(f, x, y1, y2, h, color):
	start = y1 + 1
	length = y2 - y1
	parts = length / 3
	remainder = length - parts * 3
	if remainder == 1:
		if parts > 0:
			emit_part(f, color, part_brick_1x1, x, y2, h, 0)
	if remainder == 2:
		start = start + 1
		emit_part(f, color, part_brick_1x1, x, y1, h, 0)
		emit_part(f, color, part_brick_1x1, x, y2, h, 0)
	for y in range(parts):
		emit_part(f, color, part_brick_2x1, x, start + y * 3, h, 1)
	if DEBUG:
		emit_part(f, color_black, part_brick_1x1, x, y1, h+3, 0)
		emit_part(f, color_black, part_brick_1x1, x, y2, h+3, 0)
	pass

def export(file, size, river, riverbed, castle_outline, matrixes):
	f = open(file, 'w')
	export_header(f, file)
	# Generate background plates
	emit_step(f, 'background')
	for x in range(size / 32):
		for y in range(size / 32):
			emit_part(f, color_green, part_baseplate_32x32, 32 * x, 32 * y, 0)
			
	# Generate river
	emit_step(f, 'river')
	list = lay_bricks(size, river, parts_plates)
	emit_part_list(f, 0, color_trans_light_blue, list)
	
	# Generate riverbed in layers
	for n in [1, 2]:
		emit_step(f, 'riverbed %d' % n)
		grid = filter_matrix(riverbed, lambda x,y,v: v >= n)
		list = lay_bricks(size, grid, parts_plates)
		emit_part_list(f, n - 1, color_green, list)
		
	# DEBUG constructions
	if DEBUG:
		bmax = 15
		for n in range(bmax - 3):
			emit_part(f, color_black, part_brick_1x1, 4, 20 + 3 * n, 3, 0)
			emit_part(f, color_black, part_brick_1x1, bmax - n, 20 + 3 * n, 3, 0)
			emit_part(f, color_red, part_corner_2x2, 2, 20 + 3 * n, 6, 0)
			emit_part(f, color_red, part_corner_2x2, bmax - n + 1, 20 + 3 * n, 6, 1)
			fill_merlons_x(f, 4, bmax - n, 20 + 3 * n, 6, color_red)
		for n in range(bmax - 3):
			emit_part(f, color_black, part_brick_1x1, 3 * n, 4, 3, 0)
			emit_part(f, color_black, part_brick_1x1, 3 * n, bmax - n, 3, 0)
			emit_part(f, color_red, part_corner_2x2, 3 * n, 2, 6, 3)
			emit_part(f, color_red, part_corner_2x2, 3 * n, bmax - n + 1, 6, 0)
			fill_merlons_y(f, 3 * n, 4, bmax - n, 6, color_red)
	
	def scan_cells_down(x, y, layer):
		matrix = matrixes[layer]
		filter = matrix[x][y]
		width = 1
		for sx in range(x + 1, size):
			if matrix[sx][y] != filter:
				break
			width = width + 1
		height = 1
		for sy in range(y + 1, size):
			if matrix[x][sy] != filter:
				break
			height = height + 1
		layers = 1
		for sz in range(layer - 1, -1, -1):
			if matrixes[sz][x][y] != filter:
				break
			layers = layers + 1
		return (width, height, layers)
	
	def scan_cells_up(x, y, layer):
		matrix = matrixes[layer]
		filter = matrix[x][y]
		width = 1
		for sx in range(x + 1, size):
			if matrix[sx][y] != filter:
				break
			width = width + 1
		height = 1
		for sy in range(y + 1, size):
			if matrix[x][sy] != filter:
				break
			height = height + 1
		layers = 1
		for sz in range(layer, len(matrixes)):
			if matrixes[sz][x][y] != filter:
				break
			layers = layers + 1
		return (width, height, layers)
	
	def check_top_corner(matrix, next, x, y):
		filter = matrix[x][y]
		return matrix[x - 1][y] != filter and matrix[x][y - 1] != filter and (next is None or next[x][y] != filter)
	
	def check_bottom_corner(matrix, prev, x, y):
		filter = matrix[x][y]
		return matrix[x - 1][y] != filter and matrix[x][y - 1] != filter and (prev is None or prev[x][y] != filter)
		
	#emit_part(f, color_lime, part_arch_1x3x2, 0, 0, 0, 0)
	#emit_part(f, color_lime, part_arch_1x3x2, 0, 1, 0, 1)
	#emit_part(f, color_lime, part_arch_1x3x2, 0, 4, 0, 2)
	#emit_part(f, color_lime, part_arch_1x3x2, 0, 7, 0, 3)
	#emit_part(f, color_lime, part_tile_1x8, 0, 0, 0, 0)
	#emit_part(f, color_lime, part_tile_1x8, 0, 1, 0, 1)
	
	matrix_wall_list = []
	for matrix in matrixes:
		matrix_wall_list.append(create_matrix(size))
	for layer in range(len(matrixes)):
		matrix = matrixes[layer]
		emit_step(f, 'layer %s' % layer)
		color = color_light_bley
		prev = matrixes[layer - 1] if layer > 0 else None
		next = matrixes[layer + 1] if layer < len(matrixes) - 1 else None
		matrix_wall = matrix_wall_list[layer]
		for y in range(size):
			for x in range(size):
				cell = matrix[x][y]
				
				if cell == Cell.WALL:
					matrix_wall[x][y] = True
				
				if cell == Cell.WINDOW or cell == Cell.DOOR:
					# Detect first corner cell at bottom layer
					if check_bottom_corner(matrix, prev, x, y):
						(width, height, layers) = scan_cells_up(x, y, layer)
						orientation = width < height
						rotated = 1 if orientation else 0
						min_size = min(width, height)
						max_size = max(width, height)
						base = layer
						top = layer + layers - 1
						if cell == Cell.WINDOW:
							if max_size == 3 and min_size == 2:
								emit_part(f, color, part_tile_1x2, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, 1 - rotated)
							if max_size == 4 and min_size == 2:
								emit_part(f, color, part_tile_2x2, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
							if max_size == 6 and min_size == 2:
								emit_part(f, color, part_tile_2x4, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
							if max_size == 8 and min_size == 2:
								emit_part(f, color, part_tile_1x6, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
								emit_part(f, color, part_tile_1x6, x + 1, y + 1, base * 3, rotated)
							if max_size == 10 and min_size == 2:
								emit_part(f, color, part_tile_1x8, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
								emit_part(f, color, part_tile_1x8, x + 1, y + 1, base * 3, rotated)
						if max_size == 10 and min_size == 2:
							emit_part(f, color, part_plate_4x2, x + (0 if orientation else 3), y + (3 if orientation else 0), top * 3 - 1, rotated + 2)
						for d in range(min_size):
							sx = x + (d if orientation else 0)
							sy = y + (0 if orientation else d)
							fx = sx + (0 if orientation else width - 1)
							fy = sy + (height - 1 if orientation else 0)
							for z in range(base, top - (1 if max_size < 8 else 2)):
								matrix_wall_list[z][sx][sy] = True
								matrix_wall_list[z][fx][fy] = True
							if max_size >= 8:
								emit_part(f, color, part_arch_1x3x2, sx, sy, (top - 2) * 3, rotated)
								emit_part(f, color, part_arch_1x3x2, fx, fy, (top - 2) * 3, rotated + 2)
								matrix_wall_list[top - 1][sx][sy] = True
								matrix_wall_list[top - 1][fx][fy] = True
							elif max_size == 8:
								emit_part(f, color, part_arch_1x8x2, sx, sy, (top - 2) * 3, rotated)
							elif max_size == 6:
								emit_part(f, color, part_arch_1x6, sx, sy, (top - 1) * 3, rotated)
							elif max_size == 4:
								emit_part(f, color, part_arch_1x4, sx, sy, (top - 1) * 3, rotated)
							elif max_size == 3:
								emit_part(f, color, part_arch_1x3, sx, sy, (top - 1) * 3, rotated)
							else:
								emit_part(f, color_blue, part_brick_1x1, sx, sy, (top - 1) * 3, rotated)
		
				if cell == Cell.PORTCULLIS:
					# Detect first corner cell at top layer
					if check_top_corner(matrix, next, x, y):
						(width, height, layers) = scan_cells_down(x, y, layer)
						if width == 1 and height == 9 and layers == 11:
							emit_part(f, color_dark_bley, part_portcullis, x, y, layer * 3 - part_sizes[part_portcullis][2] + 2, 1)
	
	def check_matrix(matrix, x, y, w, h):
		for bx in range(w):
			for by in range(h):
				if not matrix[x + bx][y + by]:
					return False
		return True
	
	def fill_matrix(matrix, x, y, w, h, value):
		for bx in range(w):
			for by in range(h):
				matrix[x + bx][y + by] = value
	
	for layer in range(len(matrix_wall_list)):
		emit_step(f, 'wall ' + str(n))
		matrix_wall = matrix_wall_list[layer]
		offset = (layer % 2) * 2
		color = color_light_bley
		# X-aligned 4x2
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (x % 4 == offset) and (y % 2 == 0):
					if check_matrix(matrix_wall, x, y, 4, 2):
						emit_part(f, color, part_brick_4x2, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 4, 2, False)
		# Y-aligned 4x2
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (x % 2 == 0) and (y % 4 == offset):
					if check_matrix(matrix_wall, x, y, 2, 4):
						emit_part(f, color, part_brick_4x2, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 2, 4, False)
		# X-aligned 2x3
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 3, 2):
						emit_part(f, color, part_brick_2x3, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 3, 2, False)
		# Y-aligned 2x3
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 2, 3):
						emit_part(f, color, part_brick_2x3, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 2, 3, False)
		# X-aligned 4x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (x % 4 == offset):
					if check_matrix(matrix_wall, x, y, 4, 1):
						emit_part(f, color, part_brick_4x1, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 4, 1, False)
		# Y-aligned 4x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (y % 4 == offset):
					if check_matrix(matrix_wall, x, y, 1, 4):
						emit_part(f, color, part_brick_4x1, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 1, 4, False)
		# X-aligned 3x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 3, 1):
						emit_part(f, color, part_brick_3x1, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 3, 1, False)
		# Y-aligned 3x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 1, 3):
						emit_part(f, color, part_brick_3x1, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 1, 3, False)
		# 2x2 Corner
		for y in range(size - 1):
			for x in range(size - 1):
				if matrix_wall[x][y] and matrix_wall[x + 1][y] and matrix_wall[x][y + 1] and not matrix_wall[x + 1][y + 1]:
					emit_part(f, color, part_corner_2x2, x, y, layer * 3, 0)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
				if matrix_wall[x][y] and matrix_wall[x + 1][y] and matrix_wall[x + 1][y + 1] and not matrix_wall[x][y + 1]:
					emit_part(f, color, part_corner_2x2, x, y, layer * 3, 1)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
				if matrix_wall[x][y] and matrix_wall[x][y + 1] and matrix_wall[x + 1][y + 1] and not matrix_wall[x + 1][y]:
					emit_part(f, color, part_corner_2x2, x, y, layer * 3, 3)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
				if not matrix_wall[x][y] and matrix_wall[x][y + 1] and matrix_wall[x + 1][y + 1] and matrix_wall[x + 1][y]:
					emit_part(f, color, part_corner_2x2, x, y, layer * 3, 2)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
		# 2x2
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 2, 2):
						emit_part(f, color, part_brick_2x2, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 2, 2, False)
		# X-aligned 2x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 2, 1):
						emit_part(f, color, part_brick_2x1, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 2, 1, False)
		# Y-aligned 2x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 1, 2):
						emit_part(f, color, part_brick_2x1, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 1, 2, False)
		# 1x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					emit_part(f, color, part_brick_1x1, x, y, layer * 3, 0)

	# Castle outline
	pi2 = 2 * pi
	count = len(castle_outline)
	concave_angles = []
	for n in range(count):
		p1 = castle_outline[(count + n - 1) % count]
		p2 = castle_outline[(count + n + 0) % count]
		p3 = castle_outline[(count + n + 1) % count]
		px1 = p1[0]
		py1 = p1[1]
		px2 = p2[0]
		py2 = p2[1]
		px3 = p3[0]
		py3 = p3[1]
		angle = (pi2 + atan2(py3 - py2, px3 - px2) - atan2(py2 - py1, px2 - px1)) % pi2
		concave_angles.append(angle > pi)
	
	wall_height = 8
	for h in range(wall_height):
		emit_step(f, 'wall ' + str(n))
		h3 = h * 3
		odd = (h % 2) == 1
		offset = 2 if odd else 0
		for n in range(count):
			p1 = castle_outline[(n + 0) % count]
			p2 = castle_outline[(n + 1) % count]
			px1 = p1[0]
			py1 = p1[1]
			px2 = p2[0]
			py2 = p2[1]
			if px1 == px2:
				x = px1 + 1
				if py1 < py2:
					color = color_light_bley
					if DEBUG:
						color = color_yellow
					y1 = py1
					y2 = py2
				else:
					color = color_light_bley
					if DEBUG:
						color = color_red
					y1 = py2 + 2 - (4 if odd else 0)
					y2 = py1 + 2 - (4 if odd else 0)
				for y in range(y1, y2, 4):
					color = color_light_bley if random.random() > 0.2 else color_dark_bley
					emit_part(f, color, part_brick_4x2, x - 1, y + offset, h3, 1)
			if py1 == py2:
				y = py1
				if px1 < px2:
					color = color_light_bley
					if DEBUG:
						color = color_lime
					x1 = px1 + (4 if odd else 0)
					x2 = px2 + (4 if odd else 0)
				else:
					color = color_light_bley
					if DEBUG:
						color = color_blue
					x1 = px2 + 2
					x2 = px1 + 2
				for x in range(x1, x2, 4):
					color = color_light_bley if random.random() > 0.2 else color_dark_bley
					emit_part(f, color, part_brick_4x2, x - offset, y, h3, 0)

	emit_step(f, 'parapet')
	parapet_height = 2
	for n in range(count):
		concave0 = concave_angles[(n + 0) % count]
		concave1 = concave_angles[(n + 1) % count]
		p1 = castle_outline[(n + 0) % count]
		p2 = castle_outline[(n + 1) % count]
		px1 = p1[0]
		py1 = p1[1]
		px2 = p2[0]
		py2 = p2[1]
		# check towers
		if p1[2] or p2[2]:
			pass
		for h in range(parapet_height):
			h3 = (wall_height + h) * 3
			odd = (h % 2) == 1
			offset = 2 if odd else 0
			if px1 == px2:
				x = px1 + 1
				if py1 < py2:
					color = color_light_bley
					if DEBUG:
						color = color_yellow
					reverse = False
					y1 = py1
					y2 = py2
					if odd:
						if not concave0:
							emit_part(f, color, part_brick_1x1, x, y1 + 1, h3, 1)
					else:
						if concave0:
							emit_part(f, color, part_brick_3x1, x, y1 + 1, h3, 1)
						else:
							emit_part(f, color, part_brick_4x1, x, y1, h3, 1)
					for y in range(y1 + (2 if odd else 4), y2 - (4 if odd else 2), 4):
						emit_part(f, color, part_brick_4x1, x, y, h3, 1)
					if odd:
						if concave1:
							emit_part(f, color, part_brick_3x1, x, y2 - 2, h3, 1)
						else:
							emit_part(f, color, part_brick_4x1, x, y2 - 2, h3, 1)
					if not odd and not concave1:
						emit_part(f, color, part_brick_1x1, x, y2, h3, 0)
				else:
					color = color_light_bley
					if DEBUG:
						color = color_red
					reverse = True
					y1 = py2 + 2 - (4 if odd else 0)
					y2 = py1 + 2 - (4 if odd else 0)
					if odd:
						emit_part(f, color, part_brick_3x1, x - 1, y1 + 3, h3, 1)
					else:
						if not concave1:
							emit_part(f, color, part_brick_1x1, x - 1, y1 - 1, h3, 0)
					for y in range(y1 + (6 if odd else 0), y2 - (2 if odd else 6), 4):
						emit_part(f, color, part_brick_4x1, x - 1, y, h3, 1)
					if odd:
						emit_part(f, color, part_brick_4x1, x - 1, y2 - (2 if odd else 4), h3, 1)
						if not concave0:
							emit_part(f, color, part_brick_1x1, x - 1, y2 + 2, h3, 0)
					else:
						if concave0:
							emit_part(f, color, part_brick_3x1, x - 1, y2 - 4, h3, 1)
						else:
							emit_part(f, color, part_brick_4x1, x - 1, y2 - (2 if odd else 4), h3, 1)
			if py1 == py2:
				y = py1
				if px1 < px2:
					color = color_light_bley
					if DEBUG:
						color = color_lime
					reverse = False
					x1 = px1 + (4 if odd else 0)
					x2 = px2 + (4 if odd else 0)
					if odd or not concave0:
						emit_part(f, color, part_brick_4x1, x1 - (2 if odd else 0), y, h3, 0)
					if not odd and concave0:
						emit_part(f, color, part_brick_3x1, x1 + 1, y, h3, 0)
					if odd and not concave0:
						emit_part(f, color, part_brick_2x1, x1 - 4, y, h3, 0)
					for x in range(x1 + 4 - (2 if odd else 0), x2 - 7, 4):
						emit_part(f, color, part_brick_4x1, x, y, h3, 0)
					if not odd or not concave1:
						emit_part(f, color, part_brick_4x1, x2 - (6 if odd else 4), y, h3, 0)
					if odd and concave1:
						emit_part(f, color, part_brick_3x1, x2 - (6 if odd else 4), y, h3, 0)
					if not odd and not concave1:
						emit_part(f, color, part_brick_1x1, x2, y, h3, 0)
				else:
					color = color_light_bley
					if DEBUG:
						color = color_blue
					reverse = True
					x1 = px2 + 2
					x2 = px1 + 2
					if odd:
						if concave1:
							emit_part(f, color, part_brick_3x1, x1 - 1, y + 1, h3, 0)
						else:
							emit_part(f, color, part_brick_4x1, x1 - 2, y + 1, h3, 0)
					else:
						emit_part(f, color, part_brick_4x1, x1, y + 1, h3, 0)
						if not concave1:
							emit_part(f, color, part_brick_1x1, x1 - 1, y + 1, h3, 0)
					for x in range(x1 + (2 if odd else 4), x2 - (2 if odd else 6), 4):
						emit_part(f, color, part_brick_4x1, x, y + 1, h3, 0)
					if odd:
						if not concave0:
							emit_part(f, color, part_brick_1x1, x2 - 2, y + 1, h3, 0)
					else:
						if concave0:
							emit_part(f, color, part_brick_3x1, x2 - 4, y + 1, h3, 0)
						else:
							emit_part(f, color, part_brick_4x1, x2 - 4, y + 1, h3, 0)

	emit_step(f, 'towers')
	tower_height = 16
	for n in range(count):
		concave0 = concave_angles[(n - 1 + count) % count]
		concave1 = concave_angles[(n + 0 + count) % count]
		concave2 = concave_angles[(n + 1 + count) % count]
		p0 = castle_outline[(n - 1 + count) % count]
		p1 = castle_outline[(n + 0 + count) % count]
		p2 = castle_outline[(n + 1 + count) % count]
		if p1[2]:
			px0 = p0[0]
			py0 = p0[1]
			px1 = p1[0]
			py1 = p1[1]
			px2 = p2[0]
			py2 = p2[1]
			print 'tower'
			for h in range(tower_height):
				emit_part(f, color, part_brick_1x1, px1, py1, (wall_height + parapet_height + h) * 3, 0)

	emit_step(f, 'walking planks ' + str(n))
	plank_width = 4
	grid_planks  = create_matrix(size)
	for h in range(2):
		odd = (h % 2) == 1
		for n in range(count):
			concave0 = concave_angles[(n + 0) % count]
			p1 = castle_outline[(n + 0) % count]
			p2 = castle_outline[(n + 1) % count]
			px1 = p1[0]
			py1 = p1[1]
			px2 = p2[0]
			py2 = p2[1]
			if px1 == px2:
				x = px1 + 1
				if py1 < py2:
					y1 = py1
					y2 = py2
					for py in range(y1 + 1, y2 + 1):
						for px in range(x - plank_width, x):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x - plank_width, x):
							for py in range(y1 + 1 - plank_width, y1 + 1):
								grid_planks[px][py] = True
				else:
					y1 = py2 + 2 - (4 if odd else 0)
					y2 = py1 + 2 - (4 if odd else 0)
					for py in range(y1 + 3, y2 - 1):
						for px in range(x, x + plank_width):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x, x + plank_width):
							for py in range(y2 - 1, y2 - 1 + plank_width):
								grid_planks[px][py] = True
			if py1 == py2:
				y = py1
				if px1 < px2:
					x1 = px1 + (4 if odd else 0)
					x2 = px2 + (4 if odd else 0)
					for px in range(x1 + 1, x2 - 3):
						for py in range(y + 1, y + 1 + plank_width):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x1 - plank_width + 1, x1 + 1):
							for py in range(y + 1, y + 1 + plank_width):
								grid_planks[px][py] = True
				else:
					x1 = px2 + 2
					x2 = px1 + 2
					for px in range(x1 - 1, x2 - 1):
						for py in range(y + 1 - plank_width, y + 1):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x2 - 1, x2 - 1 + plank_width):
							for py in range(y + 1 - plank_width, y + 1):
								grid_planks[px][py] = True
	list = lay_bricks(size, grid_planks, parts_plates)
	emit_part_list(f, wall_height * 3, color_brown, list)
	
	emit_step(f, 'merlons')
	h3 = (wall_height + parapet_height) * 3
	odd = (wall_height + parapet_height) % 2 == 1
	color = color_light_bley
	for n in range(count):
		concave0 = concave_angles[(n + 0) % count]
		concave1 = concave_angles[(n + 1) % count]
		p1 = castle_outline[(n + 0) % count]
		p2 = castle_outline[(n + 1) % count]
		# skip towers
		if p1[2] or p2[2]:
			continue
		px1 = p1[0]
		py1 = p1[1]
		px2 = p2[0]
		py2 = p2[1]
		if px1 == px2:
			x = px1 + 1
			if py1 < py2:
				y1 = py1
				y2 = py2
				if concave0:
					emit_part(f, color, part_corner_2x2, px1 + 1, py1 + 1, h3, 0)
				else:
					emit_part(f, color, part_corner_2x2, px1, py1, h3, 1)
				fill_merlons_y(f, px1 + 1, y1 + 2, y2 - (2 if concave1 else 1), h3, color)
			else:
				y1 = py2 + 2 - (4 if odd else 0)
				y2 = py1 + 2 - (4 if odd else 0)
				if concave0:
					emit_part(f, color, part_corner_2x2, px1 - 1, py1 - 1, h3, 2)
				else:
					emit_part(f, color, part_corner_2x2, px1, py1, h3, 3)
				fill_merlons_y(f, px1, y1 + (1 if concave1 else 0), y2 - (4 if concave0 else 3), h3, color)
		if py1 == py2:
			y = py1
			if px1 < px2:
				x1 = px1 + (4 if odd else 0)
				x2 = px2 + (4 if odd else 0)
				if concave0:
					emit_part(f, color, part_corner_2x2, px1 + 1, py1 - 1, h3, 3)
				else:
					emit_part(f, color, part_corner_2x2, px1, py1, h3, 0)
				fill_merlons_x(f, x1 + (3 if concave0 else 2), x2 - (2 if concave1 else 1), py1, h3, color)
			else:
				x1 = px2 + 2
				x2 = px1 + 2
				fill_merlons_x(f, x1 + (1 if concave1 else 0), x2 - (4 if concave0 else 3), py1 + 1, h3, color)
				if concave0:
					emit_part(f, color, part_corner_2x2, px1 - 1, py1 + 1, h3, 1)
				else:
					emit_part(f, color, part_corner_2x2, px1, py1, h3, 2)

	emit_step(f, 'minifigures')
	f.write('1 71 %s -362 %s 0 0 1 0 1 0 -1 0 0 dude.ldr\n' % (36 * SCALE + SCALE / 2, 30 * SCALE))
	f.write('1 71 %s -362 %s 0 0 1 0 1 0 -1 0 0 dude.ldr\n' % (36 * SCALE + SCALE / 2, 35 * SCALE))
	f.write('1 71 %s -362 %s 0 0 1 0 1 0 -1 0 0 dude.ldr\n' % (36 * SCALE + SCALE / 2, 40 * SCALE))
	f.write('1 71 %s -362 %s 0 0 1 0 1 0 -1 0 0 dude.ldr\n' % (36 * SCALE + SCALE / 2, 45 * SCALE))
	f.write('1 71 %s -362 %s 0 0 1 0 1 0 -1 0 0 dude.ldr\n' % (36 * SCALE + SCALE / 2, 50 * SCALE))
	f.write('1 71 %s -362 %s 0 0 1 0 1 0 -1 0 0 dude.ldr\n' % (36 * SCALE + SCALE / 2, 69 * SCALE))

	f.write('0\n')

	
def generate_river_path(size):
	path = []
	margin = 8
	start_x = random.randint(margin, 16)
	x = start_x
	deviation = 1
	for y in range(size):
		path.append((x, y))
		if x < margin:
			x = x + random.randint(0, +deviation)
		elif x > size - margin - 1:
			x = x + random.randint(-deviation, 0)
		else:
			x = x + random.randint(-deviation, +deviation)
	return path

	
def generate_river(size):
	path = generate_river_path(map_size)
	grid = create_matrix(size)
	for point in path:
		px = point[0]
		py = point[1]
		extent = random.randint(2, 3)
		for x in range(max(0, px - extent), min(size, px + extent + 1)):
			for y in range(max(0, py - extent), min(size, py + extent + 1)):
				grid[x][y] = True
	return grid

	
def distance8(x1, y1, x2, y2):
	return max(abs(x1-x2), abs(y1-y2))

	
def generate_riverbed(size, river):
	grid = create_matrix(size)
	for y in range(size):
		for x in range(size):
			grid[x][y] = 0
			if river[x][y]:
				continue
			extent = random.randint(4, 6)
			nearest = extent
			for nx in range(max(0, x - extent), min(size, x + extent + 1)):
				for ny in range(max(0, y - extent), min(size, y + extent + 1)):
					if river[nx][ny]:
						dist = distance8(x, y, nx, ny)
						if dist < nearest:
							nearest = dist
			if nearest < extent / 2:
				grid[x][y] = 2
			elif nearest < extent:
				grid[x][y] = 1
	return grid

	
def find_castle_offset(size, river, riverbed):
	max_x = 0
	for y in range(size):
		for x in range(size):
			if river[x][y] or riverbed[x][y] > 0:
				max_x = max(max_x, x + 1)
	return max_x

	
def unique_keep_order(seq):
	seen = set()
	seen_add = seen.add
	return [x for x in seq if not (x in seen or seen_add(x))]


def sanitize_path(path):
	path = unique_keep_order(path)
	updated = True
	while updated:
		updated = False
		count = len(path)
		for n in range(count):
			prev = path[(count - 1 + n) % count]
			curr = path[(count     + n) % count]
			next = path[(count + 1 + n) % count]
			if (prev[0] == curr[0] == next[0]) or (prev[1] == curr[1] == next[1]):
				del path[n]
				updated = True
				break
	return path


def generate_castle_outline(size, offset):
	def clip_x(x):
		return x - x % 8
	def clip_y(y):
		return y - y % 8
	def clip(p):
		return (clip_x(p[0]), clip_y(p[1]), p[2])
	def shift(p, x, y):
		return clip((p[0] + x, p[1] + y, p[2]))
	margin = 8
	min_x = clip_x(offset + margin - 1)
	min_y = clip_y(margin)
	max_x = clip_x(size - margin)
	max_y = clip_x(size - margin)
	variation = min(16, (max_x - min_x) / 2, (max_y - min_y) / 2)
	corners = []
	corners.append(clip((random.randint(min_x, min(max_x, min_x + variation)), random.randint(min_y, min(max_y, min_y + variation)), True)))
	corners.append(clip((random.randint(max(min_x, max_x - variation), max_x), random.randint(min_y, min(max_y, min_y + variation)), True)))
	corners.append(clip((random.randint(max(min_x, max_x - variation), max_x), random.randint(max(min_y, max_y - variation), max_y), True)))
	corners.append(clip((random.randint(min_x, min(max_x, min_x + variation)), random.randint(max(min_y, max_y - variation), max_y), True)))

	effective_min_x = min(map(lambda c: c[0], corners))
	effective_min_y = min(map(lambda c: c[1], corners))
	effective_max_x = max(map(lambda c: c[0], corners))
	effective_max_y = max(map(lambda c: c[1], corners))
	delta_min_x = min_x - effective_min_x
	delta_min_y = min_y - effective_min_y
	delta_max_x = max_x - effective_max_x
	delta_max_y = max_y - effective_max_y
	corners[0] = shift(corners[0], delta_min_x, delta_min_y)
	corners[1] = shift(corners[1], delta_max_x, delta_min_y)
	corners[2] = shift(corners[2], delta_max_x, delta_max_y)
	corners[3] = shift(corners[3], delta_min_x, delta_max_y)
	
	path = []
	count = len(corners)
	for n in range(count):
		p1 = corners[n]
		p2 = corners[(n + 1) % count]
		px1 = p1[0]
		py1 = p1[1]
		px2 = p2[0]
		py2 = p2[1]
		dx = abs(px2 - px1)
		dy = abs(py2 - py1)
		path.append(p1)
		if dx > dy:
			assert px1 != px2
			pmin = min(px1, px2) / margin
			pmax = max(px1, px2) / margin
			if pmax - pmin > 1:
				mx = random.randint(pmin + 1, pmax - 1) * margin
				path.append(clip((mx, py1, False)))
				path.append(clip((mx, py2, False)))
		else:
			assert py1 != py2
			pmin = min(py1, py2) / margin
			pmax = max(py1, py2) / margin
			if pmax - pmin > 1:
				my = random.randint(pmin + 1, pmax - 1) * margin
				path.append(clip((px1, my, False)))
				path.append(clip((px2, my, False)))
	path = sanitize_path(path)
	return path

	
map_size = 32 * 3

random.seed(1)

grid_river = generate_river(map_size)
grid_riverbed = generate_riverbed(map_size, grid_river)

def template_to_matrix(data):
	matrix = create_matrix(map_size)
	lines = string.split(data, '\n')
	y = 0
	for line in lines:
		if len(line) > 0:
			for x in range(len(line)):
				c = line[x]
				matrix[x][y] = int(c)
			y = y + 1
	return matrix

data1 = """
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000111111111111111111111111111111000000
0000000000000000000000000000111111111111111111111111111111000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000111111111111111111110000000011000000
0000000000000000000000000000111111111111111111110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000111111111111000000
0000000000000000000000000000000000000000000000111111111111000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
"""

data2 = """
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000112221222212222221111111111111000000
0000000000000000000000000000112221222212222221111111111111000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000022000000
0000000000000000000000000000110000000000000000000000000022000000
0000000000000000000000000000110000000000000000000000000022000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000011000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000300000000000000000000000000022000000
0000000000000000000000000000110000000000000000000000000022000000
0000000000000000000000000000110000000000000000000000000022000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000112221222212222221110000000022000000
0000000000000000000000000000112221222212222221110000000022000000
0000000000000000000000000000000000000000000000110000000022000000
0000000000000000000000000000000000000000000000110000000022000000
0000000000000000000000000000000000000000000000110000000022000000
0000000000000000000000000000000000000000000000110000000022000000
0000000000000000000000000000000000000000000000110000000022000000
0000000000000000000000000000000000000000000000110000000022000000
0000000000000000000000000000000000000000000000112222222211000000
0000000000000000000000000000000000000000000000112222222211000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
"""

data3 = """
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000111111111111111111111111111111000000
0000000000000000000000000000111111111111111111111111111111000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000110000000000000000000000000011000000
0000000000000000000000000000111111111111111111110000000011000000
0000000000000000000000000000111111111111111111110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000110000000011000000
0000000000000000000000000000000000000000000000111111111111000000
0000000000000000000000000000000000000000000000111111111111000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
"""

data4 = """
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000111111111111111111111111111111000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000111111111111111111100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000111111111111000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
"""

data5 = """
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000110110110110110110110110110111000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000001000000
0000000000000000000000000000100000000000000000000000000000000000
0000000000000000000000000000110110110110110111100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000100000000001000000
0000000000000000000000000000000000000000000000110110110111000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
"""

matrixes = []
for n in range(4):
	matrixes.append(template_to_matrix(data1))
for n in range(7):
	matrixes.append(template_to_matrix(data2))
for n in range(1):
	matrixes.append(template_to_matrix(data3))
for n in range(2):
	matrixes.append(template_to_matrix(data4))
for n in range(1):
	matrixes.append(template_to_matrix(data5))

def draw_tower(matrix, x, y, r):
	for n in range(0, r):
		matrix[x + n][y] = Cell.WALL
		matrix[x + n][y + 1] = Cell.WALL
		matrix[x][y + n] = Cell.WALL
		matrix[x + 1][y + n] = Cell.WALL
		matrix[x + r - 2][y + n] = Cell.WALL
		matrix[x + r - 1][y + n] = Cell.WALL
		matrix[x + n][y + r - 2] = Cell.WALL
		matrix[x + n][y + r - 1] = Cell.WALL

def draw_tower_window(matrix, x, y, r):
	for n in range(0, r):
		cell = Cell.WALL
		if n >= 2 and n < r - 2:
			if r == 20:
				cell = "11110111101111"[n - 2] == "1"
			elif r == 18:
				cell = Cell.WINDOW if n <= 7 or n >= 10 else Cell.WALL
			elif r == 16:
				cell = Cell.WINDOW if n <= 5 or n >= 10 else Cell.WALL
			elif r == 14:
				cell = Cell.WINDOW if n <= 5 or n >= 8 else Cell.WALL
			else:
				cell = Cell.WINDOW
		matrix[x + n][y] = cell
		matrix[x + n][y + 1] = cell
		matrix[x][y + n] = cell
		matrix[x + 1][y + n] = cell
		matrix[x + r - 2][y + n] = cell
		matrix[x + r - 1][y + n] = cell
		matrix[x + n][y + r - 2] = cell
		matrix[x + n][y + r - 1] = cell

def draw_tower_outline(matrix, x, y, r):
	for n in range(0, r):
		matrix[x + n][y] = Cell.WALL
		matrix[x][y + n] = Cell.WALL
		matrix[x + r - 1][y + n] = Cell.WALL
		matrix[x + n][y + r - 1] = Cell.WALL

def draw_tower_merlon(matrix, x, y, r):
	x2 = x + r - 1
	y2 = y + r - 1
	matrix[x][y] = Cell.WALL
	matrix[x + 1][y] = Cell.WALL
	matrix[x][y + 1] = Cell.WALL
	matrix[x2][y] = Cell.WALL
	matrix[x2][y + 1] = Cell.WALL
	matrix[x2 - 1][y] = Cell.WALL
	matrix[x][y2] = Cell.WALL
	matrix[x + 1][y2] = Cell.WALL
	matrix[x][y + r - 2] = Cell.WALL
	matrix[x2][y2] = Cell.WALL
	matrix[x2][y2 - 1] = Cell.WALL
	matrix[x2 - 1][y2] = Cell.WALL
	for n in range(3, r / 2, 3):
		matrix[x + n][y] = Cell.WALL
		matrix[x + n + 1][y] = Cell.WALL
		matrix[x + n][y2] = Cell.WALL
		matrix[x + n + 1][y2] = Cell.WALL
		matrix[x][y + n] = Cell.WALL
		matrix[x][y + n + 1] = Cell.WALL
		matrix[x2][y + n] = Cell.WALL
		matrix[x2][y + n + 1] = Cell.WALL
	for n in range(r - 4, r / 2 - 2, -3):
		matrix[x + n][y] = Cell.WALL
		matrix[x + n - 1][y] = Cell.WALL
		matrix[x + n][y2] = Cell.WALL
		matrix[x + n - 1][y2] = Cell.WALL
		matrix[x][y + n] = Cell.WALL
		matrix[x][y + n - 1] = Cell.WALL
		matrix[x2][y + n] = Cell.WALL
		matrix[x2][y + n - 1] = Cell.WALL

def draw_cell(matrix, x1, y1, x2, y2, cell):
	for x in range(min(x1, x2), max(x1, x2) + 1):
		for y in range(min(y1, y2), max(y1, y2) + 1):
			matrix[x][y] = cell

def draw_wall(matrix, x1, y1, x2, y2):
	draw_cell(matrix, x1, y1, x2, y2, Cell.WALL)

def mod2(n):
	return n - n % 2

offset = find_castle_offset(map_size, grid_river, grid_riverbed)

margin = 2
min_x = offset
min_y = margin
max_x = map_size - margin
max_y = map_size - margin

spread = 8
min_tower_size = 20
max_tower_size = 20

min_x_a = mod2(min_x)
max_x_a = mod2(min_x + spread)
min_y_a = mod2(min_y)
max_y_a = mod2(min_y + spread)

min_x_b = mod2(max_x - max_tower_size - spread)
max_x_b = mod2(max_x - max_tower_size)
min_y_b = mod2(max_y - max_tower_size - spread)
max_y_b = mod2(max_y - max_tower_size)

x1 = mod2(random.randint(min_x_a, max_x_a))
y1 = mod2(random.randint(min_y_a, max_y_a))
x2 = mod2(random.randint(min_x_b, max_x_b))
y2 = mod2(random.randint(min_y_a, max_y_a))
x3 = mod2(random.randint(min_x_b, max_x_b))
y3 = mod2(random.randint(min_y_b, max_y_b))
x4 = mod2(random.randint(min_x_a, max_x_a))
y4 = mod2(random.randint(min_y_b, max_y_b))

s1 = mod2(random.randint(min_tower_size, max_tower_size))
s2 = mod2(random.randint(min_tower_size, max_tower_size))
s3 = mod2(random.randint(min_tower_size, max_tower_size))
s4 = mod2(random.randint(min_tower_size, max_tower_size))

matrixes = []

matrix_ground = create_matrix(map_size)

wall_thickness = 5

draw_tower(matrix_ground, x1, y1, s1)
draw_tower(matrix_ground, x2, y2, s2)
draw_tower(matrix_ground, x3, y3, s3)
draw_tower(matrix_ground, x4, y4, s4)

yw1 = mod2((min(y1 + s1, y2 + s2) + max(y1, y2)) / 2)
xw2 = mod2((min(x2 + s2, x3 + s3) + max(x2, x3)) / 2)
yw3 = mod2((min(y3 + s3, y4 + s4) + max(y3, y4)) / 2)
xw4 = mod2((min(x4 + s4, x1 + s1) + max(x4, x1)) / 2)

draw_wall(matrix_ground, x1 + s1, yw1, x2, yw1 + wall_thickness - 1)
draw_wall(matrix_ground, xw2, y2 + s2, xw2 + wall_thickness - 1, y3)
draw_wall(matrix_ground, x3, yw3, x4 + s4 - 2, yw3 + wall_thickness - 1)

ym1 = (y4 - y1) / 2 + 5
ym2 = (y4 - y1) / 2 - 5
draw_wall(matrix_ground, xw4, y4, xw4 + wall_thickness - 1, ym1)
draw_wall(matrix_ground, xw4, ym2, xw4 + wall_thickness - 1, y1 + s1 - 2)
draw_cell(matrix_ground, xw4, ym2 + 1, xw4, ym1 - 1, Cell.PORTCULLIS)

matrix_wall = copy_matrix(map_size, matrix_ground)
draw_wall(matrix_wall, xw4, y4, xw4 + wall_thickness - 1, y1 + s1 - 2)

matrix_wall_parapet = create_matrix(map_size)
draw_wall(matrix_wall_parapet, x1 + s1, yw1, x2 - 1, yw1)
draw_wall(matrix_wall_parapet, xw2 + wall_thickness - 1, y2 + s2, xw2 + wall_thickness - 1, y3 - 1)
draw_wall(matrix_wall_parapet, x3 - 1, yw3 + wall_thickness - 1, x4 + s4, yw3 + wall_thickness - 1)
draw_wall(matrix_wall_parapet, xw4, y4 - 1, xw4, y1 + s1)

matrix_wall_tower = create_matrix(map_size)
draw_tower(matrix_wall_tower, x1, y1, s1)
draw_tower(matrix_wall_tower, x2, y2, s2)
draw_tower(matrix_wall_tower, x3, y3, s3)
draw_tower(matrix_wall_tower, x4, y4, s4)

matrix_wall_tower_door = copy_matrix(map_size, matrix_wall_tower)
for n in range(wall_thickness):
	draw_cell(matrix_wall_tower_door, x1 + s1 - 2, yw1, x1 + s1 - 1, yw1 + wall_thickness, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, xw4, y1 + s1 - 2, xw4 + wall_thickness, y1 + s1 - 1, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, x2, yw1, x2 + 1, yw1 + wall_thickness, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, xw2 - 1, y2 + s2 - 2, xw2 + wall_thickness - 1, y2 + s2 - 1, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, xw2 - 1, y3, xw2 + wall_thickness - 1, y3 + 1, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, x3, yw3 - 1, x3 + 1, yw3 + wall_thickness - 1, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, x4 + s4 - 2, yw3 - 1, x4 + s4 - 1, yw3 + wall_thickness - 1, Cell.DOOR)
	draw_cell(matrix_wall_tower_door, xw4, y4, xw4 + wall_thickness, y4 + 1, Cell.DOOR)

matrix_wall_tower_window = create_matrix(map_size)
draw_tower_window(matrix_wall_tower_window, x1, y1, s1)
draw_tower_window(matrix_wall_tower_window, x2, y2, s2)
draw_tower_window(matrix_wall_tower_window, x3, y3, s3)
draw_tower_window(matrix_wall_tower_window, x4, y4, s4)

matrix_wall_tower_parapet = create_matrix(map_size)
draw_tower_outline(matrix_wall_tower_parapet, x1, y1, s1)
draw_tower_outline(matrix_wall_tower_parapet, x2, y2, s2)
draw_tower_outline(matrix_wall_tower_parapet, x3, y3, s3)
draw_tower_outline(matrix_wall_tower_parapet, x4, y4, s4)

matrix_wall_tower_merlon = create_matrix(map_size)
draw_tower_merlon(matrix_wall_tower_merlon, x1, y1, s1)
draw_tower_merlon(matrix_wall_tower_merlon, x2, y2, s2)
draw_tower_merlon(matrix_wall_tower_merlon, x3, y3, s3)
draw_tower_merlon(matrix_wall_tower_merlon, x4, y4, s4)

for n in range(11):
	matrixes.append(matrix_ground)
for n in range(1):
	matrixes.append(matrix_wall)
for n in range(2):
	matrixes.append(combine_matrix(map_size, matrix_wall_parapet, matrix_wall_tower_door))
for n in range(4):
	matrixes.append(matrix_wall_tower_door)
for n in range(2):
	matrixes.append(matrix_wall_tower)
for n in range(3):
	matrixes.append(matrix_wall_tower_window)
for n in range(2):
	matrixes.append(matrix_wall_tower)
for n in range(3):
	matrixes.append(matrix_wall_tower_window)
for n in range(1):
	matrixes.append(matrix_wall_tower)
for n in range(2):
	matrixes.append(matrix_wall_tower_parapet)
for n in range(1):
	matrixes.append(matrix_wall_tower_merlon)

export('castle.ldr', map_size, grid_river, grid_riverbed, [], matrixes)
