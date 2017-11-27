def product(values, weights):
    return sum(v * w for v, w in zip(values, weights))
t = 0.4
l = 0.1
wts = [0, 0, 0]
training_set = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]
while True:
    print
    error_count = 0
    for input_vector, desired_output in training_set:
        print(wts)
        result = product(input_vector, wts) > t
        error = desired_output - result
        if error != 0:
            error_count += 1
        for index, value in enumerate(input_vector):
            wts[index] += l * error * value
    if error_count == 0:
        break
