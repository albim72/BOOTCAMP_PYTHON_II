import tensorflow as tf
from tensorflow.keras.datasets import mnist
import os

#pobranie danych
(mnist_train,_), (mnist_test,_)= mnist.load_data()

#definicja strategii dystrybucji
strategy = tf.distribute.MirroredStrategy()
print(f"liczba platform: {strategy.num_replicas_in_sync}")
