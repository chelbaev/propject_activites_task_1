<div align="center">
  <h1>Binary feature library</h1>
  <em>Make your binary feature</em>
  <br />
  <br />
  <p align="center">
    <a href="#"/>
      <img src="https://img.shields.io/badge/python-3.10-blue">
    </a>
  </p>
</div>

##### Development

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and sync environment:

```
uv sync --frozen --all-extras
```

- Activate project environment:

```
source .venv/bin/activate
```

#### Usage

- You can see example in examples folder

- binary_feature
```commandline
from binary_feature import binary_feature
```

```commandline
Make binary feature by average.

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
```