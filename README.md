# Solar Radiation Forecasting

## About

This repository contains the work developed by Narvaez, G, et al. in *Machine learning for site-adaptation and solar
radiation forecasting* [1]. Here is shown the solar radiation forecasting implementation with a RNN composed by LSTM
units.

## Work Environment

See [SETUP.md](SETUP.md).

## How it works?

All the project development is self content in the [*Solar_Radiation_Forecasting_LSTM.ipynb*](Solar_Radiation_Forecasting_LSTM.ipynb) notebook, feel free if you want to modify some parameters and run different train experiments.

## Demo

To use the demo run the demo.py file that has the following arguments:

- **models_path**: Path where are allocated the models folders (default: *models* folder)
- **daily_folder_name**: Folder name where are saved the .json and .h5 model files for daily forecasting (default:
  *daily_forecasting*).
- **weekly_folder_name**: Folder name where are saved the .json and .h5 model files for weekly forecasting (default:
  *weekly_forecasting*).
- **data_path**: Path where are saved the GHI_sa.csv dataset (default: *data/GHI_sa.csv*).
- **mode**: Mode to use (*daily_forecasting*, *weekly_forecasting* (default: *daily_forecasting*)).
- **day_or_week**: Day or week to forecasting. (day * 24 hours), (week * 672 hours) (default: *1416* (59*24)).

Example:

```sh
$ python demo.py --mode "daily_forecasting" --day_or_week 1416
```

## Citing Work

```BibTeX
@article{gaviria_machine_2022,
	title = {Machine learning in photovoltaic systems: A review},
	issn = {0960-1481},
	url = {https://www.sciencedirect.com/science/article/pii/S0960148122009454},
	doi = {10.1016/j.renene.2022.06.105},
	shorttitle = {Machine learning in photovoltaic systems},
	abstract = {This paper presents a review of up-to-date Machine Learning ({ML}) techniques applied to photovoltaic ({PV}) systems, with a special focus on deep learning. It examines the use of {ML} applied to control, islanding detection, management, fault detection and diagnosis, forecasting irradiance and power generation, sizing, and site adaptation in {PV} systems. The contribution of this work is three fold: first, we review more than 100 research articles, most of them from the last five years, that applied state-of-the-art {ML} techniques in {PV} systems; second, we review resources where researchers can find open data-sets, source code, and simulation environments that can be used to test {ML} algorithms; third, we provide a case study for each of one of the topics with open-source code and data to facilitate researchers interested in learning about these topics to introduce themselves to implementations of up-to-date {ML} techniques applied to {PV} systems. Also, we provide some directions, insights, and possibilities for future development.},
	journaltitle = {Renewable Energy},
	shortjournal = {Renewable Energy},
	author = {Gaviria, Jorge Felipe and Narváez, Gabriel and Guillen, Camilo and Giraldo, Luis Felipe and Bressan, Michael},
	urldate = {2022-07-03},
	date = {2022-07-01},
	langid = {english},
	keywords = {Deep learning, Machine learning, Neural networks, Photovoltaic systems, Reinforcement learning, Review},
	file = {ScienceDirect Snapshot:C\:\\Users\\jfgf1\\Zotero\\storage\\G96H46L2\\S0960148122009454.html:text/html},
},

@article{narvaez2021machine,
  title={Machine learning for site-adaptation and solar radiation forecasting},
  author={Narvaez, Gabriel and Giraldo, Luis Felipe and Bressan, Michael and Pantoja, Andres},
  journal={Renewable Energy},
  volume={167},
  pages={333--342},
  year={2021},
  publisher={Elsevier}
}
```

## References
[1] Jorge Felipe Gaviria, Gabriel Narváez, Camilo Guillen, Luis Felipe Giraldo, and Michael Bressan. Machine learning in photovoltaic systems: A review. ISSN 0960-1481. doi: 10.1016/j.renene.2022.06.105. URL https://www.sciencedirect.com/science/article/pii/S0960148122009454?via%3Dihub

[2] Narvaez, G., Giraldo, L. F., Bressan, M., & Pantoja, A. (2020). Machine learning for site-adaptation and solar 
radiation forecasting. Renewable Energy.


## Licenses

### Software
The software is licensed under an [MIT License](https://opensource.org/licenses/MIT). A copy of the license has been included in the repository and can be found [here](https://github.com/SmartSystems-UniAndes/PV_MPPT_Control_Based_on_Reinforcement_Learning/blob/main/LICENSE-MIT.txt).
