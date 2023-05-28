# -*- coding: utf-8 -*-

# -- Sheet --

# Uczenie DCGAN na zbiorze MNIST (z użyciem Keras)
# Użyjemy sieci CNN
# Zbudujemy dwie sieci: Generator i Dyskryminator, gdzie jedna będzie tworzyć obrazy podobne do tych ze zbioru danych
# a druga sieć będzie weryfikować obrazy oryginalne i wygenerowane
# Na pewnym etapie sieć dyskryminująca podpowiada generatorowi jak tworzyć najlepsze podróbki obrazów!!!


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.keras.layers import Dense, Input, Activation
from tensorflow.keras.layers import Conv2D, Flatten
from tensorflow.keras.layers import Reshape, Conv2DTranspose
from tensorflow.keras.models import Model
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import load_model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.datasets import mnist

import numpy as np
import os
import matplotlib.pyplot as plt
import math
import argparse

#funkcja budująca sieć generator
def build_generator(inputs,image_size):
    """
    Stos warstw BN-Relu-Conv2DTranspose do generowania fałszywych obrazów.
    wyjściowa funkcja aktywacji: sigmoid /ta fukcja łatwiej osiąga zbieżność niż tanh/
    ARGUMENTY:
    inputs -> warstwa wejściowa - wektor z
    image_size (tensor) -> zakładamy kształ kwadratu
    ZWRACA:
    generator -> model generatora
    """

    #parametry sieci
    image_resize = image_size//4
    kernel_size = 5
    layer_filters = [128,64,32,1]

    x = Dense((image_resize**2)*layer_filters[0])(inputs)
    x = Reshape((image_resize,image_resize,layer_filters[0]))(x)

    for filters in layer_filters:
        if filters>layer_filters[-2]:
            strides = 2
        else:
            strides = 1
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = Conv2DTranspose(filters=filters,
                            kernel_size=kernel_size,
                            strides=strides,
                            padding='same')(x)
    x = Activation('sigmoid')(x)
    generator = Model(inputs,x,name='generator')
    return generator

#konstruowanie modelu dyskryminatora
def build_discriminator(inputs):
    """
    Stos warstw LeakyRelLU-Conv2D do odróżniania obrazów prawdziwych.
    Rezygnacja z BN -> brak osiągnięcia zbieżności
    ARGUMENTY:
    inputs -> warstwa wejściowa dyskryminatora
    ZWRACA:
    dyskryminator -> model dyskryminatora
    """
    kernel_size = 5
    layer_filters = [32,64,128,256]

    x = inputs
    for filters in layer_filters:
        if filters == layer_filters[-1]:
            strides = 1
        else:
            strides = 2
        x = LeakyReLU(alpha=0.2)(x)
        x = Conv2D(filters=filters,
                   kernel_size=kernel_size,
                   strides=strides,
                   padding='same')(x)
    x = Flatten()(x)
    x = Dense(1)(x)
    x = Activation('sigmoid')(x)
    discriminator = Model(inputs,x,name='discriminator')
    return discriminator

def plot_images(generator,
                noise_input,
                show=False,
                step=0,
                model_name='gan'):
    """
    generowanie i wyświetlanie fałszywych obrazów (na kwadratowej siatce)
    Argumenty:
        generator -> model generatora
        noise_input -> tablica wektorów z
        show -> pokazywać czy nie!
        step -> dodanie do nazwy pliku zapisywanego obrazu
        model_name -> nazwa modelu
    """
    os.makedirs(model_name,exist_ok=True)
    filename = os.path.join(model_name,"%5d.png" %step)
    images = generator.predict(noise_input)
    plt.figure(figsize=(2.2,2.2))
    num_images = images.shape[0]
    image_size = images.shape[1]
    rows = int(math.sqrt(noise_input.shape[0]))
    for i in range(num_images):
        plt.subplot(rows,rows,i+1)
        image = np.reshape(images[i],[image_size,image_size])
        plt.imshow(image,cmap='gray')
        plt.axis('off')
    plt.savefig(filename)
    if show:
        plt.show()
    else:
        plt.close('all')

