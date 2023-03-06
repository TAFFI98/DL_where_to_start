from keras.models import Sequential, Model
from keras.layers import Dense, Input
from typing import Dict, List


"""
Keras offers different APIs to build your models: these are two examples.
For more informations on Keras functional API see: https://machinelearningmastery.com/keras-functional-api-deep-learning/
"""


def get_model_sequential(input_dim: int, layers: List[Dict]):
    """Build a model with Keras Sequential API."""

    model = Sequential()
    # First layer.
    model.add(Dense(layers[0]['size'], input_dim=input_dim, activation=layers[0]['activation']))
    # Other layers.
    for layer in layers[1:]:
        model.add(Dense(layer['size'], activation=layer['activation']))
    # Return the finished model.
    return model


def get_model_functional(input_dim: int, layers: List[Dict]):
    """Build a model with Keras Functional API."""

    # Input layer.
    input_layer = Input(shape=(input_dim,))
    output = input_layer
    # Each layer takes the previous (output) as input.
    for layer in layers:
        output = Dense(layer['size'], activation=layer['activation'])(output)
    # Return the finished model.
    return Model(inputs=input_layer, outputs=[output])