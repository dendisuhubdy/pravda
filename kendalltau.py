import scipy.stats as stats


def kendalltau(input1, input2):
    """
    W.R. Knight, “A Computer Method for Calculating Kendall’s Tau with Ungrouped Data”,
    Journal of the American Statistical Association, Vol. 61, No. 314, Part 1, pp. 436-439, 1966.
    """
    tau, p_value = stats.kendalltau(input1, input2)
    return tau, p_value
