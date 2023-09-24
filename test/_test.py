import pytest
import os
from main import house_statistics_polars, polars_report_generator

# Test if highest average priced houses are correctly identified
def test_house_statistics_polars():
    result = house_statistics_polars()
    assert len(result) > 0
    assert result["price"].max() == result["price"].min(), "All houses in the result should have the same highest average price"

# Test if .html report is generated
def test_polars_report_generator():
    # Use a sample dataframe for testing
    test_df = pl.DataFrame({
        "metro_distance": [1, 2, 3],
        "price": [100, 200, 300]
    })

    polars_report_generator(test_df)
    assert os.path.exists("Polars_Summary_Report.html"), ".html report file should be generated"

    
