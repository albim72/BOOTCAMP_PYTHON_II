import tensorflow as tf
from tensorflow.keras.datasets import mnist
import os

#pobranie danych
(mnist_train,_), (mnist_test,_)= mnist.load_data()

#definicja strategii dystrybucji
strategy = tf.distribute.MirroredStrategy()
print(f"liczba platform: {strategy.num_replicas_in_sync}")

#konfiguracja potoku wejściowego
num_train_examples = len(mnist_train)
num_test_examples = len(mnist_test)

BUFFER_SIZE = 10000
BATCH_SIZE_PER_REPLICA = 64
BATCH_SIZE = BATCH_SIZE_PER_REPLICA*strategy.num_replicas_in_sync

#funkcja normalizująca
# def scale(image,label):
#     image = tf.cast(image,tf.float32)
#     image /= 255
#     return image, label

mnist_train = mnist_train/255.0
mnist_test = mnist_test/255.0

with strategy.scope():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32,3,activation='relu',input_shape=(28,28,1)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  optimizer=tf.keras.optimizers.Adam(),
                  metrics=['accuracy'])




model.fit(mnist_train,epochs=12)
