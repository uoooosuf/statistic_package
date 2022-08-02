class Distribution:

    def __init__(self, mu=0, sigma=1):
        """"Generic distribution class for calculating and 
        visualizing a probability distribution.

        Attributes:
            mean (float) representing mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of float) a list of float extracted from the file

            """

        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """ Function to read data from a txt file. The txt file should have 
            one number (float) per line. The numbers are stored in a data Attribute.

        Args: 
            file_name (string): name of a file to read from

        returns:
            None

        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
