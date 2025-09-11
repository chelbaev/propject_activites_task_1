import argparse
from typing import Literal
from typing import Sequence
from pandas._libs import lib
from collections.abc import Hashable

import pandas as pd



def binary_feature (
        name: str,
        colum: str,
        index_col: int | str | Sequence[str | int] | Literal[False] | None = None,
        names: Sequence[Hashable] | None | lib.NoDefault = None,
        verbose: bool = False
        )->pd.DataFrame:
    """Make binary feature by average.

    Parameters
    ----------
    name: str
        Path to file or url
    colum: str
        Which colum mast be makes binary feature
    index_col: int | str | Sequence[str | int] | Literal[False] | None, optional
        index_col like pd.read_csv
    names: Sequence[Hashable] | None | lib.NoDefault, optional
        names like pd.read_csv
    verbose: bool, optional
        print result
    
    """
    df = pd.read_csv(name, index_col=index_col, names=names)
    average = df[colum].mean() 
    one_colum = df[colum]
    one_colum.name = f'filtered_{colum}'
    one_colum = (one_colum > average).astype(int)

    df = pd.concat([df, one_colum], axis=1)
    if verbose:
        print(df)
    return df 


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, help='Path to table or url')
    parser.add_argument("colum", type=str, help='name of colum')
    args = parser.parse_args()
    binary_feature(args.name, args.colum, verbose=True)