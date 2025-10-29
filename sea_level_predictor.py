import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope1 = result1.slope
    intercept1 = result1.intercept
    years1 = range(1880, 2051)               # inkl. 2050
    sea_level1 = [slope1 * year + intercept1 for year in years1]
    plt.plot(years1, sea_level1, 'r') 

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    result2 = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    slope2 = result2.slope
    intercept2 = result2.intercept
    years2 = range(2000, 2051)
    sea_level2 = [slope2 * year + intercept2 for year in years2]
    plt.plot(years2, sea_level2, 'g')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()