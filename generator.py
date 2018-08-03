rnn = RNN()
y = rnn.step(x)

class RNN:
    def __init__(self, ):
        self.W_xh = np.randn()
        self.W_hh =
        self.W_hy =

    def step(self, x):
        self.h = np.tanh(np.dot(self.W_xh, x) + np.dot(self.W_hh, self.h))
        y = np.tanh(np.dot(self.h, self.W_hy))
