```{post} February 16, 2021
```

# Contribution to `tobler`: Speeding up areal interpolation

Have you ever needed to link two sources of data, each attached to a different geometry? In our work in the [WP2](https://urbangrammarai.github.io/spatial_signatures/index), we do. We have to transfer data from various sources, linked to output areas, urban blocks or other spatial units to our own bespoke set of geographies. Therefore, we often need to do areal interpolation to correctly map data from one layer to another. Luckily, the open-source Python ecosystem can help.

[Tobler](https://pysal.org/tobler/), a part of [PySAL family](https://pysal.org), is a library for areal interpolation and dasymetric mapping which already offered what we needed. However, our data tends to be large, up to 15 million rows on which we need to interpolate several hundreds of thousands of rows of input data. That can take a while, so each performance improvement can help a lot.

## Speeding up existing functions

We have looked into the existing code of `tobler` and contributed to the refactoring if its `area_interpolate` function. The original implementation was using custom code for spatial indexing, which was replaced by a performant vectorised implementation based on the more recent [`pygeos`](https://pygeos.readthedocs.io/en/latest/) project.

With sample data, we've been able to speed up the interpolation from 2.4 seconds to less than 400 milliseconds, having the same result 6x faster.

Such an improvement is great, but it still uses only a single core (as most of the geospatial code to be honest), leaving the rest in a modern computer (four or more cores is not uncommon these days...) lazily laying around. We have tried to change this and contributed a (still experimental) parallel implementation of the same algorithm (based on [`joblib`](https://joblib.readthedocs.io/en/latest/)).

The resulting improvements depend a lot on the input data structure, and we are still working of further tweaking, but certain combinations can provide significant speedups, which can later save us some time.

## New addition

Interpolation is not always the best way of transferring data from one layer to the other, especially for categorical variables. We have found ourselves in need of a spatial join based on the largest intersection between geometries - the category from the largest intersection gets joined to the target geometry. Such a function was not available (at least we have not found one) so we have developed it. Once it was done and battle-tested on our application, we have contributed it as a new addition to `tobler`. Everyone can now use it as `area_join`.

## Full list of contributions

The complete list of pull requests implementing code resulting from the Urban Grammar AI project is below:

- [use STRtree.query_bulk in _area_tables_binning #110](https://github.com/pysal/tobler/pull/110)
- [STRTree parallel implementation #112](https://github.com/pysal/tobler/pull/112)
- [add area_join for join based on the largest intersection #119](https://github.com/pysal/tobler/pull/119)
- [fix parallel binning #123](https://github.com/pysal/tobler/pull/123)
