# Write your solution here
import string

alphabet = list(string.ascii_uppercase)

n_layers = int(input("Layers: "))

filtered_alphabet = alphabet[:n_layers]

layer_size = (n_layers * 2 - 1)

base_layer = list(filtered_alphabet[-1] * layer_size)

print("".join(base_layer))

layers = ["".join(base_layer)]

for idx, letter in enumerate(filtered_alphabet[n_layers - 2::-1]):
    middle = letter * (layer_size - (idx+1) * 2)
    base_layer[idx+1:layer_size-idx-1] = middle
    layers.append("".join(base_layer))
    print("".join(base_layer))

for layer in layers[n_layers - 2::-1]:
    print(layer)
