import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import polars as pl

house_data = "house.csv"

def house_statistics_polars():
    polars_house_df = pl.read_csv(house_data)

    #calculate average prices
    max_ave_prices_df = polars_house_df["price"].max()

    #select rows with the highest average prices
    polars_prices_df = polars_house_df.filter(pl.col("price")==max_ave_prices_df)

    #display houses dataset statistics
    print('Summary Statistics of the house prices:\n')
    print(polars_house_df.describe())

    #generate plot for metro distance vs price
    plt.scatter(polars_house_df["metro_distance"], polars_house_df["price"])
    plt.title("metro distance vs price")
    plt.xlabel("metro_distance")
    plt.ylabel("Average price")
    plt.show()

    #display details abount the highest prices
    print("\nDetails of the highest priced houses are: \n")
    print(polars_prices_df)

    #generate a .html summary report
    polars_report_generator(polars_house_df)
    return polars_prices_df

def polars_report_generator(polars_house_df):
    profile = ProfileReport(polars_house_df.to_pandas(), title="Summary Report")
    profile.to_file("Polars_Summary_Report.html")

house_statistics_polars()
