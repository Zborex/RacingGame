import tensorflow as tf
import numpy as np
import random
from pyglet.window.key import KeyStateHandler
from . import actor, critic, memory

np.random.seed(1)
tf.set_random_seed(1)

MAX_EPISODES = 500
MAX_EP_STEPS = 600
LR_A = 1e-4  # learning rate for actor
LR_C = 1e-4  # learning rate for critic
GAMMA = 0.9  # reward discount
REPLACE_ITER_A = 800
REPLACE_ITER_C = 700
MEMORY_CAPACITY = 2000
BATCH_SIZE = 16
VAR_MIN = 0.1
RENDER = True
LOAD = False
DISCRETE_ACTION = False

STATE_DIM = 1
ACTION_DIM = 1
ACTION_BOUND = [-1, 1]

# all placeholder for tf
with tf.name_scope('S'):
    S = tf.placeholder(tf.float32, shape=[None, STATE_DIM], name='s')
with tf.name_scope('R'):
    R = tf.placeholder(tf.float32, [None, 1], name='r')
with tf.name_scope('S_'):
    S_ = tf.placeholder(tf.float32, shape=[None, STATE_DIM], name='s_')

sess = tf.Session()

# Create actor and critic.
actor = actor.Actor(sess, ACTION_DIM, ACTION_BOUND[1], LR_A, REPLACE_ITER_A)
critic = critic.Critic(sess, STATE_DIM, ACTION_DIM, LR_C, GAMMA, REPLACE_ITER_C, actor.a, actor.a_)
actor.add_grad_to_graph(critic.a_grads)

M = memory.Memory(MEMORY_CAPACITY, dims=2 * STATE_DIM + ACTION_DIM + 1)

saver = tf.train.Saver()
path = './discrete' if DISCRETE_ACTION else './continuous'

if LOAD:
    saver.restore(sess, tf.train.latest_checkpoint(path))
else:
    sess.run(tf.global_variables_initializer())


def update_states():
    return


def get_key_handler():
    return RandomKeyStatHandler()


class RandomKeyStatHandler(KeyStateHandler):
    def __getitem__(self, item):

        return bool(random.getrandbits(1))
