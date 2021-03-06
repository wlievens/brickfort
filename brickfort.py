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
color_sand_green       = 378

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
	STAIRS     = 5
	HOLE       = 999

def create_matrix(size):
	return [[False for x in range(size)] for x in range(size)] 

def copy_matrix(size, matrix):
	result = create_matrix(size)
	for y in range(size):
		for x in range(size):
			result[x][y] = matrix[x][y]
	return result
	
def check_xy(x, y, map_size):
	return x >= 0 and y >= 0 and x < map_size and y < map_size

def erode_matrix(size, matrix):
	result = create_matrix(size)
	for y in range(size):
		for x in range(size):
			count = 0
			for ny in range(y - 1, y + 2):
				for nx in range(x - 1, x + 2):
					if check_xy(nx, ny, map_size) and matrix[nx][ny]:
						count = count + 1
			if count == 9:
				result[x][y] = True
	return result

def combine_matrix(size, *list):
	result = create_matrix(size)
	for y in range(size):
		for x in range(size):
			m = 0
			for matrix in list:
				v = matrix[x][y]
				if v > m:
					m = v
			result[x][y] = m
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

def stone_color():
	roll = random.random()
	if roll < 0.15:
		return color_dark_bley
	if roll < 0.20:
		return color_sand_green
	return color_light_bley

