import numpy as np
from tensorflow.keras.models import load_model

from data import load_dataset
from output import plot_confusion_matrix


# Load data.
(X_train, y_train), (X_test, y_test), one_hot_encoder = load_dataset(data_dir="data")

# Load the model from the saved file.
model = load_model('models/model.h5')

# Predictions.
y_test_preds = model(X_test)
y_test_labels = one_hot_encoder.inverse_transform(y_test).squeeze()
y_test_pred_labels = one_hot_encoder.inverse_transform(y_test_preds).squeeze()

categories = one_hot_encoder.categories_[0].tolist()

"""
Build and plot the confusion matrix.

The confusion matrix represents the results of all predictions from our model and is useful to determine
both its general performance and specific problems (e.g. one digit could tend to be confused with another one).
"""
confusion_matrix = np.zeros((10, 10))
for label, pred_label in zip(y_test_labels, y_test_pred_labels):
    idx_true = categories.index(label)
    idx_pred = categories.index(pred_label)
    confusion_matrix[idx_true, idx_pred] += 1
confusion_matrix_norm = confusion_matrix / np.expand_dims(np.sum(confusion_matrix, axis=1), axis=-1)

plot_confusion_matrix(confusion_matrix_norm, categories, categories, "{x:.4f}")

"""
Calculate and plot the confusion matrix with wrong predictions only.

This is obtained by removing the diagonal. This is not a canonical form of the confusion matrix, but it makes
it easier to see the colors and where wrong predictions accumulate if the network is really accurate.

An alternative would be to use logarithmic color scaling.
"""
confusion_matrix_errors = confusion_matrix - np.diag(np.diag(confusion_matrix))

plot_confusion_matrix(confusion_matrix_errors, categories, categories, "{x:.0f}")
