import logging
import os
from datetime import date, datetime
from pathlib import Path
from typing import Optional
from urllib.request import urlopen

import fire
import pandas as pd
from ics import Calendar

logger = logging.getLogger(__file__)


def main(output: Optional[str] = None, url: Optional[str] = os.getenv("CAL_ICS_URL")):
    # get calendar
    if not url:
        logger.error("URL argument or CAL_ICS_URL env variable must be set")
        quit()

    logger.info("Reading calendar")
    cal = Calendar(urlopen(url).read().decode("iso-8859-1"))

    # get events
    events = [e.__dict__ for e in cal.events]
    logger.info(f"Fetched {len(events)} events")

    # create dataframe
    df = pd.DataFrame(events)

    # dump output
    if not output:
        now = datetime.now().strftime("%Y-%m-%d")
        output = Path(__file__).parent / f"{now}_calendar.csv".resolve()
        output = output.resolve()
    else:
        output = Path(output)
    logger.info(f"Saving to {output.resolve()}")
    df.to_csv(output, index=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
