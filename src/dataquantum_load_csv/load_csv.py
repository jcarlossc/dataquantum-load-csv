"""CSV loading utilities."""

import logging
from pathlib import Path

import pandas as pd


def get_load_csv(
    file_csv: str,
    sep: str = ",",
    encoding: str = "utf-8",
) -> pd.DataFrame:
    logger = logging.getLogger(__name__)

    try:
        logger.info("Starting CSV file loading: %s", file_csv)

        path = Path(file_csv)

        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {file_csv}")

        df = pd.read_csv(
            path,
            sep=sep,
            encoding=encoding,
        )

        if df.empty:
            logger.warning("The CSV file contains no rows: %s", file_csv)

        logger.info(
            "CSV loaded successfully. Rows: %s | Columns: %s",
            df.shape[0],
            df.shape[1],
        )

        return df

    except FileNotFoundError:
        logger.exception("CSV file not found: %s", file_csv)
        raise

    except pd.errors.EmptyDataError:
        logger.exception("CSV file contains no data or headers: %s", file_csv)
        raise

    except pd.errors.ParserError:
        logger.exception("Failed to parse CSV file: %s", file_csv)
        raise

    except UnicodeDecodeError:
        logger.exception("Failed to decode CSV file: %s", file_csv)
        raise

    except Exception:
        logger.exception("Unexpected error loading CSV: %s", file_csv)
        raise
