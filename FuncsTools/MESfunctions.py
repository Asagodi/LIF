import numpy
import itertools

def close_neighbours(neuron, weight_matrix, min_weight):
    """
    Returns a list of neighbours that have a connection strength above min_weight.
    """
    neighs = weight_matrix[neuron] #select connections to neighbours
    cn = [neighs > min_weight] #select close neighbours
#    cn = [abs(neighs) > min_weight] #select close neighbours
    close_neuron_numbers = numpy.squeeze(numpy.arange(0, weight_matrix.shape[1]))[cn]
    return close_neuron_numbers

def colimit_of_pattern(pattern, weight_mat, input_strength = 1, activation = None):
    inp = numpy.zeros(weight_mat.shape[0])
    inp[pattern] = 1
    if activation:
        outp = inp.dot(weight_mat) > activation
    else: outp = inp.dot(weight_mat)
    return outp

def find_pattern_by_weight(neuron, weight_matrix, min_weight, max_length):
    """
    Returns a list of all patterns that have a connection neurons with connection 
    strength above min_weight and are of maximal size max_length.
    """
    current_neuron = neuron
    list_of_paths = [[neuron]] #paths are lists
    dict_of_paths = {}
    i = 1
    while i < max_length:
        eep = []
        for path in list_of_paths:
#             print("Path", path)
            current_neuron = path[-1]
#             print("Current", current_neuron)
            next_neurons = close_neighbours(current_neuron, weight_matrix, min_weight) #select close neighbours
#             print("Next", next_neurons)
            #add next neuron in path
            extended_paths = []
            for nn in next_neurons:
                if nn not in path:
                    extended_paths.append(path + [nn])
            eep.extend(extended_paths)
#             print("EEP", eep)
        if eep == []:
            break
        list_of_paths = eep
        i += 1
        dict_of_paths[i] = eep
    sorted_list_of_paths = [list(numpy.sort(p)) for p in list_of_paths]
    sorted_list_of_paths.sort()
    list_of_paths_nodups = list(sorted_list_of_paths for sorted_list_of_paths,
                                        _ in itertools.groupby(sorted_list_of_paths))
    return list_of_paths, list_of_paths_nodups, dict_of_paths

def find_pattern_by_synchrony(inputs, weight_matrix):
	#Implement from jupyter
	outp = inputs.dot(weight_matrix)
	syncplot = outp.mean(axis=1)
	syncplot = syncplot.reshape(weight_matrix[1],weight_matrix[1])
	return syncplot
