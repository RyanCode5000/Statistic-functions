def vector_multiplier(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        raise ValueError('Vectors must be equal length.')
    dot_product = sum(num_1 * num_2 for num_1, num_2 in zip(vector_1, vector_2))
    return dot_product
