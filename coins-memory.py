import random
import statistics


def tossCoin():
    global totalTosses
    result = random.choice(['head', 'tails'])
    totalTosses -= 1
    return result

def checkLastToss(coin):
    global results,row_ok, has_memory

    if coin == results[-1]:
        results.append(coin)
        if len(results) == objective:
            row_ok += 1
            coin = tossCoin()
            if coin == results[-1]:
                has_memory += 1
                results.pop(0)
            else:
                results = []
                results.append(coin)
    else:
        results = []
        results.append(coin)

def oneSimulation(numbTosses):
    global results, row_ok, has_memory, totalTosses
    row_ok = 0
    has_memory = 0
    results = []
    totalTosses = numbTosses

    ## Begin
    coin = tossCoin()
    results.append(coin)

    ## Iterate
    while totalTosses > 1:
        coin = tossCoin()
        checkLastToss(coin)

    if has_memory > 0:
        percentage = round(has_memory * 100 / row_ok, 4)
    else:
        percentage = 0

    each_result.append(percentage)

    print('Percentage of coins with memory:', percentage)
    print('')
    ## print('Row ok:', row_ok)
    ## print('Memory:', has_memory)
    ## print('Has memory', percentage, '%')
    ## print('- - - - - - - - - - ')



# How many coincidences in a row generates memory on a coin?
# if 10, check the 11th toss.
objective = 10

# Store Results
each_result = []


wantedTosses = 100000
wantedSimulations = 200

sim_numb = 0
for i in range(wantedSimulations):
    sim_numb += 1
    print('# Simulation:', sim_numb)
    oneSimulation(wantedTosses)

print('')
print('Do the coins have memory?')
print("Let's see the results of this study")
print('Amount of simulations:', wantedSimulations, 'Amount of tosses in each simulation:', wantedTosses)
print('Amount of simulations:', sim_numb)
print('List of results:', each_result)
print('Average of coins with memory:', statistics.mean(each_result))
print('Total Tosses:', wantedTosses * wantedSimulations)
print('Amount of succesful cases:', len(each_result))










