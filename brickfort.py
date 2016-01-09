import sys
import random
from math import floor, ceil, atan2, pi

SCALE = 20
SCALE_UP = 8

color_blue             = 1
color_green            = 2
color_red              = 4
color_brown            = 6
color_yellow           = 14
color_orange           = 25
color_lime             = 27
color_trans_light_blue = 43
color_light_bley       = 71
color_dark_bley        = 72


part_baseplate_32x32 = '3811'

part_plate_8x8       = '41539'
part_plate_6x6       = '3958'
part_plate_8x4       = '3035'
part_plate_4x4       = '3031'
part_plate_8x2       = '3034'
part_plate_6x2       = '3795'
part_plate_4x2       = '3020'
part_plate_2x2       = '3022'
part_plate_4x1       = '3710'
part_plate_2x1       = '3023'
part_plate_1x1       = '3024'

part_brick_4x2       = '3001'
part_brick_4x1       = '3010'
part_brick_3x1       = '3622'
part_brick_2x2       = '3003'
part_brick_2x1       = '3004'
part_brick_1x1       = '3005'

part_corner_2x2      = '2357'


part_sizes = {}

part_sizes[part_baseplate_32x32] = ( 32, 32,  0 )

part_sizes[part_plate_8x8]       = (  8,  8,  1 )
part_sizes[part_plate_6x6]       = (  6,  6,  1 )
part_sizes[part_plate_8x4]       = (  8,  4,  1 )
part_sizes[part_plate_4x4]       = (  4,  4,  1 )
part_sizes[part_plate_8x2]       = (  8,  2,  1 )
part_sizes[part_plate_6x2]       = (  6,  2,  1 )
part_sizes[part_plate_4x2]       = (  4,  2,  1 )
part_sizes[part_plate_2x2]       = (  2,  2,  1 )
part_sizes[part_plate_4x1]       = (  4,  1,  1 )
part_sizes[part_plate_2x1]       = (  2,  1,  1 )
part_sizes[part_plate_1x1]       = (  1,  1,  1 )

part_sizes[part_brick_4x2]       = (  4,  2,  3 )
part_sizes[part_brick_4x1]       = (  4,  1,  3 )
part_sizes[part_brick_3x1]       = (  3,  1,  3 )
part_sizes[part_brick_2x2]       = (  2,  2,  3 )
part_sizes[part_brick_2x1]       = (  2,  1,  3 )
part_sizes[part_brick_1x1]       = (  1,  1,  3 )

part_sizes[part_corner_2x2]      = (  2,  2,  3 )


part_offsets = {}

part_offsets[part_corner_2x2]    = ( 10, -10, 0 )


rotate_table_xy = [None for n in range(4)]
rotate_table_xy[0] = [1,0,0,0,1,0,0,0,1]
rotate_table_xy[1] = [0,0,-1,0,1,0,1,0,0]
rotate_table_xy[2] = []
rotate_table_xy[3] = []

parts_plates = [part_plate_8x8, part_plate_8x4, part_plate_4x4, part_plate_8x2, part_plate_6x2, part_plate_4x2, part_plate_2x2, part_plate_4x1, part_plate_2x1, part_plate_1x1]
parts_bricks = [part_brick_4x2, part_brick_4x1, part_brick_3x1, part_brick_2x1, part_brick_1x1]

