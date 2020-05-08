from scipy.io import loadmat
from elmm_admm import elmm_admm
import numpy as np

sample = loadmat('real_data_1.mat')

data = sample['data']
S0 = sample['S0']

m,n,L = data.shape

# print(data.transpose().flatten())  # data[:]


A_SCLSU = SCLSU(data, S0)

maxiter_anls = 100;
maxiter_admm = 100;
epsilon_s = 10^(-3);
epsilon_a = 10^(-3);
epsilon_psi = 10^(-3);
epsilon_admm_abs = 10^(-2);
epsilon_admm_rel = 10^(-2);


A_init = A_SCLSU;
psis_init = np.ones(A_init.shape);


