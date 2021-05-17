import pickle


def save_to_pickle(var, filename, path_write_data):
    """
    Parameters
    ----------
    var : any python variable
        variable to be saved
    filename : string
        Name of the pickle we will create
    path_write_data : string
        Path to the folder where we write and keep intermediate results
    """

    with open(path_write_data + filename + '.pickle', 'wb') as f:
        pickle.dump(var, f)
    f.close()


def load_pickle(path_data):
    """
    Parameters:
    ----------
    path_data : string
        Path to the file to be loaded
    Returns
    ----------
    var :
        The loaded object
    """
    with open(path_data, 'rb') as f:
        var = pickle.load(f)
    f.close()

    return var