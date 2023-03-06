import matplotlib.pyplot as plt
import numpy as np

def plot_history(history, metrics, restore_weights=True, yscale='linear', save_folder=None):
    """Plot the history af all specified metrics, comparing training and testing metrics."""

    if restore_weights and 'val_loss' in history.history.keys():
        # Find the epoch with the best result (which the model was restored to).
        best_epoch = np.argmin(history.history['val_loss'])
        print(f"Restored weights to epoch: {best_epoch}")
    else:
        best_epoch = None
  
    # Plot the history of each metric.
    for metric in metrics:
        plt.figure()
        plt.title(metric)
        plt.xlabel('epoch')
        plt.ylabel(metric)
        plt.yscale(yscale)

        # Trained metric.
        plt.plot(history.history[metric])
        print(f"{metric}: {history.history[metric][best_epoch or len(history.history[metric]) - 1]}")
        
        val_metric = 'val_' + metric
        if val_metric in history.history.keys():
            # Same metric evaluated on the test set.
            plt.plot(history.history[val_metric])
            print(f"{val_metric}: {history.history[val_metric][best_epoch or len(history.history[metric]) - 1]}")

            # Highlight the epoch the weights were restored to.
            if restore_weights:
                plt.plot(best_epoch, history.history[val_metric][best_epoch], 'ro')
        
        plt.legend(['train', 'validation'], loc='best')

        if save_folder:
            plt.savefig(f'{save_folder}/{metric}')
        plt.show()
