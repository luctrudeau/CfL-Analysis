# Research and Findings around Chroma from Luma (CfL)

## What is this?
This is a collection of exploratory jupyter notebooks about Chroma from Luma
prediction.


## Why?
As work progressed on CfL, I started creating jupyter notebooks here and there,
and quickly lost control of all the different versions. This project aims to
collect and organize research and findings related to CfL.

This work is inspired by:

  * [Clean Code in Jupyter notebook](https://www.slideshare.net/vladimirkazantsev/clean-code-in-jupyter-notebook)
  * [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
  * [Wind Speed Analysis](https://github.com/cqcn1991/Wind-Speed-Analysis)

## Notebooks are for exploration and communication

  When we use notebooks in our work, we subdivide the notebooks in
  notebooks/exploratory which contains initial explorations, whereas
  notebooks/reports is more polished work that can be exported as html to the
  reports directory. There are two steps for using notebooks effectively:

  * Follow a naming convention that shows the owner and the order the analysis
  was done in. We use the format <step>-<ghuser>-<description>.ipynb
  (e.g., 0.3-bull-visualize-distributions.ipynb).

  * Refactor the good parts. Don't write code to do the same task in multiple
  notebooks. If it's a data preprocessing task, put it in the pipeline at
  src/data/make_dataset.py and load data from data/interim. If it's useful
  utility code, refactor it to src.

  Reference: [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
