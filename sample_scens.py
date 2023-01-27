# -*- coding: utf-8 -*-
"""
This file contains code to replicate the example scenarios published in 
the manuscript titled "FPsim: An agent-based model of family planning", 
first published on XXX date at YYY journal.

Created on Fri Jan 27 10:05:56 2023

@author: michelleob
"""

debug = 0

if __name__ == '__main__':

    import fpsim as fp

    n_agents   = [5_000, 100][debug]
    start_year = [1980, 2010][debug]
    end_year   = 2030
    repeats    = [3, 1][debug]
    year       = 2020  #intervention year for all scenarios unless otherwise specified
    limiters   = ['>35']
    youth      = ['<18', '18-20']
    location   = 'Senegal'
    
    
    pars = fp.pars(n_agents=n_agents, start_year=start_year, end_year=end_year, location=location)
    
 
## Prepare basic set of scenarios ##

# Increase injectable efficacy

s1 = fp.make_scen(eff={'Injectables':0.99}, year=year)

# Double rate of injectables initiation
        
s2 = fp.make_scen(method='Injectables', init_factor=2, year=year)

# Target 35+ with double injectable uptake

s3 = fp.make_scen(method='Injectables', init_factor=2, year=year, ages=limiters)

# Combine scenarios 1 and 3

s4 = s1 + s3


##More advanced scenarios 

## Three-part scenario to add in new contraceptive method 

method = 'new injectables'
kw = dict(method=method)
d_kw = dict(dest=method)

#initial introduction of new method, with 1.5% probability of uptake for 35+ population
s5a = fp.make_scen(
    year=year,
    probs=[
    dict(copy_from='Injectables', method=method, ages=limiters),
    dict(disc_factor=0.5, **kw),
        ]
    )

#anticipate switching from existing injectables
s5b = fp.make_scen(
    year=year,
    probs=[
        dict(source='Injectables', value=0.20, **d_kw)
        ]
    )

#Staggered introduction to youth sub-population

s5c = fp.make_scen(
    year = 2023,
    probs = [
    dict(copy_from='Injectables', method=method, ages=youth),
    dict(init_value=0.015, **kw),
        ]
    )

s5 = s5a + s5b + s5c

#%% Create sims
scens = fp.Scenarios(pars=pars, repeats=repeats)
scens.add_scen(label='Baseline')
scens.add_scen(s1, label='Increase injectable efficacy')
scens.add_scen(s2, label='Double injectable initiation, all ages')
scens.add_scen(s3, label='Double injectable initiation, 35+ only')
scens.add_scen(s4, label='Increase injectable efficacy and double initiation for 35+')

# Run scenarios
scens.run(serial=debug)


## Integrated plot options
scens.plot()    
scens.plot('cpr')
scens.plot('method')

#%% Create sims
scens = fp.Scenarios(pars=pars, repeats=repeats)
scens.add_scen(label='Baseline')
scens.add_scen(s5, label='Introduce new injectable')

# Run scenarios
scens.run(serial=debug)


## Integrated plot options
scens.plot()    
scens.plot('cpr')
scens.plot('method')
