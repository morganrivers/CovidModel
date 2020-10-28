from random import randint
from scipy.stats import gamma
class RunResult: 
  def __init__(self): 
    self.infected = []
    self.population = []
    self.times = []
    self.n_infected = 0

def getTotalInfected(R,init_infected,n_days):
  #using a 1 day time interval
  inf_age_min = 0
  inf_age_max = 16 # 16 days
  start_t = 1
  last_t = n_days

  #gamma distribution terms
  alpha = 7.9
  beta = 1.2

  n = [0 for i in range(0,inf_age_max+1)]
  times = list(range(start_t, last_t+1)) #all days under consideration
  ages = list(range(0, inf_age_max+1)) #all the ages of infections considered
  g = [0]*(inf_age_max+1)


  sum_g=0
  for i in range(0,inf_age_max+1):
  	g[i] = gamma.pdf(i, a=alpha, scale=1/float(beta)) #normalized gamma distribution of rates of birth
  	sum_g += g[i]

  n=[element * R for element in g]

  inf = [0 for i in range(0,last_t+1)] 
  inf[0]=init_infected #t=0 we had an infection

  p = [0 for i in range(0,last_t+1)] #population over time
  p[0]=inf[0]
  for t in times:
    
    inf_t=0
    for a in ages:
      new_time=t-a
      inf_t += inf[new_time]*n[a] #Note inf[-num] = 0.

    inf[t] = inf_t
    p[t] = p[t-1]+inf[t]

  infections = inf[start_t:last_t+1]
  population = p[start_t:last_t+1]
  rr = RunResult()
  rr.infections = infections
  rr.population = population
  rr.times = times
  rr.n_infected = population[last_t-1]

  return rr