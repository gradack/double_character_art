import numpy as np

output_list = []
blank_line = np.zeros(20)

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

def interpolate(arr):
    arr_shape = arr.shape
    xdim = arr_shape[0]
    ydim = arr_shape[1]
    for i in range(1, xdim-1):
        for j in range(1, ydim-1):
            if (arr[i-1][j] == 1 and arr[i+1][j] == 1) or \
               (arr[i][j-1] == 1 and arr[i][j+1] == 1) or \
               (arr[i-1][j-1] == 1 and arr[i+1][j+1] == 1) or \
               (arr[i-1][j+1] == 1 and arr[i+1][j-1] == 1):
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

def process(line_list):
    global output_list
    global blank_line
    for line in line_list:
        print_thing(line)
    output_list.append(blank_line)

    output_arr = np.array(output_list)
    print_arr(output_arr)
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
