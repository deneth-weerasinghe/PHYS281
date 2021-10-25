def Sequence(n=2, initialSequence=[0, 1]):
    """
    Create a Fibonacci-style sequence up to the nth entry, based on an initial
    two-value sequeunce, where

    x_n = x_{n-1} + x_{n-2}

    Parameter
    ---------
    n: int
        The entry up to which to generate the sequence (n > 0, i.e., n=1 is the
        first entry, etc). Defaults to 2, the length of the initial sequence.
    initialSequence: list
        A list containing the first two values of the sequence, defaulting to
        [0, 1].

    Returns
    -------
    sequence: list
        A list containing the full sequence.
    """

    if not len(initialSequence) > 1:
        raise ValueError("list needs to be at least two elements long to form a sequence")

    if n < 2:
        raise ValueError("n must be the same or larger than the length of the initial sequence")

    # copy and store the initialSequence
    sequence = list(initialSequence)

    # extend and fill in the sequence...
    for i in range(len(initialSequence), n):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


n=100
seq = Sequence(n=n)
print(seq)
