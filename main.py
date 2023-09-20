import polars as pl
import matplotlib.pyplot as plt

def calculate_summary_and_plot(data_frame, column_name):
    """
    Calculate summary statistics (mean, median, and standard deviation) and create a histogram
    for a given column in a Polars DataFrame.

    Args:
        data_frame (pl.DataFrame): The Polars DataFrame containing the data.
        column_name (str): The name of the column for which statistics should be calculated
                           and the histogram should be created.

    Returns:
        dict: A dictionary containing the calculated statistics.
    """
    summary_stats = {}

    # Calculate mean
    mean = data_frame[column_name].mean().to_pandas().iloc[0]
    summary_stats['Mean'] = mean

    # Calculate median
    median = data_frame[column_name].median().to_pandas().iloc[0]
    summary_stats['Median'] = median

    # Calculate standard deviation
    std_dev = data_frame[column_name].std().to_pandas().iloc[0]
    summary_stats['Standard Deviation'] = std_dev

    # Create a histogram
    plt.hist(data_frame[column_name].to_pandas(), bins=20, edgecolor='k')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {column_name}')
    plt.show()

    return summary_stats

# Example usage:
if __name__ == "__main__":
    # Create a sample Polars DataFrame (replace this with your data)
    data = {'Age': [25, 30, 35, 40, 45]}
    df = pl.DataFrame(data)

    # Calculate summary statistics and create a histogram for the 'Age' column
    column_name = 'Age'
    stats = calculate_summary_and_plot(df, column_name)

    # Print the calculated statistics
    print(f"Summary Statistics for '{column_name}':")
    for stat, value in stats.items():
        print(f"{stat}: {value}")
