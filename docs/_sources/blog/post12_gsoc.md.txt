```{post} June 4, 2021
```

# Google Summer of Code

Members of the Urban Grammar project are getting involved in developing the next
generation set of tools for distributing processing of geospatial vector data. In its
[first](https://urbangrammarai.xyz/data_processing/index)
[part](https://urbangrammarai.xyz/spatial_signatures/index), the Urban Grammar
project heavily depends on the processing of vector geospatial data using
[GeoPandas](https://geopandas.org) Python library. However, to scale GeoPandas
algorithms to the extent of Great Britain, we need to do more than the library can do by
default. GeoPandas operations are currently all single-threaded, severely limiting the
scalability of its usage and leaving most of the CPU cores just laying around, doing
nothing. [Dask](https://dask.org/) is a library that brings parallel and distributed
computing to the ecosystem. For example, it provides a Dask DataFrame that consists of
partitioned pandas DataFrames. Each partition can be processed by a different process
enabling the computation to be done in parallel or even out-of-core.

We are using Dask within our workflows in bespoke scripts. However, Dask could provide
ways to scale geospatial operations in GeoPandas in a similar way it does with pandas.
There has been some effort to build a bridge between Dask and GeoPandas, currently
taking the shape of the [dask-geopandas](https://github.com/geopandas/dask-geopandas)
library. While that already supports basic parallelisation, which we used in our code,
some critical components are not ready yet. That should change during this summer within
the Google Summer of Code project Martin is (co-)mentoring. We hope that this effort
will allow us to significantly simplify and even speed up the custom machinery we built
to create spatial signatures in
[WP2](https://urbangrammarai.xyz/spatial_signatures/index).