# FigureReproductionChallenge 

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

The scripts provided in this repository accompany part 2 of the scientific short cours

``A brief guide to publication-ready scientific figures using Python’s matplotlib''

held during the 2020 seminar week of the Ultrafast Laser Laboratory at
Institute of Quantum Optics at Leibniz University Hannover.

Part 2 of the short course was aimed at reproducing Fig. 3 contained in the research article

    Experimental Observation of Picosecond Pulse Narrowing and Solitons in Optical Fibers
    L. F. Mollenauer, R. H. Stolen, and J. P. Gordon
    Phys. Rev. Lett. 45, 1095 (1980)

[see here](https://doi.org/10.1103/PhysRevLett.45.1095).

## Results of the reproduction task

An exemplary result of the reproduction task is shown below

![](https://github.com/omelchert/IQOFigureReproductionChallenge/blob/master/figure_example_solution.png)

## Prerequisites

To work as intended, the provided scripts are expected to be run via Python3 in
conjunction with

* numpy
* scipy
* matplotlib

## Included materials

The repository contains:

```
IQOFigureReproductionChallenge/
├── README.md
├── LICENSE.md
├── NSE_N2.npz
├── NSE_N3.npz
├── figure_example_solution.png
├── figure_fragment.png
├── pp_figure_example_solution.py
└── pp_figure_fragment.py
```

* `LICENSE`, a license file
* `Readme.md`, this file
* `NSE_N2.npz`, raw data file using numpys custom npz format
* `NSE_N3.npz`, raw data file using numpys custom npz format
* `figure_example_solution.png`, exemplary reproduction of Fig. 3 of [this reference](https://doi.org/10.1103/PhysRevLett.45.1095)
* `figure_fragment.png`, starting point for the reproduction challenge
* `pp_figure_example_solution.py`, python module providing functions to generate `figure_example_solution.png` 
* `pp_figure_fragment.py`, python module serving as starting point for the reproduction challenge 


## Availability of the software

You can obtain a local [clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) of this repository, e.g. via

``$ git clone https://github.com/omelchert/IQOFigureReproductionChallenge``

## License

The provided scripts are licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This work received funding from the Deutsche Forschungsgemeinschaft  (DFG)
under Germany’s Excellence Strategy within the Cluster of Excellence PhoenixD
(Photonics, Optics, and Engineering – Innovation Across Disciplines) (EXC 2122,
projectID 390833453).
