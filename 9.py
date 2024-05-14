import numpy as np
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder

X_train = np.array([[5.1, 3.5, 1.4, 0.2], 
                     [4.9, 3.0, 1.4, 0.2], 
                     [6.2, 2.9, 4.3, 1.3], 
                     [5.5, 2.3, 4.0, 1.3], 
                     [6.3, 2.5, 5.0, 1.9]])

y_train = np.array([0, 0, 1, 1, 2])  
X_test = np.array([[4.8, 3.4, 1.9, 0.2],
                    [6.0, 3.4, 4.5, 1.6],
                    [6.8, 3.0, 5.5, 2.1]])
y_test = np.array([0, 1, 2]) 
encoder = OneHotEncoder()
y_train_onehot = encoder.fit_transform(y_train.reshape(-1, 1)).toarray()
y_test_onehot = encoder.transform(y_test.reshape(-1, 1)).toarray()

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(4,), activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')  # Output layer with 3 classes (Iris species)
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train_onehot, epochs=50, batch_size=8, verbose=1)
loss, accuracy = model.evaluate(X_test, y_test_onehot, verbose=0)
print(f"Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}")
