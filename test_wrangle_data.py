import pandas as pd
from wrangle_data import wrangle_disney_data


def test_dataset_shape():
    sample_dataframe = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
           'name': ['%English Oak', '%Higan Cherry', '%Willow Oak', 
                    '%Yoshino Cherry', '%Red Oak', '%Kindred Spirit Oak',
                    '%Garry Oak', '%Accolade Cherry', '%Snow Goose Cherry',
                    '%Evergreen Oak'], 
            'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
                              'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
                              'West end','Kitsilano', 'Arbutus-ridge'],
            'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
                     'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
            'date': ['Dec 21, 1937', 'Jan 11, 1945', 'Jul 12, 1991', 'Dec 31, 1957', 'Aug 15, 1947',
                         'Sep 14, 2013', 'Dec 21, 1937', 'Dec 21, 1937', 'Oct 21, 2014', 'Dec 21, 1937']}
    helper_data = pd.DataFrame.from_dict(sample_dataframe)
    character = "[%,]"
    Column1 = 'name'
    # Tests that the expected number of rows and columns are correct
    assert wrangle_disney_data(helper_data,Column1,character,col2 = 'date').shape == (10, 5)
    return

def test_dataset_cherry():
    sample_dataframe = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
           'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
                    'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
                    'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
                    'Evergreen Oak'], 
            'neighbourhood': ['\nSunset','\nWest end','\nKitsilano', '\nSunset', 
                              '\nArbutus-ridge','\nArbutus-ridge', '\nKitsilano', 
                              '\nWest end','\nKitsilano', '\nArbutus-ridge'],
            'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
                     'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
            'date': ['Dec 21, 1937', 'Jan 11, 1945', 'Jul 12, 1991', 'Dec 31, 1957', 'Aug 15, 1947',
                         'Sep 14, 2013', 'Dec 21, 1937', 'Dec 21, 1937', 'Oct 21, 2014', 'Dec 21, 1937']}
    helper_data = pd.DataFrame.from_dict(sample_dataframe)
    character = "[\n,]"
    Column1 = 'neighbourhood'
    
    sampler = wrangle_disney_data(helper_data,Column1,character,col2 = 'date')
    
    # Tests that there are only 3 rows that are of type "Oak"
    assert sampler[sampler['type'] == 'Cherry'].shape[0] == 4, "The dataframe should only have 3 rows of type 'oak'"
    
    return


