from app_species_pop.src import *
import warnings

warnings.filterwarnings("ignore")


if __name__ == "__main__":
    observation1 = input("Quantidade de observações no tempo 1: ")
    observation2 = input("Quantidade de observações no tempo 2: ")

    observation1 = observation1.split(",")
    observation2 = observation2.split(",")

    observation1 = list(map(int, observation1))
    observation2 = list(map(int, observation2))

    trace1 = estimate_params(observation1)
    trace2 = estimate_params(observation2)

    plot_distribution(trace1)
    plot_distribution(trace2)


