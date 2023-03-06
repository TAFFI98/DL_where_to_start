# IMPORTS
import torch
import networkx as nx
import matplotlib.pyplot as plt
from model import GCN, GNN
from torch_geometric.datasets import KarateClub,TUDataset
from torch_geometric.utils import to_networkx
from torch_geometric.data import DataLoader
# This tutorial will introduce you to some fundamental concepts regarding deep learning on graphs via Graph Neural Networks based on the Pytorch Geometric library

#  Let's look at a simple graph-structured example
#  Dataset download: Zachary's karate club network.
#  This graph describes a social network of 34 members of a karate club and documents links between members who interacted outside the club.

dataset = KarateClub()
print(f'Dataset: {dataset}:')
print('======================')
print(f'Number of graphs: {len(dataset)}')
print(f'Number of features: {dataset.num_features}')
print(f'Number of classes: {dataset.num_classes}')

data = dataset[0]  # Get the first graph object.
print(data)
print('==============================================================')

# Gather some statistics about the graph.
print(f'Number of nodes: {data.num_nodes}')
print(f'Number of edges: {data.num_edges}')
print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}')
print(f'Number of training nodes: {data.train_mask.sum()}')
print(f'Training node label rate: {int(data.train_mask.sum()) / data.num_nodes:.2f}')
print(f'Has isolated nodes: {data.has_isolated_nodes()}')
print(f'Has self-loops: {data.has_self_loops()}')
print(f'Is undirected: {data.is_undirected()}')

# By printing edge_index we can further understand how PyG represents graph connectivity internally.
# For each edge, edge_index, holds a tuple of two node indices, where the first value describes the node index of the source node
# and the second value describes the node index of the destination node of an edge.
edge_index = data.edge_index
# This representation is known as the COO format (coordinate format)
print(edge_index.t())

#We can further visualize the graph by converting it to the networx library framework
G = to_networkx(data)
nx.draw_networkx(G)
plt.show()

#################################################################################################################################################
# Let's now have a closer look at how to apply Graph Neural Networks (GNNs) to the task of graph classification.
# Graph classification refers to the problem of classifiying entire graphs (in contrast to nodes), given a dataset of graphs, based on
# some structural graph properties.
# Let's download the MUTAG dataset
dataset = TUDataset(root='data/TUDataset', name='MUTAG')

print()
print(f'Dataset: {dataset}:')
# This dataset provides 188 different graphs, and the task is to classify each graph into one out of two classes.
print('====================')
print(f'Number of graphs: {len(dataset)}')
print(f'Number of features: {dataset.num_features}')
print(f'Number of classes: {dataset.num_classes}')

data = dataset[0]  # Get the first graph object.

print()
print(data)
print('=============================================================')

# Gather some statistics about the first graph.
print(f'Number of nodes: {data.num_nodes}')
print(f'Number of edges: {data.num_edges}')
print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}')
print(f'Has isolated nodes: {data.has_isolated_nodes()}')
print(f'Has self-loops: {data.has_self_loops()}')
print(f'Is undirected: {data.is_undirected()}')

# We can shuffle the dataset and use the first 150 graphs as training graphs, while using the remaining ones for testing:
torch.manual_seed(12345)
dataset = dataset.shuffle()
train_dataset = dataset[:150]
test_dataset = dataset[150:]
print(f'Number of training graphs: {len(train_dataset)}')
print(f'Number of test graphs: {len(test_dataset)}')

#  PyTorch Geometric opts an approach equivalent to data batching to achieve parallelization across a number of examples.
#  Here, adjacency matrices are stacked in a diagonal fashion (creating a giant graph that holds multiple isolated subgraphs),
#  and node and target features are simply concatenated in the node dimension: PyTorch Geometric automatically takes care of batching
#  multiple graphs into a single giant graph
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

for step, data in enumerate(train_loader):
    print(f'Step {step + 1}:')
    print('=======')
    print(f'Number of graphs in the current batch: {data.num_graphs}')
    print(data)
    print()

#  Let's train a GCN model with GCNconv layers

model = GCN(dataset,hidden_channels=64)
print(model)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()

def train():
    model.train()

    for data in train_loader:  # Iterate in batches over the training dataset.
         out = model(data.x, data.edge_index, data.batch)  # Perform a single forward pass.
         loss = criterion(out, data.y)  # Compute the loss.
         loss.backward()  # Derive gradients.
         optimizer.step()  # Update parameters based on gradients.
         optimizer.zero_grad()  # Clear gradients.

def test(loader):
     model.eval()

     correct = 0
     for data in loader:  # Iterate in batches over the training/test dataset.
         out = model(data.x, data.edge_index, data.batch)
         pred = out.argmax(dim=1)  # Use the class with highest probability.
         correct += int((pred == data.y).sum())  # Check against ground-truth labels.
     return correct / len(loader.dataset)  # Derive ratio of correct predictions.

'''
for epoch in range(1, 171):
    train()
    train_acc = test(train_loader)
    test_acc = test(test_loader)
    print(f'Epoch: {epoch:03d}, Train Acc: {train_acc:.4f}, Test Acc: {test_acc:.4f}')

# This model reaches around 76% test accuracy.

#   Let's train a GNN model with GraphConv layers
'''
model = GNN(dataset,hidden_channels=64)
print(model)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(1, 201):
    train()
    train_acc = test(train_loader)
    test_acc = test(test_loader)
    print(f'Epoch: {epoch:03d}, Train Acc: {train_acc:.4f}, Test Acc: {test_acc:.4f}')

# This model reaches around 81% test accuracy.