#funkcja trenująca dla obu sieci
def train(models,x_train,params):
    """
    uczenie naprzemienne sieci dyskryminatora i generatora na próbkach
    1. Uczenie dyskryminatora na prawdziwych i fałszywych obrazach
    2. Uczenie generatora
    3. Generowanie przykładowych obrazów co pewien okres czasu /save_interval/

    Argumenty:
    models -> lista: generator, dyskryminator, model sieci
    x_train -> obrazy uczące (tensor)
    params: lista parametrów sieci
    """

    #komponenty modelu GAN
    generator, discriminator, adversarial = models

    #parametry sieci
    batch_size, latent_size, train_steps, model_name = params

    #obrz generatora zapisywany co 500 kroków
    save_interval = 500

    #wektor szumu -> pozwala widzieć ewolucję wyjść generatora podczas uczenia
    noise_input = np.random.uniform(-1.0,1.0,size=[16,latent_size])

    #liczba elementów w zbiorze uczącym
    train_size = x_train.shape[0]

    for i in range(train_steps):
        #uczenie się dyskrymonatora dla 1 próbki
        # próbka: obrazy prawdziwe (etykieta 1.0), podrabiane (etykieta 0.0)
        #obraz jest wybierany losowo ze zbioru
        rand_indexes = np.random.randint(0,train_size,size=batch_size)
        real_images = x_train[rand_indexes]
        #generowanie fałszywych obrazów z szumu
        #szum generowany z użyciem rozkładu jednostajnego
        noise = np.random.uniform(-1.0,1.0,size=[batch_size,latent_size])
        #generowanie fałszych obrazów
        fake_images = generator.predict(noise)
        #1 próbka danych uczących = obraz prawdziwy + obraz fałszywy
        x = np.concatenate((real_images, fake_images))
        y = np.ones([2*batch_size,1])
        y[batch_size:,:] = 0.0
        #uczenie dyskryminatora, zapis funkcji starty i dokładności
        loss,acc = discriminator.train_on_batch(x,y)
        log = "%d: [Funkcja straty dyskryminatora: %f, dokładność: %f]" % (i,loss,acc)
        #uczenie sieci współzawodniczącej /generator/
        #ponieważ wagi dyskrymiantora są "zamrożone" w sieci współzawodniczącej -> tylko generator podlega uczeniu
        noise = np.random.uniform(-1.0,1.0,size=[batch_size,latent_size])
        y = np.ones([batch_size,1])
        #w przeciwieństwie do uczenia dyskryminatora fałszywe obrazy nie są zapisywane w zmiennej
        #są one przesyłane od razu do dyskryminatora /do klasyfikacji/
        loss,acc = adversarial.train_on_batch(noise,y)
        log = "%d: [Funkcja straty dyskryminatora: %f, dokładność: %f]" % (i,loss,acc)
        print(log)

        #okresowy wydruk obrazów z generatora
        if (i+1)%save_interval == 0:
            plot_images(generator,
                        noise_input=noise_input,
                        show=False,
                        step=(i+1),
                        model_name=model_name)
    generator.save(model_name + ".h5")

def build_and_train_models():
    #załaduj zbiór MNIST
    (x_train, _), (_, _) = mnist.load_data()

    #przkształcenie danych dla CNN (28,28,1) i normalizacja
    image_size = x_train.shape[1]
    x_train = np.reshape(x_train,[-1,image_size,image_size,1])
    x_train = x_train.astype('float32')/255

    model_name = 'dcgan_mnist'
    #parametry sieci -> niejawny wektor ma 100 wymiarów
    latent_size = 100
    batch_size = 64
    train_steps = 40000
    lr = 2e-4
    decay = 6e-8
    input_shape = (image_size,image_size,1)

    #konstruowanie modelu dyskryminatora
    inputs = Input(shape=input_shape, name='discriminator_input')
    discriminator = build_discriminator(inputs)
    #rezygnujemy z optimizera 'adam' -> dyskryminator szybciej osiąga zbieżność z RMSprop
    optimizer = RMSprop(lr=lr,decay=decay)
    discriminator.compile(loss='binary_crossentropy',
                          optimizer=optimizer,
                          metrics=['accurracy'])
    discriminator.summary()

    #konstruowanie modelu generatora
    input_shape = (latent_size,)
    inputs = Input(shape=input_shape, name='z_input')
    generator = build_generator(inputs, image_size)
    generator.summary()

    #budowanie modelu sieci
    optimizer = RMSprop(lr=lr*0.5,decay=decay*0.5)
    #zamrożenie wag dyskryminatora przy trenowaniu sieci GAN
    discriminator.trainable = False
    #sieć współzawodnicząca(GAN) = generator + dyskryminator
    advarsarial = Model(inputs,
                        discriminator(generator(inputs)),
                        name=model_name)
    advarsarial.compile(loss='binary_crossentropy',
                        optimizer=optimizer,
                        metrics=['accuracy'])
    advarsarial.summary()
    #proces uczenie całości
    models = (generator,discriminator,advarsarial)
    params =(batch_size, latent_size, train_steps, model_name)
    train(models,x_train,params)

def test_generator(generator):
    noise_input = np.random.uniform(-1.0,1.0,size=[16,100])
    plot_images(generator,
                noise_input=noise_input,
                show=True,
                model_name="test_outputs")
if __name__ == '__main__':
    
    #blok wykonawczy
    parser = argparse.ArgumentParser()
    help_ = "Ładowanie modelu generatora z wytrenowanymi wagami z pliku h5"
    parser.add_argument("-g","--generator",help=help_)
    args = parser.parse_args()
    if args.generator:
        generator = load_model(args.generator)
        test_generator(generator)
    else:
        build_and_train_models()

