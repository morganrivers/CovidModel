import matplotlib as mpl
import matplotlib.pyplot as plt
import infections

#number of days till vaccine
n_days = 117

#rough percentage population with it
prevalence = .01

#duration of infection is roughly a week on average
inf_duration = 7 #days

#imagine the set of 1% of population with it cycles through every 8 days (there have been cases of people getting it twice)
daily_risk = prevalence/float(inf_duration)
weekly_baseline_risk = daily_risk*7

#now imagine you've increased your daily risk by twice the average resident 
#(not hard to do, number of people in contact with is probably lognormally distributed)

#up to 2 weeks before the final
weeks = list(range(0,n_days/7-2))
avg_baseline_infect = [0 for i in range(0,n_days/7-2)]
avg_increased_infect = [0 for i in range(0,n_days/7-2)]

#each week, recalculate the number of people you will probably infect with R=.9
for week in weeks:

	days_remaining = n_days-week*7
	
	result_bl = infections.getTotalInfected(.9,weekly_baseline_risk,days_remaining);
	result_increased = infections.getTotalInfected(.9,2*weekly_baseline_risk,days_remaining);
	avg_baseline_infect[week] = result_bl.n_infected
	avg_increased_infect[week] = result_increased.n_infected

# see https://www.cdc.gov/motorvehiclesafety/impaired_driving/impaired-drv_factsheet.html
print("baseline infect: " + str(sum(avg_baseline_infect)))

#assumes: .5% mortality (.05 better estimate for young people)
print("increased exposure infect: " + str(sum(avg_increased_infect)))
at_fault_mortality = (sum(avg_increased_infect)-sum(avg_baseline_infect))/float(200)
print("deaths at fault for: "+str(at_fault_mortality))

yearly_drunk_traffic_fatalities_us = 10511
yearly_drunk_driving_trips = 111e6
drunk_driving_danger = yearly_drunk_traffic_fatalities_us/float(yearly_drunk_driving_trips)

print("mortaility drunk driving trip: "+str('{0:.10f}'.format(drunk_driving_danger)))

#https://news.gallup.com/poll/264932/percentage-americans-own-guns.aspx
#assumes ALL gun deaths due to personal gun owned, 
yearly_gun_deaths_us = 39773
american_pop = 328e6
gun_ownership = .33*american_pop
avg_danger_owning_gun = yearly_gun_deaths_us/float(gun_ownership)



print("mortality danger of owning a gun: "+str(avg_danger_owning_gun))
f=plt.figure(1)
plt.scatter(weeks,avg_baseline_infect)
f.show()

print("mortality danger of giving someone the flu: "+str(avg_danger_owning_gun))



g=plt.figure(2)
plt.scatter(weeks,avg_increased_infect)
plt.show()


#days over which we care
n_days = 10
p_safe = 1-prevalence;