def export(file, size, river, riverbed, matrixes, soldiers):
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

	matrix_wall_list = []
	for matrix in matrixes:
		matrix_wall_list.append(create_matrix(size))
	for layer in range(len(matrixes)):
		matrix = matrixes[layer]
		emit_step(f, 'layer %s' % layer)
		prev = matrixes[layer - 1] if layer > 0 else None
		next = matrixes[layer + 1] if layer < len(matrixes) - 1 else None
		matrix_wall = matrix_wall_list[layer]
		for y in range(size):
			for x in range(size):
				cell = matrix[x][y]
				
				if cell == Cell.WALL:
					matrix_wall[x][y] = True
				
				if cell == Cell.WINDOW or cell == Cell.DOOR:
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
								emit_part(f, stone_color(), part_tile_1x2, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, 1 - rotated)
							if max_size == 4 and min_size == 2:
								emit_part(f, stone_color(), part_tile_2x2, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
							if max_size == 6 and min_size == 2:
								emit_part(f, stone_color(), part_tile_2x4, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
							if max_size == 8 and min_size == 2:
								emit_part(f, stone_color(), part_tile_1x6, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
								emit_part(f, stone_color(), part_tile_1x6, x + 1, y + 1, base * 3, rotated)
							if max_size == 10 and min_size == 2:
								emit_part(f, stone_color(), part_tile_1x8, x + (0 if orientation else 1), y + (1 if orientation else 0), base * 3, rotated)
								emit_part(f, stone_color(), part_tile_1x8, x + 1, y + 1, base * 3, rotated)
						if max_size == 10 and min_size == 2:
							emit_part(f, stone_color(), part_plate_4x2, x + (0 if orientation else 3), y + (3 if orientation else 0), top * 3 - 1, rotated + 2)
						for d in range(min_size):
							sx = x + (d if orientation else 0)
							sy = y + (0 if orientation else d)
							fx = sx + (0 if orientation else width - 1)
							fy = sy + (height - 1 if orientation else 0)
							for z in range(base, top - (1 if max_size < 8 else 2)):
								matrix_wall_list[z][sx][sy] = True
								matrix_wall_list[z][fx][fy] = True
							if max_size >= 8:
								emit_part(f, stone_color(), part_arch_1x3x2, sx, sy, (top - 2) * 3, rotated)
								emit_part(f, stone_color(), part_arch_1x3x2, fx, fy, (top - 2) * 3, rotated + 2)
								matrix_wall_list[top - 1][sx][sy] = True
								matrix_wall_list[top - 1][fx][fy] = True
							elif max_size == 8:
								emit_part(f, stone_color(), part_arch_1x8x2, sx, sy, (top - 2) * 3, rotated)
							elif max_size == 6:
								emit_part(f, stone_color(), part_arch_1x6, sx, sy, (top - 1) * 3, rotated)
							elif max_size == 4:
								emit_part(f, stone_color(), part_arch_1x4, sx, sy, (top - 1) * 3, rotated)
							elif max_size == 3:
								emit_part(f, stone_color(), part_arch_1x3, sx, sy, (top - 1) * 3, rotated)
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
				if not check_xy(x + bx, y + by, len(matrix)) or not matrix[x + bx][y + by]:
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
						emit_part(f, stone_color(), part_brick_4x2, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 4, 2, False)
		# Y-aligned 4x2
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (x % 2 == 0) and (y % 4 == offset):
					if check_matrix(matrix_wall, x, y, 2, 4):
						emit_part(f, stone_color(), part_brick_4x2, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 2, 4, False)
		# X-aligned 2x3
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 3, 2):
						emit_part(f, stone_color(), part_brick_2x3, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 3, 2, False)
		# Y-aligned 2x3
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 2, 3):
						emit_part(f, stone_color(), part_brick_2x3, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 2, 3, False)
		# X-aligned 4x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (x % 4 == offset):
					if check_matrix(matrix_wall, x, y, 4, 1):
						emit_part(f, stone_color(), part_brick_4x1, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 4, 1, False)
		# Y-aligned 4x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y] and (y % 4 == offset):
					if check_matrix(matrix_wall, x, y, 1, 4):
						emit_part(f, stone_color(), part_brick_4x1, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 1, 4, False)
		# X-aligned 3x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 3, 1):
						emit_part(f, stone_color(), part_brick_3x1, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 3, 1, False)
		# Y-aligned 3x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 1, 3):
						emit_part(f, stone_color(), part_brick_3x1, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 1, 3, False)
		# 2x2 Corner
		for y in range(size - 1):
			for x in range(size - 1):
				if matrix_wall[x][y] and matrix_wall[x + 1][y] and matrix_wall[x][y + 1] and not matrix_wall[x + 1][y + 1]:
					emit_part(f, stone_color(), part_corner_2x2, x, y, layer * 3, 0)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
				if matrix_wall[x][y] and matrix_wall[x + 1][y] and matrix_wall[x + 1][y + 1] and not matrix_wall[x][y + 1]:
					emit_part(f, stone_color(), part_corner_2x2, x, y, layer * 3, 1)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
				if matrix_wall[x][y] and matrix_wall[x][y + 1] and matrix_wall[x + 1][y + 1] and not matrix_wall[x + 1][y]:
					emit_part(f, stone_color(), part_corner_2x2, x, y, layer * 3, 3)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
				if not matrix_wall[x][y] and matrix_wall[x][y + 1] and matrix_wall[x + 1][y + 1] and matrix_wall[x + 1][y]:
					emit_part(f, stone_color(), part_corner_2x2, x, y, layer * 3, 2)
					fill_matrix(matrix_wall, x, y, 2, 2, False)
		# 2x2
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 2, 2):
						emit_part(f, stone_color(), part_brick_2x2, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 2, 2, False)
		# X-aligned 2x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 2, 1):
						emit_part(f, stone_color(), part_brick_2x1, x, y, layer * 3, 0)
						fill_matrix(matrix_wall, x, y, 2, 1, False)
		# Y-aligned 2x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					if check_matrix(matrix_wall, x, y, 1, 2):
						emit_part(f, stone_color(), part_brick_2x1, x, y, layer * 3, 1)
						fill_matrix(matrix_wall, x, y, 1, 2, False)
		# 1x1
		for y in range(size):
			for x in range(size):
				if matrix_wall[x][y]:
					emit_part(f, stone_color(), part_brick_1x1, x, y, layer * 3, 0)

	emit_step(f, 'minifigures')
	for soldier in soldiers:
		pz = soldier[2] * -SCALE_UP - 72
		py = soldier[1] * SCALE# - 180
		px = soldier[0] * SCALE# - 8
		rxy = soldier[3]
		if rxy == 0:
			px = px + 220
			py = py - 9
		if rxy == 1:
			px = px + 28
			py = py + 220
		if rxy == 2:
			px = px - 180
			py = py + 28
		if rxy == 3:
			px = px - 9
			py = py - 180
		rxy = rotate_table_xy[rxy]
		f.write('1 71 %s %s %s %s %s %s %s %s %s %s %s %s dude.ldr\n' % (px, pz, py, rxy[0], rxy[1], rxy[2], rxy[3], rxy[4], rxy[5], rxy[6], rxy[7], rxy[8]))
	
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

	
def distance4(x1, y1, x2, y2):
	return abs(x1-x2) + abs(y1-y2)

	
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

