import os
import polars as pl
from main import house_statistics_polars, polars_report_generator  # Assuming your main script is named 'main.py'

def mock_data():
    # Create a small dataset for testing
    data = {
        "metro_distance": [5, 10, 15, 20],
        "price": [100, 150, 200, 250]
    }
    return pl.DataFrame(data)

def test_house_statistics_polars():
    # Mocking data reading with a smaller dataset
    pl.read_csv = mock_data

    # Call the function
    high_priced_df = house_statistics_polars()
    
    # Check if the function returns the expected highest priced house
    assert high_priced_df.shape[0] == 1
    assert high_priced_df["price"].to_list()[0] == 250

def test_polars_report_generator():
    # Mocking data reading with a smaller dataset
    pl.read_csv = mock_data

    # Create a report
    df = mock_data()
    polars_report_generator(df)
    
    # Check if the report file is created
    assert os.path.exists("Polars_Summary_Report.html")
    
