from data import load_dataset
from model import get_model
from output import plot_history, plot_samples


# Load data from the directory where images are stored.
(X_train, y_train), (X_test, y_test), one_hot_encoder = load_dataset(data_dir="data")
# Show a subset of the samples.
plot_samples(X_train[0:9], y_train[0:9], one_hot_encoder, columns=3)

model = get_model()
# Train the model.
history = model.fit(X_train, y_train, epochs=10, batch_size=32)
plot_history(history, ['loss', 'accuracy'], restore_weights=False)

# Save model for future use.
model.save('models/model.h5')
