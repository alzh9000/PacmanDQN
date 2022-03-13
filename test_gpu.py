import tensorflow as tf
print(f"Tensorflow version: {tf.__version__}")
print(f"Physical devices detected by tensorflow: {tf.config.list_physical_devices()}")
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))