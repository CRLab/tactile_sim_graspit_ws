import matplotlib.pyplot as plt
import numpy as np

f = open('handStates', 'r')
lines = f.readlines()

for i in range(0,len(lines)/3):
	sim = lines[i*3]
	real=lines[i*3 + 1]

	sim = [float(n) for n in sim.replace(' ', '').split(',')[1:-1]]
	real = [float(n) for n in real.replace(' ', '').split(',')[1:-1]]

	sim = np.asarray(sim) #/ max(sim)
	simdomain = np.asarray(range(len(sim)))
	sim_mask = sim > 0.0

	real = np.asarray(real) #/ max(real)
	realdomain = np.asarray(range(len(real)))
	real_mask = real > 0.3

	sim = sim[sim_mask]
	simdomain = simdomain[sim_mask]
	real = real[real_mask]
	realdomain = realdomain[real_mask]


	#splt = plt.scatter(range(len(sim)), sim)
	#rplt = plt.scatter(range(len(real)), real, color='r')

	splt = plt.scatter(simdomain, sim)
	rplt = plt.scatter(realdomain, real, color='r')

	plt.legend([splt, rplt], ['Simulated', 'Real'])
	plt.title('Touching the pringles can')
	plt.show()