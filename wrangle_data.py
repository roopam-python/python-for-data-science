import pandas as pd


def wrangle_disney_data(wrangled_df, interest_column, char, col2="release_date"):
    """
    This is where you write your documentation
    Parameters:
    -------
    wrangled_df: dataframe to be wrangled
    col1: column to be wrangled
    char: the character to be replaced
    col2: default value 'release_date'

    Returns:
    -------
    wrangled_df: dataframe after wrangling

    Example:
    wrangle_disney_data(sample_df,col1, "$", col2 ='release_date')
    """

    if not isinstance(wrangled_df, pd.DataFrame):
        raise TypeError("data type must be a data frame")
    if interest_column not in wrangled_df.columns.tolist():
        raise AttributeError("The interest column value does not exist in Data Frame")

    wrangled_df[interest_column] = wrangled_df[interest_column].replace(
        char, "", regex=True
    )
    wrangled_df[col2] = wrangled_df[col2].apply(pd.to_datetime)
    return wrangled_df
