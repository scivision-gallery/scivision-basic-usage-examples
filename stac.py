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

# add a new class to scivision similar to PretrainedModel called something like StacDataset which can interpret the yaml in the GH repo, right now the code is just installing the package

from scivision import load_stac_dataset

data = load_stac_dataset('https://github.com/alan-turing-institute/scivision_sentinel2_stac', allow_install=True)
# data = load_stac_dataset('https://github.com/alan-turing-institute/scivision_sentinel2_stac')
# load_stac_dataset('https://github.com/alan-turing-institute/scivision_sentinel2_stac', allow_install=True)
# load_stac_dataset('https://github.com/alan-turing-institute/scivision_sentinel2_stac')

yy = data.compute()

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
