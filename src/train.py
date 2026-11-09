import argparse

from model import ProteinExpertModel
from utils import load_assays


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    assays = load_assays(args.config)
    model = ProteinExpertModel()
    print("adapting on", len(assays), "assay families")


if __name__ == "__main__":
    main()
