```{post} August 3rd, 2021
```

# xyzservices: a unified source of XYZ tile providers in Python

*Within the project, we often need to map the results within different contexts ranging from static to interactive maps. We felt that it could be a smoother experience and built `xyzservices`.*

A Python ecosystem offers numerous tools for the visualisation of data
on a map. A lot of them depend on XYZ tiles, providing a base map layer,
either from OpenStreetMap, satellite or other sources. The issue is that
each package that offers XYZ support manages its own list of supported
providers.

We have built `xyzservices` package to support any Python library making
use of XYZ tiles. I'll try to explain the rationale why we did that,
without going into the details of the package. If you want those
details, check its [documentation].

## The situation

Let me quickly look at a few popular packages and their approach to tile
management - `contextily`, `folium`, `ipyleaflet` and `holoviews`.

### contextily

`contextily` brings contextual base maps to static `geopandas` plots. It
comes with a dedicated `contextily.providers` module, which contains [a
hard-coded list of providers] scraped from [the list used by leaflet]
(as of version 1.1.0).

### folium

`folium` is a lightweight interface to a JavaScript leaflet library. It
providers built-in support for 6 types of tiles and allows passing any
XYZ URL and its attribution to a map. It means that it mostly relies on
external sources of tile providers.

### ipyleaflet

`ipyleaflet` brings leaflet support to Jupyter notebooks and comes with
a bit more options than `folium`. It has a very similar approach as
`contextily` does - it has [a hard-coded list] of about 37 providers in
its `basemaps` module.

### holoviews

`holoviews` provides a Python interface to the Bokeh library and its
list of supported base maps is also [hard-coded].

  [documentation]: https://xyzservices.readthedocs.io/en/latest/
  [a hard-coded list of providers]: https://github.com/geopandas/contextily/blob/v1.1.0/contextily/_providers.py
  [the list used by leaflet]: http://leaflet-extras.github.io/leaflet-providers/preview/
  [a hard-coded list]: https://github.com/jupyter-widgets/ipyleaflet/blob/0.14.0/ipyleaflet/basemaps.py
  [hard-coded]: https://github.com/holoviz/holoviews/blob/v1.14.5/holoviews/element/tiles.py

A similar situation is in other packages like `geemap` or `leafmap`.

Each package has to maintain the list of base maps, ensure that they all
work, respond to users requiring more, update links... That is a lot of
duplicated maintenance burden. We think it is avoidable.

## The vision

All XYZ tile providers have a single lightweight home and a clean API
supporting the rest of the ecosystem. All the other packages use the
same resource, one which is tested and expanded by a single group of
maintainers.

We have designed `xyzservices` to be exactly that. It is a Python
package that has no dependencies and only a single purpose - to collect
and process metadata of tile providers.

We envisage a few potential use cases.

The first - packages like `contextily` and `geopandas` will directly
support `xyzservices.TileProvider` object when specifying tiles. Nothing
else is needed, `contextily` will fetch the data it needs (final tile
URL, an attribution, zoom and extent limits) from the object. In the
code form:

    import xyzservices.providers as xyz
    from contextily import add_basemap

    add_basemap(ax, source=xyz.CartoDB.Positron)

The second option is wrapping `xyzservices.providers` into a custom API
providing, for example, an interactive selection of tiles.

The third one is using different parts of a `TileProvider` individually
when passing the information. This option can be currently used, for
example, with `folium`:

    import folium
    import xyzservices.providers as xyz

    tiles = xyz.CartoDB.Positron

    folium.Map(
        location=[53.4108, -2.9358],
        tiles=tiles.build_url(),
        attr=tiles.attribution,
    )

The last one is the most versatile. The `xyzservices` comes with a JSON
file used as a storage of all the metadata. The JSON is automatically
installed to `share/xyzservices/providers.json` where it is available
for any other package without depending on `xyzservices` directly.

We hope to cooperate with maintainers of other existing packages and
move most of the functionality around XYZ tiles that can be reused to
`xyzservices`. We think that it will:

1.  Remove the burden from individual developers. Any package will just
    implement an interface to Python or JSON API of `xyzservices`.
2.  Expand the list easy-to-use tiles for users. `xyzservices` currently
    has over 200 providers, all of which should be available for users
    across the ecosystem, without the need to individually hard-code
    them in every package.

While this [discussion started in May 2020] (thanks [@darribas]!), the
initial version of the package is out now and installable from PyPI and
conda-forge. We hope to have as many developers as possible on board to
allow for the consolidation of the ecosystem in the future.

  [discussion started in May 2020]: https://github.com/geopandas/contextily/issues/153
  [@darribas]: https://github.com/darribas