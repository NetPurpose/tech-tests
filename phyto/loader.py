from datetime import datetime, date

from typing import Dict, Any
from phyto.database import Session, Sample, LocalAuthority
import csv

CSV_FILE = "data/phytoplankton-results-august-2005-to-august-2012.csv"


def read_csv():
    with open(CSV_FILE) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def get_or_create_local_authority(sess: Session, la: str) -> LocalAuthority:
    authority = sess.query(LocalAuthority).filter_by(name=la).one_or_none()
    if authority is None:
        authority = LocalAuthority(name=la)
        sess.add(authority)
    return authority


def cooerce_to_none(row: Dict[str, Any], key: str, default=None):
    val = row[key]
    if val == "":
        return default
    return val


def coeerce_value(row, key):
    val = row[key]
    try:
        return float(val)
    except ValueError:
        return None


def date_parse(date_str: str) -> date:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None


def add_sample(
    sess: Session, row: Dict[str, Any], local_authority: LocalAuthority
) -> None:
    keys = [
        "Alex",
        "Gym",
        "Dino",
        "Pro",
        "Pseudo",
        "Karen",
        "Yesso",
        "Proto",
        "Vener",
        "Crass",
    ]
    date_collected = date_parse(row["DateSampleCollected"])
    date_arrived = date_parse(row["DateSampleArrivedatLowestoft"])
    date_analysed = date_parse(row["DateOfAnalysis"])
    if any(x is None for x in [date_collected, date_arrived, date_analysed]):
        return
    values = dict((k.lower(), coeerce_value(row, k)) for k in keys)
    sample = Sample(
        sample_number=row["SampleNumber"],
        bed_id=cooerce_to_none(row, "BedId"),
        local_authority=local_authority,
        collection_method=cooerce_to_none(
            row, "SampleCollectionMethod", default="unknown"
        ).lower(),
        date_collected=date_collected,
        date_analysed=date_analysed,
        date_arrived=date_arrived,
        **values
    )
    sess.add(sample)


def main(sess: Session):
    for row in read_csv():
        local_authority = get_or_create_local_authority(sess, row["LocalAuthority"])
        add_sample(sess, row, local_authority)


if __name__ == "__main__":
    session = Session()
    main(session)
    session.commit()
