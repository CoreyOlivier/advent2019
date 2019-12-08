class Layer:
    def __init__(self, layer_data):
        self.data = layer_data
        self.counts = {}
    
    def calc_counts(self,n_counts):
        for i in range(n_counts):
            count = 0
            for j in self.data:
                if int(j) == int(i):
                    count += 1
            self.counts[str(i)] = count

    def get_count(self, n):
        return self.counts[n]

    def multiply_counts(self, count1, count2):
        return self.counts[count1] * self.counts[count2]
    
    def display(self, width, height):
        white  = '\u2588'
        black  = ' '
        row_strings = []
        for row in range(height):
            row_list = self.data[row*width:(row+1)*width]
            row_string = ''.join(str(x) for x in row_list)
            row_strings.append(row_string)
        raw_display_string = '\n'.join(row_strings)
        black_dislpaly = raw_display_string.replace('0', black)
        full_display = black_dislpaly.replace('1', white)
        return full_display

    

def create_layers(data, width, height):
    layer_area = width * height
    layers = []
    data = list(data)
    while len(data) > 0:
        layers.append(Layer(data[:layer_area]))
        del(data[:layer_area])
    return layers

class Composite_Layer(Layer):
    def __init__(self, layers):
        composite_data = []
        for i in range(len(layers[0].data)):
            for layer in layers:
                if i < len(composite_data):
                    pass
                else:
                    print('layer #{}'.format(layers.index(layer)))
                    print(layer.data)
                    if int(layer.data[i]) == int(0):
                        print(0)
                        composite_data.append(int(layer.data[i]))
                    elif int(layer.data[i]) == int(1):
                        print(1)
                        composite_data.append(int(layer.data[i]))
                    else:
                        pass
        super().__init__(composite_data)
            


def parse_file():
    with open('input.txt') as f:
        file = f.readlines()[0].rstrip()
    return file
        

def fewest_0s(layers):
    selected_layer = None
    for layer in layers:
        if selected_layer is None:
            selected_layer = layer
        else:
            if layer.get_count('0') < selected_layer.get_count('0'):
                selected_layer = layer
    return selected_layer

def part1():
    data = parse_file()
    layers = create_layers(data, 25, 6)
    for layer in layers:
        layer.calc_counts(3)
    fewest_0_layer = fewest_0s(layers)
    return fewest_0_layer.multiply_counts('1','2')


def part2(data, width, height):
    layers = create_layers(data,  width, height)
    composite = Composite_Layer(layers)
    image = composite.display(width, height)
    return layers, composite, image

sample1 = '0222112222120000'

if __name__ == '__main__':
    #p2_layers, p2_composite, p2_image = part2(parse_file(), 25, 6)
    s_layer, s_composite, s_image = part2(sample1, 2, 2)



    
