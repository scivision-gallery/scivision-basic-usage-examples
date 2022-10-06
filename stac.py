# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from scivision import load_dataset, default_catalog, load_pretrained_model
import matplotlib.pyplot as plt

data = load_dataset('https://github.com/alan-turing-institute/scivision_sentinel2_stac')

yy = data.load_data(resolution=20, bands=("red", "green", "blue"))

type(yy)

yy = yy.compute()

_ = (
    yy.isel(time=0)
    .to_array("band")
    .plot.imshow(
        col="band",
        size=4,
        vmin=0,
        vmax=4000,
    )
)

plt.show()

data_catalog = default_catalog.datasources.to_dataframe()
data_catalog

dataset_name = data_catalog.loc[data_catalog['url'] == 'https://github.com/alan-turing-institute/scivision_sentinel2_stac'].name.values[0]

compatible_models = default_catalog.compatible_models(dataset_name).to_dataframe()
compatible_models

model = load_pretrained_model('https://github.com/MartinSJRogers/VEdge_Detector_scivision', allow_install=True)
model

# Notes:
#
# - To run vedgedetector requires python 3.7 becuase of tensorflow
# - odc-stac used by the data plugin requires 3.8+
