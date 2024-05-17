import torch
import graphviz
from model import ContextAwareModel
from torchviz import make_dot

model = ContextAwareModel()

model.eval()

print(model)

x = torch.randn(128, 1, 240, 512)
y = model(x)

make_dot(y, params=dict(list(model.named_parameters()))).render("cnn", format="png")