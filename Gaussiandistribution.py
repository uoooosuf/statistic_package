from audioop import avg
import math
from statistics import mean
from typing_extensions import Self
from unittest import result
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Gaussian(Distribution):
    """_summary_
    Gaussia distribution class for calculating and 
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from data file
    """

    def __init__(self, mu=0, sigma=1):
        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):
        """_summary_
        Function to calculate the mean of the data set

        Args:
            None

        Returns: 
            float: mean of the data set

        """
        avg = 1.0 * sum(self.data) / len(self.data)

        self.mean = avg

        return self.mean

    def calculate_stdev(self, sample=True):
        """Function to calculate the standard deviation of the data set.

        Args:
        sample (bool): standard deviation of the dataset

        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.calculate_mean()

        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)

        self.stdev = sigma

        return self.stdev

    def plot_histogram(self):
        """_summary_
        Function to output histogram of the instance variable data
        using matplotlib pyplot library.

        Args: None

        Returns:
        None

        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('counnt')

    def pdf(self, x):
        """_summary_
        Probability density function calculator for the gaussian distribution.

        Args:
            x (float): _description_
            point for the probability density function

        Returns:
            float: probability density function output

        """

        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) /
                                                                            self.stdev) ** 2)

    def plot_histogram_pdf(Self, n_spaces=50):
        """_summary_
        Function to plot the normalized histogram of the data and a plot of the 
        probability density function along thesame range.

        Args: 
            n_spaces (int): number of data poits

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot 

        """

        mu = self.mean
        sigma = Self.stdev

        min_range = min(Self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(Self.data, density=True)
        axes[0].set_title('Normal Histogram of Data')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y

    def __add__(self, other):
        """_summary_
        Function to add together two Gaussian distributions

        Args:
            other( Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian Distribution    

        """

        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

        return result

    def__repr__(Self):

        """_summary_
        Function to output the characteristics of the gaussian instance

        Args:
            None

        Return:
            string: characteristics of the Gaussian

        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
