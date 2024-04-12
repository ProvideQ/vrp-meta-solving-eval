import requests
import os
import json

#Generic Data:
url = 'http://localhost:8080/solve/vrp'
headers = {
    'Content-Type': 'application/json'
}

def dataLkhNoCluster(problem):
    #Running Lkh without Clustering does not print the Value of the Solution (because Lkh does not do this)
    #We do a work-wround for this, by applying k-means with k = 1, which does not cluster the problem, but prints the value

    #create Meta-Solver Strategy
    solver = 'edu.kit.provideq.toolbox.vrp.solvers.ClusterAndSolveVrpSolver'
    clusterer = 'edu.kit.provideq.toolbox.vrp.clusterer.KmeansClusterer'
    clusterSolver = 'edu.kit.provideq.toolbox.vrp.solvers.LkhVrpSolver'

    #create Data for API Request:
    data = {
        'requestContent': problem,
        'requestedSolverId': solver,
        'requestedSubSolveRequests': {
            'clusterable-vrp': {
                'requestedSolverId': clusterer,
                'requestedMetaSolverSettings': [{
                        "name": "kmeans-cluster-number",
                        "title": "Number of Kmeans Cluster (default: 3)",
                        "type": "INTEGER",
                        "number": 1
                    }],
                'requestedSubSolveRequests': {
                    'vrp': {
                        'requestedSolverId':clusterSolver
                    }
                }
            }
        }
    }
    return data
def dataLkhTwoPhase(problem):
    #create Meta-Solver Strategy
    solver = 'edu.kit.provideq.toolbox.vrp.solvers.ClusterAndSolveVrpSolver'
    clusterer = 'edu.kit.provideq.toolbox.vrp.clusterer.TwoPhaseClusterer'
    clusterSolver = 'edu.kit.provideq.toolbox.vrp.solvers.LkhVrpSolver'

    #create Data for API Request:
    data = {
        'requestContent': problem,
        'requestedSolverId': solver,
        'requestedSubSolveRequests': {
            'clusterable-vrp': {
                'requestedSolverId': clusterer,
                'requestedSubSolveRequests': {
                    'vrp': {
                        'requestedSolverId':clusterSolver
                    }
                }
            }
        }
    }
    return data
def dataQuboTspSolver(problem):
    #create Meta-Solver Strategy
    solver = 'edu.kit.provideq.toolbox.vrp.solvers.ClusterAndSolveVrpSolver'
    clusterer = 'edu.kit.provideq.toolbox.vrp.clusterer.TwoPhaseClusterer'
    tspToQubo = 'edu.kit.provideq.toolbox.vrp.solvers.QuboTspSolver'
    qrispQubo = 'edu.kit.provideq.toolbox.qubo.solvers.QrispQuboSolver'

    #create Data for API Request:
    data = {
        'requestContent': problem,
        'requestedSolverId': solver,
        'requestedSubSolveRequests': {
            'clusterable-vrp': {
                'requestedSolverId': clusterer,
                'requestedSubSolveRequests': {
                    'vrp': {
                        'requestedSolverId': tspToQubo,
                        'requestedSubSolveRequests': {
                            'qubo': {
                                'requestedSolverId': qrispQubo
                            }
                        }
                    }
                }
            }
        }
    }
    return data
def dataAnnealer(problem):
    #create Meta-Solver Strategy
    solver = 'edu.kit.provideq.toolbox.vrp.solvers.ClusterAndSolveVrpSolver'
    clusterer = 'edu.kit.provideq.toolbox.vrp.clusterer.TwoPhaseClusterer'
    tspToQubo = 'edu.kit.provideq.toolbox.vrp.solvers.QuboTspSolver'
    dwaveSimulator = 'edu.kit.provideq.toolbox.qubo.solvers.DwaveQuboSolver'

    #create Data for API Request:
    data = {
        'requestContent': problem,
        'requestedSolverId': solver,
        'requestedSubSolveRequests': {
            'clusterable-vrp': {
                'requestedSolverId': clusterer,
                'requestedSubSolveRequests': {
                    'vrp': {
                        'requestedSolverId': tspToQubo,
                        'requestedSubSolveRequests': {
                            'qubo': {
                                'requestedSolverId': dwaveSimulator
                            }
                        }
                    }
                }
            }
        }
    }
    return data

#load all files:
script_directory = os.path.dirname(os.path.realpath(__file__))
files_in_directory = [f for f in os.listdir(script_directory) if os.path.isfile(os.path.join(script_directory, f))]

#file that stores solution for eval:
eval_file = script_directory
eval_file += "/results.txt"
#clear eval file before running a new evaluation:
with open(eval_file, 'w') as f:
    pass

for file in files_in_directory:
    #TODO: Change to "*.txt"
    if file.__contains__('.txt'):
        with open(file) as f:
            problem = f.read()
        print(f"Starting to Solve Problem: " + file + "\n")

        #write new entry in eval file:
        with open(eval_file, 'a') as f:
            f.write(file +  ', ')

        #Solve the Problem (Make the API Request)
        data = dataQuboTspSolver(problem)
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(result)
        else:
            print('Failed to make POST request:' , response.status_code)

        #write main results in eval file:
        with open(eval_file, 'a') as f:
            #format solutionData so that it only includes the tour costs
            solutionData = str(result['solutionData'])
            parts = solutionData.split()
            
            value = -1
            for part in parts:
                if '.' in part:
                    value = part
                    break
            if (value == -1): value = 'No Solution'

            time = str(result['executionMilliseconds'])
            f.write(value +  ', ' + time + '\n')

        #save complete solution in an extra file:
        path = script_directory 
        path += "/Solutions/"
        path += file
        print(path)

        with open(path, 'w') as f: 
            f.write(json.dumps(result, indent=4)) 

        print("Done")