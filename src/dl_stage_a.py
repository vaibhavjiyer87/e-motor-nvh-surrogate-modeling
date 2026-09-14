import torch
import torch.nn as nn


class StageAMLP(nn.Module):

    def __init__(
        self,
        input_dim=14,
        hidden_dims=(64, 32, 16),
        dropout=0.10,
        num_classes=2,
    ):
        super().__init__()

        layers = []
        previous = input_dim

        for hidden in hidden_dims:
            layers.extend([
                nn.Linear(previous, hidden),
                nn.LayerNorm(hidden),
                nn.ReLU(),
                nn.Dropout(dropout),
            ])
            previous = hidden

        layers.append(
            nn.Linear(
                previous,
                num_classes
            )
        )

        self.network = nn.Sequential(
            *layers
        )

    def forward(self, x):
        return self.network(x)


def count_trainable_parameters(model):
    return sum(
        p.numel()
        for p in model.parameters()
        if p.requires_grad
    )
