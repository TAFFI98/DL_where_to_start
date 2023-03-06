# Simple tutorial on Graph Data Handling and Graph Neural Network for Classification

This folder contains a simple tutorial on Graph datasets handling and a Graph Neural Network classification example. It is based on [this tutorial](https://colab.research.google.com/drive/1I8a0DfQ3fI7Njc62__mVXUlcAleUclnb?usp=sharing) and [this tutorial](https://colab.research.google.com/drive/1h3-vJGRVloF5zStxL5I0rSy4ZUPNsjy8?usp=sharing) with some additions suggested in the tutorials from [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) itself.

This example is available on Colab: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/imanlab/iml_dl_tutorial/blob/master/examples/GraphNN_tutorial/GraphNN_tutorial.ipynb)


## Prerequisites

You can run this example on your laptop without any major issues: no big CPU nor any GPU is required.  
The only requisite is the creation of an environment with [PyTorch](https://pytorch.org) and [PyTorch Geometric or PyG](https://pytorch-geometric.readthedocs.io/en/latest/).

## Environment setup

Use `conda` to create a new environment from the `env.yaml` file (see the [conda guide](../../resources/conda/guide.md) if you need a refresher)

```bash
cd /path/to/folder/Graph_NN_tutorial/
conda env create --name PyG_env -f env.yaml
conda activate PyG_env
```

## Running the script

Now, have a look at the Python files.

The `main.py` file is the principal script of the tutorial. It can be divided in two parts. 
1. The first part lets the user have some understanding about the architecture of a simple dataset of graphs. The dataset taken in consideration is the [Zachary's karate club dataset](https://en.wikipedia.org/wiki/Zachary%27s_karate_club). The network captures 34 members of a karate club, documenting links between pairs of members who interacted outside the club.
2.  The second part performs a simple Graph classification task with GNNs with two different architectures. The dataset used for training and testing is the [TUDataset](https://chrsmrrs.github.io/datasets/).


The `model.py` file is the script devoted to the models architectures implementation. One model architecture makes use of the [Graph Convolutional Operator](https://arxiv.org/abs/1609.02907), while the other one makes use of the [Graph Neural Network Operator](https://arxiv.org/abs/1810.02244).


When you are ready you can just run:

```bash
python3 main.py
```
To start the tutorial.

## Considerations

This is a very simple Graph Neural Network tutorial that introduces various useful concepts, such as:

- architecture of a graph dataset and its attributes
- PyTorch geometric environment
- networkx library 
- GNNs for classification based on graph convolutional operator and graph neural network operator