def draw_tower_wall(matrix, x, y, r):
	for n in range(0, r):
		matrix[x + n][y] = Cell.WALL
		matrix[x + n][y + 1] = Cell.WALL
		matrix[x][y + n] = Cell.WALL
		matrix[x + 1][y + n] = Cell.WALL
		matrix[x + r - 2][y + n] = Cell.WALL
		matrix[x + r - 1][y + n] = Cell.WALL
		matrix[x + n][y + r - 2] = Cell.WALL
		matrix[x + n][y + r - 1] = Cell.WALL

def draw_tower_floor(matrix, x, y, r):
	for nx in range(x, x + r):
		for ny in range(y, y + r):
			matrix[nx][ny] = Cell.WALL

def draw_tower_parapet(matrix, x, y, r):
	for n in range(0, r):
		matrix[x + n][y] = Cell.WALL
		matrix[x][y + n] = Cell.WALL
		matrix[x + r - 1][y + n] = Cell.WALL
		matrix[x + n][y + r - 1] = Cell.WALL

WINDOW_PATTERNS = ["__1111__1111__1111__",
                   "__1111_1111_1111__",
				   "___1111__1111___",
				   "__1111__1111__",
				   "___111111___",
				   "__111111__",
				   "__1111__"
				  ]

def draw_tower_window(matrix, x, y, r):
	for n in range(0, r):
		cell = Cell.WALL
		for pattern in WINDOW_PATTERNS:
			if len(pattern) == r:
				cell = Cell.WINDOW if pattern[n] == "1" else Cell.WALL
				break
		matrix[x + n][y] = cell
		matrix[x + n][y + 1] = cell
		matrix[x][y + n] = cell
		matrix[x + 1][y + n] = cell
		matrix[x + r - 2][y + n] = cell
		matrix[x + r - 1][y + n] = cell
		matrix[x + n][y + r - 2] = cell
		matrix[x + n][y + r - 1] = cell
		matrix[x + r - 1][y + n] = cell

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

def draw_wall_merlon(matrix, source):
	size = len(matrix)
	for x in range(size):
		segments = []
		start = None
		end = None
		open = False
		for y in range(size):
			if source[x][y]:
				end = y
				if not open:
					open = True
					start = y
			elif open:
				if end > start:
					segments.append((start, end))
				open = False
		if open and end > start:
			segments.append((start, end))
		if len(segments) > 0:
			for segment in segments:
				for y in range(segment[0], segment[1] + 1, 3):
					matrix[x][y] = True
					matrix[x][y + 1] = True
	for y in range(size):
		segments = []
		start = None
		end = None
		open = False
		for x in range(size):
			if source[x][y]:
				end = x
				if not open:
					open = True
					start = x
			elif open:
				if end > start:
					segments.append((start, end))
				open = False
		if open and end > start:
			segments.append((start, end))
		if len(segments) > 0:
			for segment in segments:
				for x in range(segment[0], segment[1] + 1, 3):
					matrix[x][y] = True
					matrix[x + 1][y] = True

def mod2(n):
	return n - n % 2

