def num_mean(num_list):
    quantity = len(num_list)
    numbers_sum = sum(num_list)

    mean = round(numbers_sum / quantity, 1)

    return mean

def num_median(num_list):
    sorted_numbers = sorted(num_list, reverse = True)
    num_list_length = len(sorted_numbers)

    if num_list_length % 2 == 1:
        median = sorted_numbers[num_list_length // 2]
    else:
        median = (sorted_numbers[num_list_length // 2] + sorted_numbers[num_list_length // 2 -1]) / 2

    return median

def num_mode(num_list):
    counts = {}

    for num in num_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    most_frequent = max(counts.values())
    modes = [num for num, count in counts.items() if count == most_frequent]

    return modes

def num_variance(num_list):
    mean = num_mean(num_list)
    sum_sqr_devs = 0

    for num in num_list:
        sqr_dev = (num - mean) ** 2
        sum_sqr_devs += sqr_dev

    variance = round(sum_sqr_devs / (len(num_list)), 1)

    return variance

def num_standard_deviation(num_list):
    std_deviation = round((num_variance(num_list) ** 0.5), 1)

    return std_deviation

def basic_stats(num_list):
    print(f'Provided numbers:   {num_list}')
    print(f'Mean:   {num_mean(num_list)}')
    print(f'Median:   {num_median(num_list)}')
    print(f'Mode:   {num_mode(num_list)}')
    print(f'Variance:   {num_variance(num_list)}')
    print(f'Standard deviation:   {num_standard_deviation(num_list)}')
