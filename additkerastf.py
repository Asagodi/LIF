import tensorflow as tf


def get_weights_TF(model, layer):
    "Gives numpy array of weights of a layer."
    x = model.weights[layer]
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)
    weight_mat = sess.run(x)    
    return weight_mat
