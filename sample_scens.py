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

    n_agents   = [10_000, 100][debug]
    start_year = [1980, 2010][debug]
    end_year   = 2030
    repeats    = [3, 1][debug]
    year       = 2020  #intervention year for all scenarios unless otherwise specified
    youth_ages = ['<18', '18-20']
    
    
    pars = fp.pars(n_agents=n_agents, start_year=start_year, end_year=end_year)
    
    
