"""CSV loading utilities."""

import logging
from pathlib import Path

import pandas as pd


def get_load_csv(
    file_csv: str,
    sep: str = ",",
    encoding: str = "utf-8",
) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame.

    Validate the file path, read the CSV using the specified delimiter
    and encoding, and log the loading process.

    Args:
        file_csv: Path to the CSV file.
        sep: Field delimiter used in the CSV. Defaults to ",".
        encoding: Character encoding of the file. Defaults to "utf-8".

    Returns:
        A pandas DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the file contains no data or headers.
        pd.errors.ParserError: If pandas cannot parse the CSV structure.
        UnicodeDecodeError: If the file cannot be decoded with the
            specified encoding.
        Exception: Propagates unexpected exceptions raised during
            file loading.

    Example:
        >>> df = load_csv("data/sales.csv")
        >>> df.shape
        (100, 5)
    """

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