def convex_hull(points):
    """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

    # Sort the points lexicographically (tuples are compared lexicographically).
    # Remove duplicates to detect the case we have just one unique point.
    points = sorted(set(points))

    # Boring case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]

def lerp(t, a, b):
	return a + (b - a) * t

def prel(x, a, b):
	return 1.0 * (x - a) / (b - a)


random.seed(53167)

map_size = 32 * 4

margin                 = 4
min_tower_size         = 12
max_tower_size         = 16
thickness_wall         = 5
height_window          = 4
height_base_wall       = 12
height_portcullis      = 11
height_parapet         = 2
height_tower_floor     = 2
height_merlon          = 1
height_door            = 6
height_window_spacing  = 3
tower_window_layers    = 2
height_tower_top_floor = height_base_wall + height_door + tower_window_layers * (height_window + height_window_spacing) + height_tower_floor

grid_river = generate_river(map_size)
grid_riverbed = generate_riverbed(map_size, grid_river)

offset = find_castle_offset(map_size, grid_river, grid_riverbed)

min_x = mod2(offset + margin + max_tower_size / 2)
max_x = mod2(map_size - margin - max_tower_size / 2)
min_y = mod2(margin + max_tower_size / 2)
max_y = mod2(map_size - margin - max_tower_size / 2)

edges = []
retries = 0
max_retries = 0
min_edge_distance = 16
while len(edges) < 5:
	x = random.randint(min_x, max_x)
	y = random.randint(min_y, max_y)
	retries = retries + 1
	if retries > 100:
		edges.pop(random.randrange(len(edges)))
		retries = 0
	conflict = False
	ax1 = x
	ay1 = y
	ax2 = x
	ay2 = y
	for edge in edges:
		x2 = edge[0]
		y2 = edge[1]
		bx1 = x2
		by1 = y2
		bx2 = x2
		by2 = y2
		if not (bx1 > ax1 or bx2 < ax1 or bx1 > bx1 or bx2 < bx2):
			conflict = True
			break
		if (x != x2 and abs(x - x2) < min_edge_distance) or (y != y2 and abs(y - y2) < min_edge_distance):
			conflict = True
			break
		distance = distance4(x, y, x2, y2)
		distance = distance4(x, y, (min_x + max_x) / 2, (min_y + max_y) / 2)
		if distance < 15:
			conflict = True
			break
	if conflict:
		continue
	edges.append((x, y))
	edges = convex_hull(edges)
	retries = 0

gatehouse = edges[0]

#edges = [(40, 30), (90, 50), (70, 70), (60, 90)]

tower_centers = []
for n in range(len(edges)):
	edge1 = edges[n]
	edge2 = edges[(n + 1) % len(edges)]
	x1 = edge1[0]
	y1 = edge1[1]
	x2 = edge2[0]
	y2 = edge2[1]
	tower_centers.append(edge1)
	if x1 < x2:
		if y1 < y2:
			tower_centers.append((x2, y1))
		else:
			tower_centers.append((x1, y2))
	else:
		if y1 < y2:
			tower_centers.append((x1, y2))
		else:
			tower_centers.append((x2, y1))

gen_min_x = min(map(lambda t: t[0], tower_centers))
gen_max_x = max(map(lambda t: t[0], tower_centers))
gen_min_y = min(map(lambda t: t[1], tower_centers))
gen_max_y = max(map(lambda t: t[1], tower_centers))

def rebalance(t, s, a, b, c, d):
	t = int(round(lerp(prel(t, a, b), c, d)))
	return t - (t - s / 2) % 2

def make_tower(p):
	s = mod2(random.randint(min_tower_size, max_tower_size))
	x = rebalance(p[0], s, gen_min_x, gen_max_x, min_x, max_x)
	y = rebalance(p[1], s, gen_min_y, gen_max_y, min_y, max_y)
	return (x, y, s)

towers = map(make_tower, sanitize_path(tower_centers))

matrixes = []

matrix_wall          = create_matrix(map_size)
matrix_wall_parapet  = create_matrix(map_size)
matrix_wall_merlon   = create_matrix(map_size)
matrix_tower_wall    = create_matrix(map_size)
matrix_tower_floor   = create_matrix(map_size)
matrix_tower_door    = create_matrix(map_size)
matrix_tower_window  = create_matrix(map_size)
matrix_tower_parapet = create_matrix(map_size)
matrix_tower_merlon  = create_matrix(map_size)
matrix_portcullis    = create_matrix(map_size)

matrices_stairs = []
for n in range(height_base_wall):
	matrices_stairs.append(create_matrix(map_size))

for tower in towers:
	x = tower[0]
	y = tower[1]
	s = tower[2]
	x1 = x - s / 2
	y1 = y - s / 2
	draw_tower_wall(matrix_tower_wall, x1, y1, s)
	draw_tower_floor(matrix_tower_floor, x1, y1, s)
	draw_tower_window(matrix_tower_window, x1, y1, s)
	draw_tower_parapet(matrix_tower_parapet, x1, y1, s)
	draw_tower_merlon(matrix_tower_merlon, x1, y1, s)

min_tower_x = min(map(lambda t: t[0], towers))
leftmost_towers = filter(lambda t: t[0] == min_tower_x, towers)

portcullis_tower_index1 = towers.index(leftmost_towers[0])
portcullis_tower_index2 = (portcullis_tower_index1 + 1) % len(towers)
portcullis_x = (towers[portcullis_tower_index1][0])
portcullis_y = (towers[portcullis_tower_index1][1] + towers[portcullis_tower_index2][1]) / 2
for n in range(-4, +5):
	matrix_portcullis[portcullis_x - thickness_wall / 2][portcullis_y + n] = Cell.PORTCULLIS
	for k in range(-thickness_wall / 2 + 2, thickness_wall):
		matrix_portcullis[portcullis_x + k][portcullis_y + n] = Cell.HOLE

for n in range(len(towers)):
	tower1 = towers[n]
	tower2 = towers[(n + 1) % len(towers)]
	t1x = tower1[0]
	t1y = tower1[1]
	t1s = tower1[2]
	t2x = tower2[0]
	t2y = tower2[1]
	t2s = tower2[2]
	stairs_margin   = 4 # The minimum number of studs of wall on each side of the stairs
	stairs_width    = 2 # The width of the stairs in studs
	stairs_offset   = 2 # The number of empty studs at the ground level before the stairs
	stairs_min_size = height_base_wall + stairs_margin * 2 + stairs_offset
	t1y1 = t1y - t1s / 2
	t1y2 = t1y + t1s / 2
	t2y1 = t2y - t2s / 2
	t2y2 = t2y + t2s / 2
	t1x1 = t1x - t1s / 2
	t1x2 = t1x + t1s / 2
	t2x1 = t2x - t2s / 2
	t2x2 = t2x + t2s / 2
	if t1x < t2x and abs(t1y - t2y) < 4:
		wx1 = t1x2
		wx2 = t2x1 - 1
		wy1 = t1y - thickness_wall / 2
		wy2 = t1y + thickness_wall / 2
		draw_wall(matrix_wall, wx1, wy1, wx2, wy2)
		draw_wall(matrix_wall_parapet, wx1, wy1, wx2, wy1)
		draw_cell(matrix_tower_door, t1x2 - 2, wy1, t1x2 - 1, wy2 + 1, Cell.DOOR)
		draw_cell(matrix_tower_door, t2x1, wy1, t2x1 + 1, wy2 + 1, Cell.DOOR)
		if abs(wx1 - wx2) >= stairs_min_size:
			for n in range(height_base_wall):
				draw_cell(matrices_stairs[n], wx1 + stairs_margin, wy2, wx1 + stairs_margin + stairs_offset + n - 1, wy2 - stairs_width + 1, Cell.STAIRS)
	if t1x > t2x and abs(t1y - t2y) < 4:
		wx1 = t1x1 - 1
		wx2 = t2x2
		wy1 = t1y - thickness_wall / 2
		wy2 = t1y + thickness_wall / 2
		draw_wall(matrix_wall, wx1, wy1, wx2, wy2)
		draw_wall(matrix_wall_parapet, wx1, wy2, wx2, wy2)
		draw_cell(matrix_tower_door, t2x2 - 2, wy1 - 1, t2x2 - 1, wy2, Cell.DOOR)
		draw_cell(matrix_tower_door, t1x1, wy1 - 1, t1x1 + 1, wy2, Cell.DOOR)
		if abs(wx1 - wx2) >= stairs_min_size:
			for n in range(height_base_wall):
				draw_cell(matrices_stairs[n], wx1 - stairs_margin, wy1, wx1 - stairs_margin - stairs_offset - n + 1, wy1 + stairs_width - 1, Cell.STAIRS)
	if abs(t1x - t2x) < 4 and t1y < t2y:
		wx1 = t1x - thickness_wall / 2
		wx2 = t1x + thickness_wall / 2
		wy1 = t1y2
		wy2 = t2y1 - 1
		draw_wall(matrix_wall, wx1, wy1, wx2, wy2)
		draw_wall(matrix_wall_parapet, wx2, wy1, wx2, wy2)
		draw_cell(matrix_tower_door, wx1 - 1, t1y2 - 2, wx2, t1y2 - 1, Cell.DOOR)
		draw_cell(matrix_tower_door, wx1 - 1, t2y1, wx2, t2y1 + 1, Cell.DOOR)
		if abs(wy1 - wy2) >= stairs_min_size:
			for n in range(height_base_wall):
				draw_cell(matrices_stairs[n], wx1, wy1 + stairs_margin, wx1 + stairs_width - 1, wy1 + stairs_margin + stairs_offset + n - 1, Cell.STAIRS)
	if abs(t1x - t2x) < 4 and t1y > t2y:
		wx1 = t1x - thickness_wall / 2
		wx2 = t1x + thickness_wall / 2
		wy1 = t1y1 - 1
		wy2 = t2y2
		draw_wall(matrix_wall, wx1, wy1, wx2, wy2)
		draw_wall(matrix_wall_parapet, wx1, wy1, wx1, wy2)
		draw_cell(matrix_tower_door, wx1, t2y2 - 2, wx2 + 1, t2y2 - 1, Cell.DOOR)
		draw_cell(matrix_tower_door, wx1, t1y1, wx2 + 1, t1y1 + 1, Cell.DOOR)
		if abs(wy1 - wy2) >= stairs_min_size:
			for n in range(height_base_wall):
				draw_cell(matrices_stairs[n], wx2, wy1 - stairs_margin, wx2 - stairs_width + 1, wy1 - stairs_margin - stairs_offset - n + 1, Cell.STAIRS)

draw_wall_merlon(matrix_wall_merlon, matrix_wall_parapet)

def place_soldiers(matrix, z, count):
	map_size = len(matrix)
	matrix_wall_inner = erode_matrix(map_size, erode_matrix(map_size, matrix))
	list = []
	for y in range(map_size):
		for x in range(map_size):
			if matrix_wall_inner[x][y]:
				list.append((x, y))
	soldiers = []
	for n in range(count):
		if len(list) == 0:
			break
		point = random.choice(list)
		x = point[0]
		y = point[1]
		facing = random.randrange(0, 3)
		list = filter(lambda p: distance8(x, y, p[0], p[1]) >= 4, list)
		soldiers.append( (x, y, z * 3, facing) )
	return soldiers

soldiers = place_soldiers(matrix_wall, height_base_wall, 25) + place_soldiers(matrix_tower_floor, height_tower_top_floor, 10)

matrix_base = combine_matrix(map_size, matrix_wall, matrix_tower_wall)

for n in range(height_portcullis):
	matrixes.append(combine_matrix(map_size, matrix_base, matrices_stairs[n], matrix_portcullis))
for n in range(height_base_wall - height_portcullis):
	matrixes.append(combine_matrix(map_size, matrix_base, matrices_stairs[n], matrix_tower_floor))
for n in range(height_parapet):
	matrixes.append(combine_matrix(map_size, matrix_tower_wall, matrix_wall_parapet, matrix_tower_door))
for n in range(height_merlon):
	matrixes.append(combine_matrix(map_size, matrix_tower_wall, matrix_wall_merlon, matrix_tower_door))
for n in range(height_door - height_parapet - height_merlon):
	matrixes.append(combine_matrix(map_size, matrix_tower_wall, matrix_tower_door))

for l in range(tower_window_layers):
	for n in range(height_window_spacing):
		matrixes.append(matrix_tower_wall)
	for n in range(height_window):
		matrixes.append(matrix_tower_window)

for n in range(height_tower_floor):
	matrixes.append(combine_matrix(map_size, matrix_tower_wall, matrix_tower_floor))
for n in range(height_parapet):
	matrixes.append(matrix_tower_parapet)
for n in range(height_merlon):
	matrixes.append(matrix_tower_merlon)

export('castle.ldr', map_size, grid_river, grid_riverbed, matrixes, soldiers)
