'''import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)

# Display the first image and prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()'''

import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0
network = models.Sequential([
     layers.Flatten(input_shape=(28, 28)),layers.Dense(128, activation='relu'),layers.Dense(10, activation='softmax')])

network.compile(
                 loss='sparse_categorical_crossentropy',
                 optimizer='adam', metrics=['accuracy'
                ])
network.fit(train_images, train_labels, epochs=5)

loss, accuracy = network.evaluate(test_images, test_labels)
print("Accuracy:", accuracy)
results = network.predict(test_images)
plt.imshow(test_images[0], cmap='binary')
plt.title(f"Predicted Digit: {results[0].argmax()}")
plt.show()