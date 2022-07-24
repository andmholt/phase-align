import numpy as np

def align(x, y):

    # be sure to check for errors!

    # create essential vars
    x_sub = None
    y_sub = None
    if len(x) <= 2000:
        x_sub = np.array(x)
        y_sub = np.array(y)
    else:
        x_sub = np.array(x[:2000])
        y_sub = np.array(y[:2000])

    arr_len = len(x_sub)
    channels = len(x_sub[0])

    # try out each possible offset
    best_diff = None
    best_offset = None
    for curr_offset in range(arr_len-1):
        curr_diff = 0
        if (curr_offset+1)%20 == 0:
            print(str((curr_offset+1)/20) + '%')

        # iterate through array and find difference
        for i in range(arr_len):

            # set offset for iteration
            iter_offset = curr_offset
            if i+iter_offset > (arr_len-1):
                # if iter_offset greater than len of array, invert offset
                iter_offset = iter_offset * -1

            # find difference in this sample, add to total difference
            for channel in range(channels):
                sample_diff = abs(x_sub[i][channel] - y_sub[i+iter_offset][channel])
                curr_diff += sample_diff

        # if best_offset == None, use curr_offset as best_offset
        if best_offset == None:
            best_diff = curr_diff
            best_offset = curr_offset

        # if curr_diff less than best_diff, use curr_offset as best_offset
        elif curr_diff < best_diff:
            best_diff = curr_diff
            best_offset = curr_offset

    # print best found offset
    print("DONE!")
    print("file 2 offset from file 1 by", arr_len-best_offset, "samples.")

    # shift y according to the best offset
    if best_offset == 0:
        return y
    
    else:
        y = np.roll(y, best_offset, axis=0)
        return y