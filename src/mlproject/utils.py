def save_object(obj, filename):
	"""Save an object to a file using pickle."""
	import pickle
	with open(filename, 'wb') as file:
		pickle.dump(obj, file)
