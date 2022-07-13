from django.db import models
import tensorflow as tf
import numpy as np
import cv2
# Create your models here.
class CustomDataset(tf.keras.utils.Sequence):
    def __init__(self, imgfiles, labels, batch_size, target_size=(64, 64), shuffle=False, scale=255, n_classes=1,
                 n_channels=3):
        self.batch_size = batch_size
        self.dim = target_size
        self.labels = labels
        self.imgfiles = imgfiles
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.n_channels = n_channels
        self.scale = scale

        self.c = 0
        self.on_epoch_end()

    def __len__(self):
        # returns the number of batches
        return int(np.floor(len(self.imgfiles) / self.batch_size))

    def __getitem__(self, index):
        # returns one batch
        indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]

        # Generate data
        X, y = self.__data_generation(indexes)
        return X, y

    def on_epoch_end(self):
        self.indexes = np.arange(len(self.imgfiles))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, list_IDs_temp):
        X = np.empty((self.batch_size, *self.dim, self.n_channels))
        y = np.empty((self.batch_size), dtype=int)

        # Generate data
        for i, ID in enumerate(list_IDs_temp):
            # Store sample
            img = cv2.imread(self.imgfiles[ID])
            try:
                img = cv2.resize(img, self.dim, interpolation=cv2.INTER_CUBIC)
            except:
                break
            X[i,] = img / self.scale

            # Store class
            y[i] = self.labels[ID]

            self.c += 1
        return X, y  # keras.utils.to_categorical(y, num_classes=self.n_classes)


class CustomPipeline(tf.keras.utils.Sequence):
    def __init__(self, data_x, data_y, batch_size=48, shuffle=False, n_classes=1):
        self.features = data_x
        self.labels = data_y
        self.batch_size = 48
        self.shuffle = shuffle
        self.n_features = self.features.shape[1]
        self.n_classes = 1
        self.on_epoch_end()

    def __len__(self):
        return int(np.floor(len(self.features) / self.batch_size))

    def __getitem__(self, index):
        indexes = self.indexes[index * self.batch_size:(index + 1) * self.batch_size]
        X, y = self.__data_generation(indexes)
        return X, y

    def on_epoch_end(self):
        self.indexes = np.arange(len(self.features))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, indexes):
        X = np.empty((self.batch_size, self.n_features))
        y = np.empty((self.batch_size), dtype=int)

        for i, ID in enumerate(indexes):
            X[i,] = self.features[ID]
            y[i,] = self.labels[ID]
        return X, y


class MultipleInputGenerator(tf.keras.utils.Sequence):
    """Wrapper of two generatos for the combined input model"""

    def __init__(self, X1, X2, Y, batch_size, target_size=(64, 64)):
        self.genX1 = CustomPipeline(X1, Y, batch_size=batch_size, shuffle=False)
        self.genX2 = CustomDataset(X2, Y, batch_size=batch_size, shuffle=False, target_size=target_size)

    def __len__(self):
        return self.genX1.__len__()

    def __getitem__(self, index):
        X1_batch, Y_batch = self.genX1.__getitem__(index)
        X2_batch, Y_batch = self.genX2.__getitem__(index)
        X_batch = [X1_batch, X2_batch]
        return X_batch, Y_batch


class TripleInputGenerator(tf.keras.utils.Sequence):
    """Wrapper of two generatos for the combined input model"""

    def __init__(self, X1, X2, Y, batch_size, target_size=(64, 64)):
        self.genX1 = CustomPipeline(X1, Y, batch_size=batch_size, shuffle=False)
        self.genX2 = CustomDataset(X2, Y, batch_size=batch_size, shuffle=False, target_size=target_size)
        # self.genX3 = CustomPipeline(X3, Y, batch_size=batch_size,shuffle=False)

    def __len__(self):
        return self.genX1.__len__()

    def __getitem__(self, index):
        X1_batch, Y_batch = self.genX1.__getitem__(index)
        X2_batch, Y_batch = self.genX2.__getitem__(index)
        # X3_batch, Y_batch = self.genX3.__getitem__(index)

        X_batch = [X1_batch, X2_batch]  # , X3_batch]
        return X_batch, Y_batch
