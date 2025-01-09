import matplotlib.pyplot as plt

# Numbers to experiment with

some_numbers = [34,56,87,34,34,21,64,81,13,45,45,78,72,82,22]

# Function to calculate the moving average

def calc_moving_average(list, window):
    moving_averages = []

    # For loop to begin the MA with a shortened window until window size reached

    for i in range(len(list)):
        current_window = list[max(0, i - window + 1): i + 1]
        window_average = round(sum(current_window) / len(current_window), 1)
        moving_averages.append(window_average)
    return moving_averages

def moving_average(list, window):

    # Create MA list

    moving_average_list = calc_moving_average(list, window)

    # Plot simple graph with matplotlib

    plt.plot(list, label = 'Your data')
    plt.plot(moving_average_list, label = f'{window}MA', linestyle = '--')
    plt.legend()
    plt.show()

moving_average(some_numbers, 3)
