import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Diferenciador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.prev_sample = 0.0

    def work(self, input_items, output_items):
        in_vec = input_items[0]
        out_vec = output_items[0]
        
        for i in range(len(in_vec)):
            out_vec[i] = in_vec[i] - self.prev_sample
            self.prev_sample = in_vec[i]
            
        return len(output_items[0])