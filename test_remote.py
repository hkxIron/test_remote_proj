import tensorflow as tf
import sys

"""
使用远程编辑有很多不好的地方,
1. 没有代码提示
2. 无法查看文档
3. idea会自动当相关的python代码下载下来,之后会就会有提示了
"""

sess = tf.Session()
const = tf.constant("hello")
print("sess out: ", sess.run(const))
sess.close()

print("python version: ", sys.version)
print("hello world.")
print("tf version: ", tf.__version__)
