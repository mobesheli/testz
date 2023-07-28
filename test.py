import matplotlib.pyplot as plt

# Create a list of the months of the year.
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create a list of the number of holidays for each month.
holidays = [1, 2, 3, 4, 5, 6, 0, 0, 1, 2, 3, 4]

# Create a plot with the months on the x-axis and the number of holidays on the y-axis.
plt.plot(months, holidays)

# Label the axes and title the plot.
plt.xlabel("Month")
plt.ylabel("Number of Holidays")
plt.title("Number of Holidays per Month")

# Show the plot.
plt.show()