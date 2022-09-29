```{post} March 29, 2022
```

# Contribution to `tobler` once again: Areal interpolation even faster

Last year, we needed areal interpolation to transfer data from various administrative
and statistical spatial units like Output areas to enclosed tessellation cells. To do
that, we used the [Tobler](https://pysal.org/tobler/) Python package from [PySAL
family](https://pysal.org). And since we needed to scale it to a national level, we
spent some time refactoring the tools to make it much more performant. All that is
discussed in [this blog post](post6_tobler).

After a year, we needed areal interpolation again. This time, we took a slightly
different approach. We did not want to partition the data a priori. We also knew that
the first part of the function would work well as we had already reimplemented it
before. However, we hit another bottleneck. This time in the second part of the code, we
did not touch before. What has happened?

It is a bit technical. We need to store a relation between source and target geometries.
Say that we have 100 000 source geometries and 1 000 000 target ones. We essentially
want an array of 100 000 rows and 1 000 000. That does not fit in memory. But since a
lot of the cells of such an array would say 0, we can omit them and use a sparse array
(or sparse matrix) format, which behaves like a normal dense array but is way more
memory efficient. However, there are multiple ways of storing the data in a sparse
array. Tobler was using DOK - Dictionary of Keys. That is really fast if you need to
access individual records quickly. But that is not the application we have in tobler. We
need quick row indexing (apart from a few other things). Fortunately, the fix was
simple. We replaced DOK with CSR - Compressed Sparse Row matrix, and the results we
miraculous. While the small test benchmark was about 45x faster, our actual
interpolation was faster by several orders of magnitude. The original code did not
finish after hours. The new once was done in under a second.

Small things, like storage formats, matter. If you want to see the effect of different
sparse array formats, see [this
notebook](https://gist.github.com/martinfleis/7f68536a0fe6f3f30f1b834484d9cbab). And the
change in tobler is [here](https://github.com/pysal/tobler/pull/160) and will be part of
the next release.
