```{post} November 23, 2020
```

# 30DayMapChallenge 2020

On Novemeber 1<sup>st</sup> Topi Tjukanov [started](https://twitter.com/tjukanov/status/1311568912950140930) a [#30DayMapChallenge 2020](https://twitter.com/hashtag/30DayMapChallenge) - one day, one map, one theme. Because it is a lot of fun, the Geographic Data Science Lab wanted to be a part of it and on 23<sup>rd</sup> day, it was our turn.

Since the topic was _boundaries_, we decided to share with you the process of creation of boundaries of morpohlogical tessellation - the (smallest) spatial unit used in urban morphometrics.
<center>
<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/notebooks/mapchallenge/mapchallenge.gif?raw=true" alt="Tessellation animation" width=400></center>

Five cities, five different urban patterns. Morphological tessellation is in principle Voronoi tessellation based on building footprint polygons. In practice, we first shrink our polygons (you need a gap between adjacent buildings) by a small margin, then generate a dense array of points along the polygon boundary which is passed to Voronoi algorithm. Finally, resulting polygons are dissolved based on the building it belongs to, and morphological tessellation is done. See by yourself how each step looks and compares across different patterns on a matrix below. If you click on the image, you can see the [full resolution (16.2 MB)](https://github.com/urbangrammarai/urbangrammarai.github.io/blob/mapchallenge/src/notebooks/mapchallenge/matrix_lowres.png?raw=true).

<a href="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/notebooks/mapchallenge/matrix_fullres.png?raw=true">
<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/notebooks/mapchallenge/matrix_lowres.png?raw=true" alt="Matrix of cases"></a>

Do you want to play with the algorithm and create your own sequences? We have a [notebook](https://nbviewer.jupyter.org/github/urbangrammarai/urbangrammarai.github.io/blob/mapchallenge/src/notebooks/mapchallenge/tessellation.ipynb) just for you! And if you're going to generate tessellation on your data, [`momepy`](http://docs.momepy.org/en/stable/user_guide/elements/tessellation.html) has you covered. For further details head to Martin's blog post about [a paper on tessellation](https://martinfleischmann.net/morphological-tessellation/) he has published earlier this year. 

Stay tuned for new advances in this space!
