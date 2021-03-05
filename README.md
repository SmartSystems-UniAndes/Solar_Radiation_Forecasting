# Machine learning for site-adaptation and solar radiation forecasting

## About

This repository contains the work developed by Gabriel Narvaez et al. in *Machine learning for site-adaptation and solar
radiation forecasting*. 

## Work Environment

See [SETUP.md](SETUP.md).

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
@article{narvaez2021machine,
  title={Machine learning for site-adaptation and solar radiation forecasting},
  author={Narvaez, Gabriel and Giraldo, Luis Felipe and Bressan, Michael and Pantoja, Andres},
  journal={Renewable Energy},
  volume={167},
  pages={333--342},
  year={2021},
  publisher={Elsevier}
}