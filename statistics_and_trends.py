"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x='year', y='price', ax=ax)
    ax.set_title('BMW Car Price vs Year')
    plt.tight_layout()
    plt.show()
    plt.close()
    return
 

def plot_categorical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    top_models = df['model'].value_counts().head(10)
    sns.barplot(x=top_models.values, y=top_models.index, ax=ax)
    ax.set_title('Top 10 BMW Models by Count')
    ax.set_xlabel('Count')
    ax.set_ylabel('Model')
    plt.tight_layout()
    plt.show()
    plt.close()
    return


def plot_statistical_plot(df):
    fig, ax = plt.subplots(figsize=(8, 6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title(
    'Correlation Heatmap for Numeric BMW Attributes and '
    'Their Statistical Relationships'
)
    plt.tight_layout()
    plt.show()
    plt.close()
    return


def statistical_analysis(df, col: str):
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col].dropna())
    excess_kurtosis = ss.kurtosis(df[col].dropna())
    return mean, stddev, skew, excess_kurtosis


def preprocessing(df):
    print("Initial Data Overview:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())
    df = df.dropna(subset=['price'])
    print("\nCorrelation Matrix:")
    print(df.corr(numeric_only=True))
    return df


def writing(moments, col):
    print(f'For the attribute {col}:')
    print(f'Mean = {moments[0]:.2f}, '
          f'Standard Deviation = {moments[1]:.2f}, '
          f'Skewness = {moments[2]:.2f}, and '
          f'Excess Kurtosis = {moments[3]:.2f}.')
    skew_type = "right skewed" if moments[2] > 0 else "left skewed" if moments[2] < 0 else "not skewed"
    if moments[3] > 0:
        kurtosis_type = "leptokurtic"
    elif moments[3] < 0:
        kurtosis_type = "platykurtic"
    else:
        kurtosis_type = "mesokurtic"
    print(f"The data was {skew_type} and {kurtosis_type}.")
    return


def main():
    df = pd.read_csv('bmw.csv')
    df = preprocessing(df)
    col = 'price'  
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == '__main__':
    main()
