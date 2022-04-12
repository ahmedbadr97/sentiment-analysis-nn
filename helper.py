def load_data():
    """
    load dataset from reviews and labels text files
    :return (list of reviews , list of reviews labels):
    """
    with open('dataset/reviews.txt') as reviews_file:
        reviews = list(map(lambda line: line[:-1], reviews_file.readlines()))
    if reviews is None:
        raise FileNotFoundError("there is a problem reading reviews file")
    with open('dataset/labels.txt') as labels_file:
        labels = list(map(lambda line: line[:-1], labels_file.readlines()))
    if labels is None:
        raise FileNotFoundError("there is a problem reading labels file")
    return reviews, labels
