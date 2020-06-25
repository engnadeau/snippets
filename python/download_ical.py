import logging
import os
from datetime import date, datetime
from pathlib import Path
from typing import Optional
from urllib.request import urlopen

import fire
import pandas as pd
from ics import Calendar

CAL_ICS = os.getenv("CAL_ICS_URL")
NOW = datetime.now().strftime("%Y-%m-%d")
DEFAULT_OUTPUT_PATH = Path(__file__).parent / f"{NOW}_calendar.csv"
logger = logging.getLogger(__file__)


def main(output: Optional[str] = None, url: Optional[str] = None):
    # get calendar
    if not url and not CAL_ICS:
        logger.error("URL argument or CAL_ICS_URL env variable must be set")
        quit()
    elif not url:
        url = CAL_ICS

    logger.info("Reading calendar")
    cal = Calendar(urlopen(url).read().decode("iso-8859-1"))

    # get events
    events = [e.__dict__ for e in cal.events]
    logger.info(f"Fetched {len(events)} events")

    # create dataframe
    df = pd.DataFrame(events)

    # dump output
    if not output:
        output = DEFAULT_OUTPUT_PATH.resolve()
    else:
        output = Path(output)
    logger.info(f"Saving to {output.resolve()}")
    df.to_csv(output, index=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
