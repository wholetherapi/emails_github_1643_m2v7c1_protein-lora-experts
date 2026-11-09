import torch.nn as nn


class LoRAExpert(nn.Module):
    """Single low-rank expert applied to a frozen projection."""

    def __init__(self, dim, rank=8):
        super().__init__()
        self.down = nn.Linear(dim, rank, bias=False)
        self.up = nn.Linear(rank, dim, bias=False)

    def forward(self, hidden):
        return hidden + self.up(self.down(hidden))
