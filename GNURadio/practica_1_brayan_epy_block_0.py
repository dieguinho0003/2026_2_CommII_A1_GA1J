import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Acumulador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.acc = 0.0

    def work(self, input_items, output_items):
        in_vec = input_items[0]
        out_vec = output_items[0]
        
        for i in range(len(in_vec)):
            self.acc += in_vec[i]
            out_vec[i] = self.acc
            
        return len(output_items[0])