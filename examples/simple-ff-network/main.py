# IMPORTS

from sklearn.model_selection import train_test_split

from data import load_data
from model import get_model_functional, get_model_sequential
from output import plot_history

# HYPERPARAMETERS
# These values are tunable parameters, often are loaded from an external configuration file.

# A seed can be provided to all random processes to ensure reproducibility.
# For more information see: https://machinelearningmastery.com/randomness-in-machine-learning/
random_state = 42
test_fraction = 0.2
batch_size = 32
input_size = 8
layers = [
    {'size': 12, 'activation': 'relu'},
    {'size': 8, 'activation': 'relu'},
    {'size': 1, 'activation': 'sigmoid'},
]
epochs = 150


# DATA

# Load the dataset.
X, y = load_data(csv_path='data/pima-indians-diabetes.csv')
# Split train and test (or validation) dataset.
# For more information see: https://machinelearningmastery.com/train-test-split-for-evaluating-machine-learning-algorithms/
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_fraction, shuffle=True, random_state=random_state)

# MODEL DEFINITION

model_seq = get_model_sequential(input_size, layers)
model_func = get_model_functional(input_size, layers)

# Model representation.
# For more information see: https://machinelearningmastery.com/visualize-deep-learning-neural-network-model-keras/
print(model_func.summary())
input("This is the functional model: press any key to continue...")
print(model_seq.summary())
input("This is the sequential model: press any key to continue...")

# In practice the two model are the same, so we choose one.
model = model_seq

# For more information on losses, optimizers, metrics, callbacks search the Keras documentation and read:
# https://machinelearningmastery.com/5-step-life-cycle-neural-network-models-keras/
#
# https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/
# https://machinelearningmastery.com/tour-of-optimization-algorithms/ 
# https://machinelearningmastery.com/custom-metrics-deep-learning-keras-python/
# https://machinelearningmastery.com/how-to-stop-training-deep-neural-networks-at-the-right-time-using-early-stopping/
#
# You can also define your own functions as losses, metrics or callbacks.

# Our case is a classification problem, so we'll use binary crossentropy loss and accuracy metric.
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# TRAINING

# Fit the keras model on the dataset.
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)
plot_history(history, metrics=['loss', 'accuracy'], restore_weights=False, save_folder='plots')

# SAVING
# The trained model can be saved to be retrieved later, without re-training it.
# e.g. model = keras.models.load_model('path/to/model')
# For more information: https://machinelearningmastery.com/save-load-keras-deep-learning-models/

model.save('models/model') 

# EVALUATION
# The trained model can be used to perform predictions.

# Here we perform predictions on already used data, but we could use this on new data. 
predictions, accuracy = model.evaluate(X_val, y_val)
print(f'Accuracy: {accuracy*100:.2f}')