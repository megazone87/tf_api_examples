import tensorflow as tf

string = tf.constant("a,b,c,d", shape=(1,))
str_list = tf.string_split(string, delimiter=",").values

with tf.Session() as sess:
    strs = [i.decode() for i in str_list.eval()]
    print(strs)
