# MNIST digits CNN example

This is a simple Deep Learning example loosely based on [this tutorial](https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/).  
It will introduce you to CNNs and the basics of image data pipelines.

The objective of this model is to take in a simple black and white image of an handwritten digit and predict the digit it represents. The dataset we are using is quite famous in the AI world and is called [MNIST](http://yann.lecun.com/exdb/mnist/).

This example is available on Colab: [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/imanlab/iml_dl_tutorial/blob/master/examples/mnist-digits-cnn/mnist-digits-cnn-colab.ipynb)

## Prerequisites

You can run this example on your laptop without any major issues, except that the model will be quite slow to train. Depending on the performance of you machine it might take from 15 minutes to more than one our. A GPU would speed this process up by a lot, but setting up A GPU environment is outside of the scope of this guide and the training is still doable with CPU only.  
If you want to experiment with the difference in performance between CPU and GPU use the Google Colab version of this example.

## Data

The data is already stored in the data folder in an archive file, which must be extracted.

```bash
cd /path/to/folder/example/mnist-digits-cnn/data
tar -xf mnist-data-png.tar.xz
```

This should create two folders: "training" and "testing" containing all the images.

## Environment setup

Use `conda` to create a new environment from the `env.yaml` file (see the [conda guide](../../resources/conda/guide.md) if you need a refresher)

```bash
cd /path/to/folder/example/mnist-digits-cnn
conda env create --name mnist_digits_cnn -f env.yaml
conda activate mnist_digits_cnn
```

## Running the script

Now, have a look at the Python files (they are full of comments with external links to deepen your knowledge on various topics).  
When you are ready just run the training file:

```bash
python3 train.py
```

Once the model is trained and saved you can load and evaluate it by running:

```bash
python3 eval.py
```

These two scripts are separate so that you can run the training only once and then run the evaluation whenever you want without having to run the training again.

## Considerations

This is a very simple CNN example, but it introduces various useful concepts, such as:

- simple image pipeline and normalization
- CNN models
- classification problems, one-hot encoding, categorical crossentropy
- confusion matrix

Don't take this code as a "best practice" example, just use it to understand the most important steps to build and use a deep learning model.
