```{post} November 2, 2020
```

# Implementing morphological functions to the ecosystem

This blog post covers some of the efforts the team has made to contribute code developed for the project to the broader Python eco-system for (geographic) data science. Processing of data within [WP1](https://urbangrammarai.xyz/data_processing/index) and morphometric assessment within [WP2](https://urbangrammarai.xyz/spatial_signatures/index) entail the development of new bespoke algorithms and implementation of some which are currently available in the Python ecosystem. However, even those already existing were often not performant enough for the scale of this project.

## Speedups of existing code

As part of the data processing stage of the project, we have refactored some of them to gain the performance enhancements we needed. Since we strongly believe in replicability of research, all software developed within Urban Grammar AI project should be available for other researchers, optimally packaged in a friendly shape of a Python library. At the same time, we want to support open-source software which we use for the research.

We think the natural approach is to include enhancements made within the area of urban morphometrics to [`momepy`](http://docs.momepy.org) an existing toolkit for urban morphology. [WP2](https://urbangrammarai.xyz/spatial_signatures/index) heavily builds on `momepy`'s code and every relevant piece of code we made is now merged back into `momepy`. That covers both performance-focused changes to implementation ([#219](https://github.com/martinfleis/momepy/pull/219), [#209](https://github.com/martinfleis/momepy/pull/209), [#207](https://github.com/martinfleis/momepy/pull/207), [#205](https://github.com/martinfleis/momepy/pull/205)), mostly based on `pygeos` and vectorization, and new additions.

## New functionality

Two key features of Spatial Signatures, the concepts of [enclosures](https://urbangrammarai.xyz/spatial_signatures/spatial_unit/Parallelized_enclosures.html) and [enclosed tessellation](https://urbangrammarai.xyz/spatial_signatures/spatial_unit/enclosed_tessellation.html) are now available in `momepy.elements` module and you can create both using only a few lines of code:

```python
enclosures = momepy.enclosures(
    streets, limit=gpd.GeoSeries([convex_hull]), additional_barriers=[railway, rivers])

enclosed_tessellation = momepy.Tessellation(
    buildings, unique_id='uID', enclosures=enclosures).tessellation
```

See the detailed guidance in [momepy's documentation](http://docs.momepy.org/en/latest/user_guide/elements/enclosed.html).

Tools [we used](https://urbangrammarai.xyz/spatial_signatures/spatial_unit/Generate_enclosures.html#preprocess-railways) to preprocess street network and railway tracks before creating enclosures for a core of a new module [`momepy.preprocessing`](http://docs.momepy.org/en/latest/api.html#preprocessing), where you can find them as [`momepy.remove_false_nodes`](http://docs.momepy.org/en/latest/generated/momepy.remove_false_nodes.html#momepy.remove_false_nodes), [`momepy.close_gaps`](http://docs.momepy.org/en/latest/generated/momepy.close_gaps.html#momepy.close_gaps) and [`momepy.extend_lines`](http://docs.momepy.org/en/latest/generated/momepy.extend_lines.html#momepy.extend_lines). To measure percentiles used as a convolution layer for delineation of Spatial Signatures, you can use [`momepy.Percentiles`](http://docs.momepy.org/en/latest/generated/momepy.Percentiles.html#momepy.Percentiles) and to link enclosed tessellation to street network, there is a new function [`momepy.get_network_ratio`](http://docs.momepy.org/en/latest/generated/momepy.get_network_ratio.html#momepy.get_network_ratio).

## Full list of contributions

The complete list of pull requests implementing code resulting from Urban Grammar AI is below:

- [#219 REF: vectorize StreetProfile](https://github.com/martinfleis/momepy/pull/219)
- [#218 ENH: ratio-based network links](https://github.com/martinfleis/momepy/pull/218)
- [#217 ENH: extend_lines](https://github.com/martinfleis/momepy/pull/217)
- [#215 ENH: Close gaps](https://github.com/martinfleis/momepy/pull/215)
- [#214 REF: preprocessing module](https://github.com/martinfleis/momepy/pull/214)
- [#213 API: unified Tessellation](https://github.com/martinfleis/momepy/pull/213)
- [#212 ENH: Enclosed tessellation](https://github.com/martinfleis/momepy/pull/212)
- [#211 ENH: add enclosures function](https://github.com/martinfleis/momepy/pull/211)
- [#209 ENH: speedups, Percentiles](https://github.com/martinfleis/momepy/pull/209)
- [#207 REF: pygeos-based Tessellation](https://github.com/martinfleis/momepy/pull/207)
- [#205 ENH: faster circular compactness](https://github.com/martinfleis/momepy/pull/205)
- [#204 ENH: vectorised remove_false_nodes](https://github.com/martinfleis/momepy/pull/204)