def create_matrix(size):
	return [[False for x in range(size)] for x in range(size)] 

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
		offset = part_offsets[part]
		x = x + offset[0]
		y = y + offset[1]
		z = z + offset[2]
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

	
def export(file, size, river, riverbed, castle_outline):
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
		
	# Debug corner
	#emit_part(f, color_red, part_brick_4x1, 0, 0, 0, 0)
	#emit_part(f, color_red, part_brick_4x1, 8, 0, 0, 1)
	
	# Castle outline
	pi2 = 2 * pi
	count = len(castle_outline)
	print castle_outline
	height = 9 # must be odd
	grid_planks  = create_matrix(size)
	grid_merlons = create_matrix(size)
	plank_width = 4
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
	for h in range(height):
		emit_step(f, 'wall ' + str(n))
		h3 = h * 3
		wall    = h <= height - 4
		parapet = h >= height - 3 and h <= height - 2
		planks  = h == height - 3
		merlon  = h == height - 1
		print h,height,wall,parapet,planks,merlon
		odd = (h % 2) == 1
		offset = 2 if odd else 0
		for n in range(count):
			concave0 = concave_angles[(n + 0) % count]
			concave1 = concave_angles[(n + 1) % count]
			p1 = castle_outline[(n + 0) % count]
			p2 = castle_outline[(n + 1) % count]
			px1 = p1[0]
			py1 = p1[1]
			px2 = p2[0]
			py2 = p2[1]
			#emit_part(f, color_red, part_brick_1x1, px1, py1, 6+h3, 1)
			if px1 == px2:
				x = px1 + 1
				if py1 < py2:
					color = color_light_bley
					color = color_yellow
					reverse = False
					y1 = py1
					y2 = py2
					for py in range(y1 + 1, y2 + 1):
						for px in range(x - plank_width, x):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x - plank_width, x):
							for py in range(y1 + 1 - plank_width, y1 + 1):
								grid_planks[px][py] = True
					if parapet:
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
					color = color_red
					reverse = True
					y1 = py2 + 2 - (4 if odd else 0)
					y2 = py1 + 2 - (4 if odd else 0)
					for py in range(y1 + 3, y2 - 1):
						for px in range(x, x + plank_width):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x, x + plank_width):
							for py in range(y2 - 1, y2 - 1 + plank_width):
								#emit_part(f, color_red, part_brick_1x1, px, py, height * 3 - 3, 1)
								grid_planks[px][py] = True
					if parapet:
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
				if wall:
					for y in range(y1, y2, 4):
						color = color_light_bley if random.random() > 0.2 else color_dark_bley
						emit_part(f, color, part_brick_4x2, x - 1, y + offset, h3, 1)
			if py1 == py2:
				y = py1
				if px1 < px2:
					color = color_light_bley
					color = color_lime
					reverse = False
					x1 = px1 + (4 if odd else 0)
					x2 = px2 + (4 if odd else 0)
					for px in range(x1 + 1, x2 - 3):
						for py in range(y + 1, y + 1 + plank_width):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x1 - plank_width + 1, x1 + 1):
							for py in range(y + 1, y + 1 + plank_width):
								grid_planks[px][py] = True
					if parapet:
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
					color = color_blue
					reverse = True
					x1 = px2 + 2
					x2 = px1 + 2
					for px in range(x1 - 1, x2 - 1):
						for py in range(y + 1 - plank_width, y + 1):
							grid_planks[px][py] = True
					if not odd and concave0:
						for px in range(x2 - 1, x2 - 1 + plank_width):
							for py in range(y + 1 - plank_width, y + 1):
								grid_planks[px][py] = True
					if parapet:
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
				if wall:
					for x in range(x1, x2, 4):
						color = color_light_bley if random.random() > 0.2 else color_dark_bley
						emit_part(f, color, part_brick_4x2, x - offset, y, h3, 0)
		# Walking planks
		if planks:
			emit_step(f, 'planks ' + str(n))
			list = lay_bricks(size, grid_planks, parts_plates)
			emit_part_list(f, h3, color_brown, list)
	
	#list = lay_bricks(size, castle_outline, parts_bricks)
	#emit_part_list(f, 0, color_light_bley, list)
	
	f.write('1 71 690 -224 880 0 0 1 0 1 0 -1 0 0 dude.ldr\n')

	f.write('0\n')

	
def generate_river_path(size):
	path = []
	margin = 8
	start_x = random.randint(ceil(size * 0.1), floor(size * 0.3))
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

	
def generate_castle_floor(size, offset):
	grid = create_matrix(size)
	margin = 4
	for x in range(offset + margin, size - margin):
		for y in range(margin, size - margin):
			grid[x][y] = True
	return grid

	
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
	def clip(x, y):
		return (x - x % 8, y - y % 8)
	margin = 8
	min_x = ((offset + margin - 1) / margin) * margin
	min_y = margin
	max_x = size - margin - 1
	max_y = size - margin - 1
	variation = min(16, (max_x - min_x) / 2, (max_y - min_y) / 2)
	corners = []
	corners.append(clip(random.randint(min_x, min(max_x, min_x + variation)), random.randint(min_y, min(max_y, min_y + variation))))
	corners.append(clip(random.randint(max(min_x, max_x - variation), max_x),random.randint(min_y, min(max_y, min_y + variation))))
	corners.append(clip(random.randint(max(min_x, max_x - variation), max_x),random.randint(max(min_y, max_y - variation), max_y)))
	corners.append(clip(random.randint(min_x, min(max_x, min_x + variation)),random.randint(max(min_y, max_y - variation), max_y)))
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
			mx = random.randint(min(px1, px2), max(px1, px2))
			path.append(clip(mx, py1))
			path.append(clip(mx, py2))
		else:
			my = random.randint(min(py1, py2), max(py1, py2))
			path.append(clip(px1, my))
			path.append(clip(px2, my))
	grid = create_matrix(size)
	for n in range(len(path)):
		p1 = path[n]
		p2 = path[(n + 1) % len(path)]
		px1 = p1[0]
		py1 = p1[1]
		px2 = p2[0]
		py2 = p2[1]
		thickness = 2
		if px1 == px2:
			x = px1
			y1 = min(py1, py2)
			y2 = max(py1, py2)
			for y in range(y1, y2 + 1):
				for tx in range(thickness):
					for ty in range(thickness):
						grid[x + tx][y + ty] = True
		if py1 == py2:
			y = py1
			x1 = min(px1, px2)
			x2 = max(px1, px2)
			for x in range(x1, x2 + 1):
				for tx in range(thickness):
					for ty in range(thickness):
						grid[x + tx][y + ty] = True
	return sanitize_path(path)

	
map_size = 32 * 3

random.seed(52)
random.seed(643619)

grid_river = generate_river(map_size)
grid_riverbed = generate_riverbed(map_size, grid_river)

castle_offset = find_castle_offset(map_size, grid_river, grid_riverbed)

castle_outline = generate_castle_outline(map_size, castle_offset)
#print_matrix(map_size, castle_outline)

#castle_floor = generate_castle_floor(map_size, castle_offset)

export('castle.ldr', map_size, grid_river, grid_riverbed, castle_outline)
