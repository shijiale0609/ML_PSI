# Predicting Adhesive Free Energies of Polymer-Surface Interactions with Machine Learning

This repository contains an open source implementation of the machine learning model and corresponding dataset described in our paper.


## Abstract

Polymer-surface interactions are crucial to many biological processes and industrial applications of polymers. Composition significantly influences a polymer's structural and functional properties, such as its solubility and accessible conformations. Here we propose a machine-learning method to connect a model polymer's composition with its adhesion to decorated surfaces. We simulate the adhesive free energies of 20,000 unique coarse-grained 1D sequential polymers interacting with functionalized surfaces and build support vector regression models that demonstrate inexpensive and reliable prediction of the adhesive free energy as a function of the sequence. Our work highlights the promising integration of coarse-grained simulation with data-driven machine learning methods for the design of new functional polymers and represents an important step toward linking polymer composition with polymer-surface interactions.

## Dataset

The free energy is calculated by lammps and [SSAGES](https://ssagesproject.github.io/docs/) in CG model with ABF sampling.

## Cite this work and star this repo

If this repository is helpful for your research please cite this work and star this repo.

[Predicting Adhesive Free Energies of Polymer-Surface Interactions with Machine Learning](https://pubs.acs.org/doi/10.1021/acsami.2c08891)
Jiale Shi and Michael J. Quevillon and Pedro H. Amorim Valença and Jonathan K. Whitmer
```
@article{shi2021predicting,
author = {Shi, Jiale and Quevillon, Michael J. and Amorim Valença, Pedro H. and Whitmer, Jonathan K.},
title = {Predicting Adhesive Free Energies of Polymer–Surface Interactions with Machine Learning},
journal = {ACS Applied Materials \& Interfaces},
volume = {14},
number = {32},
pages = {37161-37169},
year = {2022},
doi = {10.1021/acsami.2c08891},
URL = {https://doi.org/10.1021/acsami.2c08891},
eprint = {https://doi.org/10.1021/acsami.2c08891}
}
```
[Arxiv verion](https://arxiv.org/abs/2110.03041) is also available

## Note
code and data for academic purpose only.
