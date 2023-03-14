# species_population_estimation

Species Observation Analysis
This project aims to estimate the Gaussian distribution parameters of a species' observations among two different time periods. The analysis considers the amount of observations of the species in each period to estimate the mean and standard deviation of the distribution.

Getting Started
To run the analysis, you will need to install Python 3 and the following libraries:

- pandas
- numpy
- scipy
- matplotlib
- pymc3
- scipy

You can install these libraries by running the following command in your terminal:

`pip install pandas numpy scipy matplotlib pymc3 scipy`

After installing the required libraries, you can run the jupyternotebook file to perform the analysis. 

Data
The data used in this analysis consists of the number of observations of a species in two different time periods. 

period: the time period of the observation (either "period 1" or "period 2")
observations: the number of observations of the species in the corresponding time period as reported by multiple people in a fake assessment. 

Analysis
The analysis consists of the following steps:

Load the data.
Calculate the mean and standard deviation of the observations in each period.
Estimate the Gaussian distribution for each period using the calculated mean and standard deviation.
Use Markov Chain Monte Carlo, which is a statistical method used to simulate complex distributions and estimate the posterior distribution of a model's parameters for the second period estimation.
Plot the Gaussian distribution for each period using matplotlib.


Results
The results of the analysis are presented in the form of four plots per each period. The plots show the estimated Gaussian distribution of the species' observations, as well as the mean and standard deviation of the distribution, followed by an interpretation help for them.

Conclusion
By estimating the Gaussian distribution of a species' observations among two different time periods, this analysis provides valuable insights into the population dynamics of the species. 
However, gaussian distributions might not be the best distribution to use and anecdote reports on species observations are not the most reliable way to
estimatimate population distribution in a given area. However, this can be a fun exercise to start raising questions on the best way to do so, which is the intention of this notebook.
