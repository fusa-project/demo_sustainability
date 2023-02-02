import numpy as np
from matplotlib import pyplot as plt


def find_duration_from_predictions(predictions):
    duration = 0.0
    for segments in predictions.values():
        for segment in segments:
            if segment['end'] > duration:
                duration = segment['end']
    return duration


def plot_prediction_matrix(predictions, xaxis_resolution=1000):
    categories = list(predictions.keys())
    duration = find_duration_from_predictions(predictions)
    prediction_matrix = np.zeros(shape=(xaxis_resolution, len(categories)))
    for k, segments in enumerate(predictions.values()):
        for segment in segments:
            start_idx = int(xaxis_resolution*segment['begin']/duration)
            end_idx = int(xaxis_resolution*segment['end']/duration)
            prediction_matrix[start_idx:end_idx, k] = segment['probability']

    fig, ax = plt.subplots(figsize=(8, 4.5), tight_layout=True)
    img = ax.pcolormesh(prediction_matrix.T, vmin=0, vmax=1, cmap=plt.cm.Blues)
    plt.colorbar(img)
    ax.set_xticks(np.linspace(0, xaxis_resolution, num=13))
    ax.set_xticklabels(np.linspace(0, duration, num=13).astype('int'))
    ax.set_yticks(np.arange(len(categories))+0.5)
    ax.set_yticklabels(categories);
    ax.set_xlabel('Time [s]')
    ax.grid()

