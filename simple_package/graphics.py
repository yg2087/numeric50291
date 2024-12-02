
import matplotlib.pyplot as plt

def hist_plots(data, mean, median):
    plt.hist(data,bins=20,color = "skyblue", edgecolor="black", alpha =0.7)
    plt.axvline(mean, color = 'red', linestyle = '--', linewidth = 1.5, label = f"Mean = {mean:.2f}" )
    plt.axvline(median, color = 'blue', linestyle = '-', linewidth = 1.5, label = f"Median = {median:.2f}")
    plt.title("Histogram with Mean and Median")
    plt.xlabel("Data Values")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


