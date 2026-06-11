
import numpy as np

lista=[0, 1, 2, 3, 4, 5, 6, 7, 8]

def calculate(list): 
    
    if len(list) != 9:
        return "ValueError: List must contain nine numbers."
    
    else:
        mat = np.reshape(list, (3,3))
        calculations = {
              'mean': [[np.mean(mat[:,0]), np.mean(mat[:,1]), np.mean(mat[:,2])],
            [np.mean(mat[0,:]), np.mean(mat[1,:]), np.mean(mat[2,:])], np.mean(list)],
        
              'variance': [[np.var(mat[:,0]), np.var(mat[:,1]), np.var(mat[:,2])],
            [np.var(mat[0,:]), np.var(mat[1,:]), np.var(mat[2,:])], np.var(list)],
        
              'standard deviation': [[np.std(mat[:,0]), np.std(mat[:,1]), np.std(mat[:,2])],
            [np.std(mat[0,:]), np.std(mat[1,:]), np.std(mat[2,:])], np.std(list)],
        
              'max': [[np.amax(mat[:,0]), np.amax(mat[:,1]), np.amax(mat[:,2])],
            [np.amax(mat[0,:]), np.amax(mat[1,:]), np.amax(mat[2,:])], np.amax(list)],
        
              'min': [[np.amin(mat[:,0]), np.amin(mat[:,1]), np.amin(mat[:,2])],
            [np.amin(mat[0,:]), np.amin(mat[1,:]), np.amin(mat[2,:])], np.amin(list)],
        
              'sum': [[np.sum(mat[:,0]), np.sum(mat[:,1]), np.sum(mat[:,2])],
            [np.sum(mat[0,:]), np.sum(mat[1,:]), np.sum(mat[2,:])], np.sum(list)]
        
                }

        return calculations


calculate(lista)
