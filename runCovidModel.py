import infections

R_same=0.9;
n_init_infected = 5;



#let's assume two cases, one with no second wave, one with second wave

#CASE 1: no second wave
n_infected_case1 = infections.getTotalInfected(R,n_init_infected,117);
"""
#CASE 2: second wave coming in october (1 month)
R_2ndwave_up=1.1;
R_2ndwave_down = .9;

n_infected_after1mo = infections.getTotalInfected(R,n_init_infected,30);
n_infected_after2mo = infections.getTotalInfected(R_2ndwave_up,n_init_infected,30);

infections.getTotalInfected(R,n_init_infected,60)


#simple assumption of 1% mortality from total infected population 
n_deaths = .01*n_infected_2mo;
 infections.getTotalInfected(R,n_init_infected,60)
 """