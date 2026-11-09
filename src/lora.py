import torch
import torch.nn as nn


class ExpertRouter(nn.Module):
    def __init__(self, dim, num_experts=4):
        super().__init__()
        self.gate = nn.Linear(dim, num_experts)

    def forward(self, hidden):
        weights = torch.softmax(self.gate(hidden.mean(dim=1)), dim=-1)
        return weights
