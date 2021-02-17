```{post} February 17, 2021
```

# Visual style and a graphics package

Any work of the size of our Urban Grammar AI project has many outputs. All of them should ideally share the same design language, so once we combine them, they tell a coherent story. Therefore, we have defined a visual style applied to any graphical output we will produce.

We have started with a basic colourmap. A significant part of our work will result in categorical maps, so we need diverse colours. We have looked back at the excellent cartography our predecessors produced and found a gem. A study of wage and nationality in Chicago by Jane Addams and Florence Kelley from 1895 resulted in a series of beautiful maps like this one:

<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/_static/hull_house.jpg?raw=true" alt="Hull House Maps and Papers" class="bg-primary">

*Hull House Maps and Papers (1895) by Jane Addams and Florence Kelley.*

We based our primary colours on the six colours you can see on this map. This colour map offers a variety while retaining readability, colours nicely play with each other and, importantly, are colour blind safe.

<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/_static/dots.png?raw=true" alt="Primary colours" class="bg-primary">

*Primary colours derived from Adams and Kelly.*

Since we'll need more than 6 colours, we have a tiny script that generates a colour map of any size based on different lightness levels of the primary set. In the [Jupyter notebook](https://github.com/urbangrammarai/graphics/blob/main/examples/visual_style.ipynb) dedicated to the visual style, we also specified pre-sets for graphics of various plots and defined diverging colour maps based on blue and red primary colours.

<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/_static/blues.png?raw=true" alt="Blue colours" class="bg-primary">

*Shades based on blue*

<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/_static/reds.png?raw=true" alt="Red colours" class="bg-primary">

*Shades based on red*

<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/_static/diverging.png?raw=true" alt="Diverging colours" class="bg-primary">

*Diverging colour map based on blue and red*

We have also specified the styling of maps, including custom Mapbox tiles to provide additional context to our geometries. As a bonus, we have a tiny function adding a north arrow to the map, so we can generate publication-ready maps straight from Python.

<img src="https://github.com/urbangrammarai/urbangrammarai.github.io/blob/master/src/_static/bcn.png?raw=true" alt="Signatures in Barcelona" class="bg-primary">

*Spatial Signatures in Barcelona*

All of that is wrapped in a [lightweight Python library](https://github.com/urbangrammarai/graphics) called `urbangrammar-graphics`, which includes colour maps, tiles and an arrow. If you want to use the same in your project, feel free to do so! It is as simple as `pip install urbangrammar-graphics`.
