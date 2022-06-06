```{post} April 25, 2022
```

# CEUS paper

This week saw the first peer-reviewed publication related to the Urban Grammar
see the light of day. Full coordinates of the paper are available here:

> Singleton, A.; Arribas-Bel, D.; Murray, J.; Fleischmann, M. (2022). "Estimating generalized measures of local neighbourhood context from multispectral satellite images using a convolutional neural network". *Computers, Environment and Urban Systems*, 95. `10.1016/j.compenvurbsys.2022.101802`

* [Published Version](https://www.sciencedirect.com/science/article/pii/S0198971522000461) (Open Access)
* [Code repository@`GitHub`](https://github.com/GDSL-UL/sat_cnn)
* [Data repository@`Dataverse`](https://dataverse.harvard.edu/dataverse/sat_cnn)
* [Interactive map@`Unfolded`](https://studio.unfolded.ai/public/c40f0a5b-a1f8-48af-8b7d-7c258942cf0d)
* `bibtex` citation:

```bibtex
@article{SINGLETON2022101802,
title = {Estimating generalized measures of local neighbourhood context from multispectral satellite images using a convolutional neural network},
journal = {Computers, Environment and Urban Systems},
volume = {95},
pages = {101802},
year = {2022},
issn = {0198-9715},
doi = {https://doi.org/10.1016/j.compenvurbsys.2022.101802},
url = {https://www.sciencedirect.com/science/article/pii/S0198971522000461},
author = {Alex Singleton and Dani Arribas-Bel and John Murray and Martin Fleischmann},
keywords = {Deep learning, Convolutional neural networks, Urban morphology, Multispectral satellite imagery, Cluster analysis},
abstract = {The increased availability of high-resolution multispectral imagery captured by remote sensing platforms provides new opportunities for the characterisation and differentiation of urban context. The discovery of generalized latent representations from such data are however under researched within the social sciences. As such, this paper exploits advances in machine learning to implement a new method of capturing measures of urban context from multispectral satellite imagery at a very small area level through the application of a convolutional autoencoder (CAE). The utility of outputs from the CAE is enhanced through the application of spatial weighting, and the smoothed outputs are then summarised using cluster analysis to generate a typology comprising seven groups describing salient patterns of differentiated urban context. The limits of the technique are discussed with reference to the resolution of the satellite data utilised within the study and the interaction between the geography of the input data and the learned structure. The method is implemented within the context of Great Britain, however, is applicable to any location where similar high resolution multispectral imagery are available.}
}
```

This is technically not an Urban Grammar paper 100%, as
it was a collab initiated and led by [Alex Singleton](https://www.alex-singleton.com/) and
[John Murray](https://uk.linkedin.com/in/murraydata), both from the
[Geographic Data Science Lab](https://www.liverpool.ac.uk/geographic-data-science/).
But it was a project we got involved in because of the Urban Grammar and its
output is very much in line with the spirit of our project.
A propos of the publication, Alex did a Twitter thread that summarises better
than anything I could do the gist of the paper, why it's important, and some
of our thinking into how this feeds into broader efforts to measure and
understand neighborhood context.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">New paper w/ <a href="https://twitter.com/MurrayData?ref_src=twsrc%5Etfw">@murraydata</a>, <a href="https://twitter.com/martinfleis?ref_src=twsrc%5Etfw">@martinfleis</a> and <a href="https://twitter.com/darribas?ref_src=twsrc%5Etfw">@darribas</a> that uses open-source satellite imagery to create measures of local neighbourhood context. Open Access published version here: <a href="https://t.co/dyunv1KMUc">https://t.co/dyunv1KMUc</a> - all data and code: <a href="https://t.co/4Qi1ps3UrI">https://t.co/4Qi1ps3UrI</a> 1/11 <a href="https://t.co/45W4LELsgP">pic.twitter.com/45W4LELsgP</a></p>&mdash; Alex Singleton (@alexsingleton) <a href="https://twitter.com/alexsingleton/status/1518537575778168833?ref_src=twsrc%5Etfw">April 25, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

We are hugely excited about our results and the posibilities that using
satellite technology, combined with a bit of machine learning and computer
vision, opens up for building an understanding of cities at neighborhood
level. The paper is open access, and the open data product we built around is,
well... open; so, if you're interested in this space (pun intended!) there is
plenty for you to play with. If any of it stirs your interest further, do get
in touch, we'd love to talk!

