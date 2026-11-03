import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from app.ml.model import AnomalyDetector
from app.config import settings


def synthetic_dataset(n=1000):
    # features: [amount, from_entropy, to_entropy]
    normal = np.random.normal(loc=[1.0, 3.0, 3.0], scale=[1.0, 1.0, 1.0], size=(n,3))
    anomalous = np.random.normal(loc=[10.0, 8.0, 8.0], scale=[5.0, 1.0, 1.0], size=(int(n*0.1),3))
    X = np.vstack([normal, anomalous]).astype(np.float32)
    y = np.concatenate([np.zeros(len(normal)), np.ones(len(anomalous))]).astype(np.float32)
    # shuffle
    idx = np.random.permutation(len(X))
    return X[idx], y[idx]


def train(epochs=10, lr=1e-3):
    X, y = synthetic_dataset(2000)
    X = torch.from_numpy(X)
    y = torch.from_numpy(y)
    model = AnomalyDetector(input_dim=X.shape[1])
    opt = optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.BCELoss()
    for epoch in range(epochs):
        model.train()
        opt.zero_grad()
        out = model(X)
        loss = loss_fn(out, y)
        loss.backward()
        opt.step()
        if (epoch+1) % max(1, epochs//5) == 0:
            print(f"Epoch {epoch+1}/{epochs} loss={loss.item():.4f}")
    torch.save(model.state_dict(), settings.model_path)
    print("Model saved to", settings.model_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    train(epochs=args.epochs)
