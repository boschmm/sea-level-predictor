import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision="legacy")

    # Create scatter plot
    plt.figure(1, figsize=(24,12))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='CSIRO Adjusted Sea Level', color='black')

    # Create first line of best fit
    last_year = df['Year'].max()
    df = df.append([{'Year': y} for y in range(last_year + 1, 2050)])
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    plt.plot(df['Year'], res1.intercept + res1.slope*df['Year'], color='red', label='Fitted line')


    # Create second line of best fit
    df_last = df.loc[df['Year']>=2000]
    res2 = linregress(df_last['Year'], df_last['CSIRO Adjusted Sea Level'])
    
    plt.plot(df_last['Year'], res2.intercept + res2.slope*df_last['Year'], color='b', label='Fitted line since year 2000')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc='upper left')

    xticks_labels = range(1850, 2051, 25)
    plt.xticks(ticks=xticks_labels)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
