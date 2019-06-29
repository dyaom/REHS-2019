# Import `tensorflow`
import tensorflow as tf

input('.')

# Initialize two constants
x1 = tf.constant([1,1,2,3,5,8,13,21])
x2 = tf.constant([1,2,3,5,8,13,21,34])

# Multiply
result = tf.multiply(x1, x2)

# Print the result
print(result)
with tf.Session() as sess:
    print(sess.run(result))
