"""Tests for the CSV loading function."""

import logging

import pandas as pd
import pytest

from dataquantum_load_csv.load_csv import get_load_csv


def test_get_load_csv_success(tmp_path):
    """Load a valid CSV file."""
    file_csv = tmp_path / "sales.csv"
    file_csv.write_text("product,price\nBook,25\nPen,5\n", encoding="utf-8")

    df = get_load_csv(str(file_csv))

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df["product"].tolist() == ["Book", "Pen"]


def test_load_csv_custom_separator(tmp_path):
    """Load a CSV file using a semicolon delimiter."""
    file_csv = tmp_path / "sales.csv"
    file_csv.write_text("product;price\nBook;25\n", encoding="utf-8")

    df = get_load_csv(str(file_csv), sep=";")

    assert df.columns.tolist() == ["product", "price"]
    assert df.iloc[0]["price"] == 25


def test_load_csv_file_not_found(tmp_path):
    """Raise FileNotFoundError when the file does not exist."""
    file_csv = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="CSV file not found"):
        get_load_csv(str(file_csv))


def test_load_csv_empty_file(tmp_path):
    """Raise EmptyDataError when the file has no content."""
    file_csv = tmp_path / "empty.csv"
    file_csv.write_text("", encoding="utf-8")

    with pytest.raises(pd.errors.EmptyDataError):
        get_load_csv(str(file_csv))


def test_load_csv_without_rows(tmp_path, caplog):
    """Return an empty DataFrame and log a warning when there are no rows."""
    file_csv = tmp_path / "no_rows.csv"
    file_csv.write_text("product,price\n", encoding="utf-8")

    with caplog.at_level(logging.WARNING):
        df = get_load_csv(str(file_csv))

    assert df.empty
    assert "contains no rows" in caplog.text


def test_load_csv_unexpected_error(tmp_path, monkeypatch, caplog):
    """Log and propagate unexpected errors from pandas."""
    file_csv = tmp_path / "sales.csv"
    file_csv.write_text("product,price\nBook,25\n", encoding="utf-8")

    def mock_read_csv(*args, **kwargs):
        raise RuntimeError("Unexpected test error")

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    with caplog.at_level(logging.ERROR):
        with pytest.raises(RuntimeError, match="Unexpected test error"):
            get_load_csv(str(file_csv))

    assert "Unexpected error loading CSV" in caplog.text
