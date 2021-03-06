from pandas._typing import FrameOrSeries as FrameOrSeries, Scalar as Scalar, AxisType as AxisType, KeysArgType
from pandas.core.base import PandasObject as PandasObject, SelectionMixin as SelectionMixin
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.generic import NDFrame as NDFrame
from pandas.core.groupby import ops as ops
from pandas.core.indexes.api import Index as Index
from pandas.core.series import Series as Series
from typing import Any, Callable, Dict, Generator, List, Optional, Tuple, Union


class GroupByPlot(PandasObject):
    def __init__(self, groupby) -> None: ...
    def __call__(self, *args, **kwargs): ...
    def __getattr__(self, name: str) : ...

class _GroupBy(PandasObject, SelectionMixin):
    level = ...
    as_index = ...
    keys = ...
    sort = ...
    group_keys = ...
    squeeze = ...
    observed = ...
    mutated = ...
    obj = ...
    axis = ...
    grouper = ...
    exclusions = ...
    def __init__(self, obj: NDFrame, keys: Optional[KeysArgType]=..., axis: int=..., level=..., grouper: Optional[ops.BaseGrouper]=..., exclusions=..., selection=..., as_index: bool=..., sort: bool=..., group_keys: bool=..., squeeze: bool=..., observed: bool=..., mutated: bool=...) -> None: ...
    def __len__(self) -> int: ...
    @property
    def groups(self) -> Dict[str, str]: ...
    @property
    def ngroups(self): ...
    @property
    def indices(self) -> Dict[str, Index]: ...
    def __getattr__(self, attr: str) : ...
    def pipe(self, func: Callable, *args, **kwargs) : ...
    plot = ...
    def get_group(self, name, obj: Optional[DataFrame] = ...) -> DataFrame: ...
    def __iter__(self) -> Generator[Tuple[str, Any], None, None]: ...
    def apply(self, func: Callable, *args, **kwargs) -> FrameOrSeries: ...
    def transform(self, func: Callable, *args, **kwargs): ...


class GroupBy(_GroupBy):
    def any(self, skipna: bool=...) -> bool: ...
    def all(self, skipna: bool=...) -> bool: ...
    def count(self) -> FrameOrSeries: ...
    def mean(self, **kwargs) -> FrameOrSeries: ...
    def median(self, **kwargs) -> FrameOrSeries: ...
    def std(self, ddof: int = ...) -> FrameOrSeries: ...
    def var(self, ddof: int = ...) -> FrameOrSeries: ...
    def sem(self, ddof: int = ...) -> FrameOrSeries: ...
    def size(self) -> Series: ...
    def ohlc(self) -> DataFrame: ...
    def describe(self, **kwargs) -> FrameOrSeries: ...
    def resample(self, rule, *args, **kwargs): ...
    def rolling(self, *args, **kwargs): ...
    def expanding(self, *args, **kwargs): ...
    def pad(self, limit: Optional[int] = ...): ...
    def ffill(self, limit: Optional[int] = ...) -> FrameOrSeries: ...
    def backfill(self, limit: Optional[int] = ...) -> FrameOrSeries: ...
    def bfill(self, limit: Optional[int] = ...) -> FrameOrSeries: ...
    def nth(self, n: Union[int, List[int]], dropna: Optional[str] = ...) -> FrameOrSeries: ...
    def quantile(self, q=..., interpolation: str=...) : ...
    def ngroup(self, ascending: bool = ...) -> Series: ...
    def cumcount(self, ascending: bool = ...) -> Series: ...
    def rank(
        self, method: str = ..., ascending: bool = ..., na_option: str = ..., pct: bool = ..., axis: int = ...,
    ) -> DataFrame: ...
    def cummax(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries: ...
    def cummin(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries: ...
    def cumprod(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries: ...
    def cumsum(self, axis: AxisType = ..., **kwargs) -> FrameOrSeries: ...
    def shift(self, periods: int = ..., freq = ..., axis: int = ..., fill_value = ...): ...
    def pct_change(
        self, periods: int = ..., fill_method: str = ..., limit = ..., freq = ..., axis: AxisType = ...,
    ) -> FrameOrSeries: ...
    def head(self, n: int = ...) -> FrameOrSeries: ...
    def tail(self, n: int = ...) -> FrameOrSeries: ...
    # Surplus methodss from original pylance stubs; should they go away?
    def first(self, **kwargs) -> FrameOrSeries: ...
    def last(self, **kwargs) -> FrameOrSeries: ...
    def max(self, **kwargs) -> FrameOrSeries: ...
    def min(self, **kwargs) -> FrameOrSeries: ...
    def prod(self, **kwargs) -> FrameOrSeries: ...
    def sum(self, **kwargs) -> FrameOrSeries: ...


def get_groupby(obj: NDFrame, by: Optional[KeysArgType]=..., axis: int=..., level=..., grouper: Optional[ops.BaseGrouper]=..., exclusions=..., selection=..., as_index: bool=..., sort: bool=..., group_keys: bool=..., squeeze: bool=..., observed: bool=..., mutated: bool=...) -> GroupBy: ...
