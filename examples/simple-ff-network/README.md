# Simple feed forward network

This is a simple Deep Learning example based on [this tutorial](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/) and some extensions suggested in the article itself.

This example is available on Colab: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/imanlab/iml_dl_tutorial/blob/master/examples/simple-ff-network/simple-ff-network-colab.ipynb)


## Prerequisites

You can run this example on your laptop without any major issues: no big CPU nor any GPU is required.  
The only requisites are some Python packages which will be listed later on.

## Environment setup

Use `conda` to create a new environment from the `env.yaml` file (see the [conda guide](../../resources/conda/guide.md) if you need a refresher)

```bash
cd /path/to/folder/example/simple-ff-network
conda env create --name simple_ff_net -f env.yaml
conda activate simple_ff_net
```

## Running the script

Now, have a look at the Python files (they are full of comments with external links to deepen your knowledge on various topics).  
When you are ready just run:

```bash
python3 main.py
```

## Considerations

This is a very simple deep learning example with a small dataset, but it introduces various useful concepts, such as:

- train/test split
- keras models
- losses, optimizers and metrics
- training and evaluation

Don't take this code as a "best practice" example, just use it to understand the most important steps to build and use a deep learning model.