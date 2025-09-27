import numpy as np

#from line_util import min_lines
from solution import Solution

output_list = []
blank_line = np.zeros(20)
n_lines = None

def print_thing(thing):
    global output_list
    global blank_line
    index_list = [i for i, x in enumerate(thing) if x == "*"]
    transformed_index_list = map(lambda x: (x-4)*2 + 8, index_list)
    blank_line_list = list(blank_line)
    transformed_thing = list(blank_line_list)
    for i in transformed_index_list:
        transformed_thing[i+1] = 1
    output_list.append(blank_line_list)
    output_list.append(transformed_thing)

def extract_points(arr):
    output_list = []
    arr_shape = arr.shape
    xdim = arr_shape[0]
    ydim = arr_shape[1]
    for i in range(1, xdim):
        for j in range(1, ydim):
            if arr[i][j] == 1.0:
                output_list.append([j,i])
    return output_list
    
def min_lines_arr(arr):
    point_list = extract_points(arr)
    print("point_list",point_list)
    solution = Solution()
    
#    n_lines = min_lines(point_list)
    n_lines = solution.minimum_lines(point_list)
    return n_lines

def on_existing_line(i, j, arr):
    global n_lines
    arr[i][j] = 1
    n_lines_after_add = min_lines_arr(arr)
    print(f"i -> {i}, j -> {j}, n_lines -> {n_lines}, n_lines_after_add -> {n_lines_after_add}", flush=True)
    ret = n_lines_after_add == n_lines
    arr[i][j] = 0
    return ret
    
def interpolate(arr):
    arr_shape = arr.shape
    xdim = arr_shape[0]
    ydim = arr_shape[1]
    for i in range(1, xdim-1):
        for j in range(1, ydim-1):
            if (arr[i][j] == 0) and \
               ((arr[i-1][j] == 1 and arr[i+1][j] == 1) or \
                (arr[i][j-1] == 1 and arr[i][j+1] == 1) or \
                (arr[i-1][j-1] == 1 and arr[i+1][j+1] == 1) or \
                (arr[i-1][j+1] == 1 and arr[i+1][j-1] == 1)):
                if on_existing_line(i, j, arr):
                    arr[i][j] = 1
                

def print_arr(arr):
    my_arr = arr.astype(str)
    #replace all elements equal to 0 with ' '
    my_arr[my_arr == "0.0"] = ' '
    #replace all elements equal to 1 with '*'
    my_arr[my_arr == "1.0"] = '*'
    for row in my_arr:
        row_list = row.tolist()
        print("".join(row_list))

def fill_row(line):
    # get the index of the first occurrence of *
    index0 = line.index("*")

    # get the index of the last occurrence of *
    line_rev = line[::-1]
    index1x = line_rev.index("*")
    l = len(line)
    index1 = l - index1x - 1

    # fill between the first occurrence and the last occurrence of *
    line_list = list(line)
    for i in range(index0+1, index1):
        line_list[i] = "*"

    return "".join(line_list)

def process(line_list):
    global output_list
    global blank_line
    global n_lines

    for line in line_list:
        print_thing(line)
    output_list.append(blank_line)

    output_arr = np.array(output_list)
    print_arr(output_arr)
    n_lines = min_lines_arr(output_arr)
    interpolate(output_arr)
    print_arr(output_arr)

line_list = [    
    "    *    ",
    "   * *   ",
    "  *   *  ",
    " *     * ",
    "***   ***",
    "  *   *  ",
    "  *   *  ",
    "  *****  "
]

process(line_list)
