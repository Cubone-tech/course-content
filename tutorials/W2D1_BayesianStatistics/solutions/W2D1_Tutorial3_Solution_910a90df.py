def my_marginalization(input_array, binary_decision_array):

    marginalization_array = input_array * binary_decision_array
    marginal = np.sum(marginalization_array, axis=0)
    marginal /= marginal.sum()

    return marginalization_array, marginal

marginalization_array, marginal = my_marginalization(input_array, binary_decision_array)
with plt.xkcd():
  plot_myarray(marginalization_array, '$x$', '$\^x$', 'Marginalization array: $p(\^x | x)$')
  plt.figure()
  plt.plot(x, marginal)
  plt.xlabel('$\^x$')
  plt.ylabel('probability')
  plt.show()