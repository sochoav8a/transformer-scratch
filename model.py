import torch 
import torch.nn as nn
import math

class InputEmbeddings(nn.Module):\
    def __init_(self, d_model: int, vocab_size: int)
        super().__init_()
        self.d_model = d_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size, d_model)
    
    def forward(self, x):
        return self.embedding(x) * math(self.d_model)


class PositionalEncoding(nn.Module):    

    def __init__(self, d_model: int, seq_len: int, dropout= float):
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        self.dropout = nn.Dropout(dropout)
        
        #create a matrix of shape (seq_len, d_model)
        pe = torch.zeros(seq_len, d_model)
        
        ###remeber the formula (sin or cos) pos/ 10000**2i/d_model
        #create a vector of shape (seq_len)
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        #apply sin to the even positions
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)

        self.register_buffer("pe", pe)

    def forward(self, x):
        x = x + (self.pe[:, :x.shape[1], :]).requieres_grad_(False)
        return self.dropout(x)

class LayerNormalization(nn.Module):

    def __init_(self, eps: float = 10e-6):
        super().__init__()
        self.eps = eps
        self.alpha = nn.Parameter(torch.ones(1)) #multiplied
        self.bias = nn.Parameter(torch.ones(1)) #add

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        std = x.std(dim=-1, keepdim=True)
        return self.alpha * (x - mean) / (std + self.eps) + self.bias
        