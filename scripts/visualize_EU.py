from numpy import dtype, int64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.ticker as ticker
import argparse


EU_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
                   'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 
                   'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland',
                   'Portugal', 'Romania', 'Slovenia', 'Spain', 'Sweden']

Visegrad_countries = ['Czech Republic', 'Hungary', 'Poland', 'Slovakia']

EU_North = ['Sweden', 'Denmark', 'Netherlands', 'Germany']
EU_South = ['Malta', 'Italy', 'Croatia', 'Austria']
EU_East = ['Greece', 'Bulgaria', 'Romania', 'Cyprus']
EU_West = ['Portugal', 'Spain', 'France', 'Belgium']

TARGETS = ['C1_School closing', 'C2_Workplace closing', 'C3_Cancel public events', 
            'C7_Restrictions on internal movement', 'E3_Fiscal measures', 'E2_Debt/contract relief',
            'H4_Emergency investment in healthcare','H7_Vaccination policy', 'H3_Contact tracing',
            'H8_Protection of elderly people']


def preprocess_dates(x):
    x = str(x)
    year = int(x[:4])
    month = int(x[4:6])
    day = int(x[6:])
    required_date = datetime(year,month,day)
    return required_date

def create_country_dataset(data, labels):
    ds = data
    countries = labels
    df_new = pd.DataFrame()
    for cntr in countries:
        new_country = ds.loc[cntr]
        df_new = df_new.append(new_country, ignore_index=True)
    return df_new

def plot_policy(dataset, target, info, step):
    
    if info is True:
        fig, axes = plt.subplots(2, 2, figsize = (14, 12))
        sns.lineplot(ax=axes[0,0], data=dataset[0], x='Date', y=target, hue='CountryCode')
        axes[0,0].set_title('EU North')
        axes[0,0].xaxis.set_major_locator(ticker.MultipleLocator(step))
        plt.setp(axes[0,0].get_xticklabels(), rotation=45, fontsize = 4)

        sns.lineplot(ax=axes[0,1], data=dataset[1], x='Date', y=target, hue='CountryCode')
        axes[0,1].set_title('EU South')
        axes[0,1].xaxis.set_major_locator(ticker.MultipleLocator(step))
        plt.setp(axes[0,1].get_xticklabels(), rotation=45, fontsize = 4)

        sns.lineplot(ax=axes[1,0], data=dataset[3], x='Date', y=target, hue='CountryCode')
        axes[1,0].set_title('EU West')
        axes[1,0].xaxis.set_major_locator(ticker.MultipleLocator(step))
        plt.setp(axes[1,0].get_xticklabels(), rotation=45, fontsize = 7)
        
        sns.lineplot(ax=axes[1,1], data=dataset[2], x='Date', y=target, hue='CountryCode')
        axes[1,1].set_title('EU East')
        axes[1,1].xaxis.set_major_locator(ticker.MultipleLocator(step))
        plt.setp(axes[1,1].get_xticklabels(), rotation=45,  fontsize = 7)
        plt.show()        
    else:
        fig = plt.subplots(figsize=(14, 8))
        ax = sns.lineplot(data=dataset, x='Date', y=target, hue='CountryCode')
        ax.set_title(target, size=20)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(15))
        plt.setp(ax.get_xticklabels(), rotation=90)
        plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", default='whole', required=True, help="Mode to visualize: block or whole", type=str)
    parser.add_argument("-t", "--trgt", default=1 , required=False, help="Target variable to use for plot", type=int)
    parser.add_argument("-s", "--step", default=30, required=False, help='Step size to plot (1=day)', type=int)
    args = parser.parse_args()

    datasets=[]    
    #Read Dataset 
    oxford_data = pd.read_csv(r"data/OxCGRT_latest.csv", low_memory=False, index_col='CountryName')
    oxford_data['Date'] = oxford_data['Date'].apply(preprocess_dates)
    oxford_data = oxford_data.sort_values('Date', ascending=True)
    print("Dataset length: {}".format(oxford_data['Date'].max()-oxford_data['Date'].min()))

    DIRECTIONAL = [EU_North, EU_South, EU_East, EU_West]
    for direct in DIRECTIONAL:        
        new_dataset = create_country_dataset(oxford_data, direct)
        datasets.append(new_dataset)

    if args.mode == 'block':
        #Plot x4 blocks x4 countries
        plot_policy(datasets, TARGETS[args.trgt], True, args.step)
    elif args.mode == 'whole':
        #Plot for all EU Countries
        EU_dataset = create_country_dataset(oxford_data, EU_countries)
        plot_policy(EU_dataset, TARGETS[args.trgt], False, args.step)

    