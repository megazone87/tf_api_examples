import tensorflow as tf

string = tf.constant("1234567890", shape=(1,))
int = tf.string_to_number(string, tf.int64)

with tf.Session() as sess:
    print(int.eval()[0])
