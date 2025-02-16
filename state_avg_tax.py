tax_rates_income = {                    
    "Alabama": {                        
        "single":{                   
        (0,501): 0.02,
        (501,3001): 0.04,
        (3001,float('inf')): 0.05
        },
        "married": { 
        (0,1001): 0.02,
        (1001,6001): 0.04,
        (6001,float('inf')): 0.05
        }
    },
    "Alaska": { #type: ignore
        "single": {
        (0,11601): 0.10,
        (11601,47151): 0.12,
        (47151,100526): 0.22,
        (100526,191951): 0.24,
        (191951,243725): 0.32,
        (243725,609350): 0.35,
        (609350,float('inf')): 0.37
        },
        "married": {
        (0, 23200): 0.10,
        (23201, 94300): 0.12,
        (94301, 201050): 0.22,
        (201051, 383900): 0.24,
        (383901, 487450): 0.32,
        (487451, 731200): 0.35,
        (731201, float('inf')): 0.37
        }
    },
    "Arizona": {
        "single":{ 
        (0,)
        }
    }
}# type: ignore

#type: ignore
