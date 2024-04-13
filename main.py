import numpy as np
import time
import tensorflow as tf

from recording_helper import record_audio, terminate
# from tf_helper import preprocess_audiobuffer
# from tf_helper import get_spectrogram



# !! Modify this in the correct order
commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']

loaded_model = tf.saved_model.load("saved")

# print(loaded_model.signatures)

def predict_mic():
    audio = record_audio()
    # spec = preprocess_audiobuffer(audio)
    # # spec = get_spectrogram(audio)
    audio = tf.expand_dims(audio, 0)  # Add batch dimension, shape = (1, 16000)
    audio = tf.cast(audio, tf.float32)  # Convert audio to float32
    prediction = loaded_model(audio)
    prediction = prediction['predictions']
    # Check the shape of prediction
    # print("Shape of prediction:", prediction.shape)

    label_pred = np.argmax(prediction, axis=1) # axis = 1 means we are taking the max of each row (each row is a prediction)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    return command

if __name__ == "__main__":
    from turtle_helper import move_turtle
    while True:
        command = predict_mic()
        move_turtle(command)
        if command == "stop":
            terminate()
            break