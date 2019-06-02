import os
import turtle

freq_dic = {'\0': 0}
code_dic = {}
keys = []


class Node(object):
    def __init__(self, left=None, right=None) -> None:
        if left and right:
            self.freq = left.freq + right.freq
        else:
            self.freq = 0
        self.left = left
        self.right = right
        self.parent = None

    def __lt__(self, other) -> bool:
        return self.freq < other.freq


class Leaf(Node):
    def __init__(self, char: chr) -> None:
        super().__init__()
        self.freq = freq_dic[char]
        self.char = char
        self.code = ''


def make_tree(lst_nodes: list) -> Node:
    if len(lst_nodes) == 2:
        return lst_nodes[1]  # root

    left = lst_nodes[1]
    remove_min_heap(lst_nodes)
    right = lst_nodes[1]
    remove_min_heap(lst_nodes)
    node = Node(left, right)
    left.parent = node
    right.parent = node
    add_min_heap(lst_nodes, node)
    return make_tree(lst_nodes)


def coding(root: Node, code: str = '') -> None:
    if root.left and root.right:
        coding(root.left, code + '0')
        coding(root.right, code + '1')
    else:
        root.code = code
        code_dic.update({root.char: root.code})
        char = root.char
        if char == '\n':
            char = '\\n'
        elif char == '\t':
            char = '\\t'
        elif char == '\r':
            char = '\\r'
        key = '%s\t%d\t%s' % (char, len(root.code), root.code)
        keys.append(key)


def min_heapify(heap_array: list, index: int) -> None:
    if index > 1 and heap_array[index] < heap_array[index // 2]:
        heap_array[index], heap_array[index // 2] = heap_array[index // 2], heap_array[index]
        min_heapify(heap_array, index // 2)


def max_heapify(heap_array: list, index: int) -> None:
    if index * 2 > len(heap_array) - 1:
        return

    elif index * 2 == len(heap_array) - 1:
        if heap_array[index] > heap_array[index * 2]:
            heap_array[index], heap_array[index * 2] = heap_array[index * 2], heap_array[index]
            max_heapify(heap_array, index * 2)
        return

    if heap_array[index * 2] < heap_array[index * 2 + 1]:
        if heap_array[index] > heap_array[index * 2]:
            heap_array[index], heap_array[index * 2] = heap_array[index * 2], heap_array[index]
            max_heapify(heap_array, index * 2)
    else:
        if heap_array[index] > heap_array[index * 2 + 1]:
            heap_array[index], heap_array[index * 2 + 1] = heap_array[index * 2 + 1], heap_array[index]
            max_heapify(heap_array, index * 2 + 1)


def add_min_heap(heap_array: list, new_node: Node) -> None:
    heap_array.append(new_node)
    min_heapify(heap_array, len(heap_array) - 1)


def remove_min_heap(heap_array: list) -> None:
    if len(heap_array) == 2:
        heap_array.pop()
        return
    heap_array[1] = heap_array.pop()
    max_heapify(heap_array, 1)


def draw_tree(painter: turtle.Turtle, root: Node, scale: float) -> None:
    x = painter.xcor()
    y = painter.ycor()
    painter.hideturtle()
    if type(root) == Leaf:
        char = root.char
        if char == '\n':
            char = '\\n'
        if char == '\0':
            char = '\\0'
        text = "'%s',%d" % (char, root.freq)
        painter.color('yellow')
        painter.stamp()
        painter.up()
        painter.sety(y - 15)
    else:
        text = str(root.freq)
        painter.color('cyan')
        painter.stamp()
        painter.up()
        painter.sety(y - 10)

    painter.color('black')
    painter.write(text, align='center', font=('Arial', 16, 'bold'))

    if root.left is not None:
        t = turtle.Turtle(shape='circle')
        t.up()
        t.goto(x, y)
        t.down()
        t.pensize(2)
        t.color('grey')
        t.goto(x - scale, y - scale)
        draw_tree(t, root.left, scale * 0.5)
    if root.right is not None:
        t = turtle.Turtle(shape='circle')
        t.up()
        t.goto(x, y)
        t.down()
        t.pensize(2)
        t.color('grey')
        t.goto(x + scale, y - scale)
        draw_tree(t, root.right, scale * 0.5)


def main_draw_tree(root: Node, scale: float = 500) -> None:
    wn = turtle.Screen()
    wn.tracer(8)
    t = turtle.Turtle(shape='circle')
    t.up()
    t.goto(0, scale)
    t.down()
    draw_tree(t, root, scale)
    wn.exitonclick()


def main(file_address: str, dt: int) -> None:
    try:
        file_stream = open(file_address, 'r')

    except FileNotFoundError as ex:
        print('No such file or directory:', ex.filename)
        return

    file_text = file_stream.read()
    file_stream.close()
    for char in file_text:
        if char not in freq_dic:
            freq_dic.update({char: 1})
        else:
            freq_dic[char] += 1

    lst_nodes = [Leaf(x) for x in freq_dic]
    leaves = lst_nodes[:]
    heap_array = [None, lst_nodes.pop()]

    while lst_nodes:
        new_node = lst_nodes.pop()
        add_min_heap(heap_array, new_node)

    root = make_tree(heap_array)
    coding(root)
    file_stream = open('Huffman.txt', 'w')
    file_stream.write('\n'.join(keys))
    file_stream.close()

    file_text += '\0'
    bin_text = ''
    for char in file_text:
        bin_text += code_dic[char]

    zeros = 8 - len(bin_text) % 8
    bin_text += zeros * '0'
    code_text = ''
    while bin_text:
        code = bin_text[:8]
        code_text += chr(int(code, 2))
        bin_text = bin_text[8:]

    file_stream = open('Zip.txt', 'w')
    file_stream.write(code_text)
    file_stream.close()
    if dt == 2:
        main_draw_tree(root)

    print("File '%s' zipped to 'Zip.txt' successfully\n" % file_address)
    print("Original size:", os.stat(file_address).st_size, 'B')
    print("Zipped size:", os.stat('Zip.txt').st_size, 'B')


if __name__ == '__main__':
    import sys

    try:
        dt_code = int(sys.argv[2])
        input_file_address = sys.argv[1]

    except ValueError:
        dt_code = 2
        input_file_address = 'Input.txt'

    except IndexError:
        dt_code = 2
        input_file_address = 'Input.txt'

    main(input_file_address, dt_code)
