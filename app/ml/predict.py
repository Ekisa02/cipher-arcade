import torch
import numpy as np
from app.ml.model import AnomalyDetector
from app.config import settings

_model = None


def _load_model():
    global _model
    if _model is None:
        model = AnomalyDetector(input_dim=3)
        try:
            model.load_state_dict(torch.load(settings.model_path, map_location='cpu'))
        except Exception:
            # If model not present, keep randomly initialized model
            pass
        model.eval()
        _model = model
    return _model


def predict_tx_anomaly(features: dict) -> float:
    """features: {amount: float, from_entropy: float, to_entropy: float}
    Returns anomaly score between 0..1
    """
    arr = np.array([features.get('amount', 0.0), features.get('from_entropy', 0.0), features.get('to_entropy', 0.0)], dtype=np.float32)
    model = _load_model()
    with torch.no_grad():
        x = torch.from_numpy(arr).unsqueeze(0)
        score = model(x).item()
    return float(score)
