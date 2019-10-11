import random

import matplotlib.pyplot as plt
import tensorflow as tf


def showOnePicture():
    (xt, yt), (nul) = tf.keras.datasets.mnist.load_data();
    fig = plt.figure(figsize=(10, 10));

    plt.imshow(xt[random.randint(1, 60000)], cmap='Greys')

    plt.gcf().canvas.set_window_title("api");
    plt.show();


if __name__ == '__main__':
    showOnePicture()
    pass