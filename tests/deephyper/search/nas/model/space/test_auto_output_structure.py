import pytest


@pytest.mark.incremental
class TestAutoOutputStructure:
    def test_import(self):
        from deephyper.search.nas.model.space.struct import AutoOutputStructure

    def test_create(self):
        from deephyper.search.nas.model.space.struct import AutoOutputStructure
        struct = AutoOutputStructure((5, ), (1, ))

    def test_create_one_vnode(self):
        from deephyper.search.nas.model.space.struct import AutoOutputStructure
        struct = AutoOutputStructure((5, ), (1, ))

        from deephyper.search.nas.model.space.node import VariableNode
        vnode = VariableNode()

        struct.connect(struct.input_nodes[0], vnode)

        from deephyper.search.nas.model.space.op.op1d import Dense
        vnode.add_op(Dense(10))

        struct.set_ops([0])

        falias = 'test_auto_output_structure'
        struct.draw_graphviz(f'{falias}.dot')

        model = struct.create_model()
        from tensorflow.keras.utils import plot_model

        plot_model(model, to_file=f'{falias}.png', show_shapes=True)

    def test_create_more_nodes(self):
        from deephyper.search.nas.model.space.struct import AutoOutputStructure
        from deephyper.search.nas.model.space.node import VariableNode
        from deephyper.search.nas.model.space.op.op1d import Dense
        struct = AutoOutputStructure((5, ), (1, ))

        vnode1 = VariableNode()
        struct.connect(struct.input_nodes[0], vnode1)

        vnode1.add_op(Dense(10))

        vnode2 = VariableNode()
        vnode2.add_op(Dense(10))

        struct.connect(vnode1, vnode2)

        struct.set_ops([0, 0])

        falias = 'test_auto_output_structure'
        struct.draw_graphviz(f'{falias}.dot')

        model = struct.create_model()
        from tensorflow.keras.utils import plot_model

        plot_model(model, to_file=f'{falias}.png', show_shapes=True)

    def test_create_multiple_inputs(self):
        from deephyper.search.nas.model.space.struct import AutoOutputStructure
        from deephyper.search.nas.model.space.node import VariableNode
        from deephyper.search.nas.model.space.op.op1d import Dense
        struct = AutoOutputStructure([(5, ), (5, )], (1, ))

        struct.set_ops([])

        falias = 'test_auto_output_structure'
        struct.draw_graphviz(f'{falias}.dot')

        model = struct.create_model()
        from tensorflow.keras.utils import plot_model

        plot_model(model, to_file=f'{falias}.png', show_shapes=True)
