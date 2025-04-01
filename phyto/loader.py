from phyto.database import Session

CSV_FILE = "data/phytoplankton-results-august-2005-to-august-2012.csv"


def main(sess):
    # Write some code to load the csv into your data model
    pass


if __name__ == "__main__":
    with Session() as sess:
        main(sess)
