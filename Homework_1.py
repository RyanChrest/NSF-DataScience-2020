# (poor) estimation of pi 

print(4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11))
print(4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15))

# population growth (constant)

starting_population = 312032486

birth_rate_per_minute = 60 / 7 # 60 seconds, divided by 1 birth per 7 seconds
death_rate_per_minute = 60 / 13
immigration_rate_per_minute = 60 / 45

total_rate_per_minute = birth_rate_per_minute + immigration_rate_per_minute - death_rate_per_minute

net_change_population_per_year = 365 * 24 * 60 * total_rate_per_minute # days * hours * minutes * rate

for x in range(1, 6):
    print(f'Population for Year {x}:', round(starting_population + x * net_change_population_per_year))
    
# Compound interest calculator

investmentAmount = float(input('Enter investment amount: ') or '0')

interest_rate = float(input('Enter interest rate (50% = 0.50): ') or '0')

n_periods = int(input('Enter periods to compound: ') or '0')

future_value = round(investmentAmount * (1 + interest_rate) ** n_periods, 2)
print('Future Value:', future_value)
