from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD


def get_model():
    """Create the model."""

    INPUT_SHAPE = (28, 28, 1)
    NUM_CLASSES = 10

    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=INPUT_SHAPE))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    """
    A softmax activation is typical of the output layer for a classifier network.

    Softmax ensures that the N outputs of the layer sum to a total of 1.
    With regard to classification each weight can then be interpreted as a "confidence"
    that the sample can be classified as the label corresponding to that output.
    You can read more about softmax here: https://towardsdatascience.com/softmax-activation-function-how-it-actually-works-d292d335bd78
    """
    model.add(Dense(NUM_CLASSES, activation='softmax'))

    """
    The learning rate and the momentum of the SGD optimizer are hyperparameters of the model:
    you can try running multiple training cycles with different values and see how they affect the results.
    """
    opt = SGD(learning_rate=0.01, momentum=0.9)
    """
    The categorical crossentropy loss function is used in classification problems.
    You can read more about it here: https://machinelearningmastery.com/cross-entropy-for-machine-learning/

    Accuracy is a metric defined as (# of correct predictions / # of total predictions).
    You can read more about it here: https://machinelearningmastery.com/custom-metrics-deep-learning-keras-python/
    """
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

    return model
