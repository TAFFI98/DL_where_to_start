import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot_samples(X, y, one_hot_encoder, columns=3):
    """Show the images and corresponding labels."""
    N = y.shape[0]
    rows = int(np.ceil(N / columns))

    for i, (sample_X, sample_y) in enumerate(zip(X, y)):
        # y values are one-hot-encoded so we need to recover the label (the digit).
        label = one_hot_encoder.inverse_transform(sample_y).squeeze()

        plt.subplot(rows, columns, i+1)
        # .squeeze() removes the single channel which otherwise causes an error in some versions of matplotlib.
        plt.imshow(sample_X.squeeze(), cmap=plt.get_cmap('gray'))
        plt.xlabel(f"Label: {label}")
    plt.tight_layout()
    plt.show()


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", xlabel="", ylabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("white", "black"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


def plot_confusion_matrix(data, row_labels, col_labels, valfmt):
    fig, ax = plt.subplots()
    im, cbar = heatmap(data, row_labels, col_labels, xlabel="Predicted label", ylabel="True label")
    annotate_heatmap(im, valfmt=valfmt)
    plt.show()


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
