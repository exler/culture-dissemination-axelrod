from culdisaxel.model import AxelrodModel

if __name__ == "__main__":
    AxelrodModel(n=10, cycles=100000, print_at_cycles=[0, 20000, 40000, 80000]).simulate()
