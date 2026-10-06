# Optimizers: SGD vs Adam — Complete Notes

## 1. What is an Optimizer?

An optimizer is an algorithm used to update the trainable parameters (weights and biases) of a neural network so that the model minimizes its loss function.

Training flow:

```text
Input → Neural Network → Prediction → Loss
      → Backpropagation → Gradients → Optimizer
      → Updated Weights → Repeat
```

### Important distinction

- **Backpropagation** calculates gradients.
- **Optimizer** uses those gradients to update model parameters.

---

## 2. Gradient Descent

The basic gradient descent update rule is:

$$
\theta_{t+1} = \theta_t - \eta \nabla_\theta L(\theta_t)
$$

Where:

- `θ` = model parameter
- `L` = loss function
- `∇L` = gradient
- `η` = learning rate

Example:

```text
Current weight = 5.0
Gradient       = 2.0
Learning rate  = 0.1

new_weight = 5.0 - (0.1 × 2.0)
           = 4.8
```

---

## 3. Learning Rate

The learning rate controls how large each parameter update is.

### Small learning rate

```text
0.0001
```

Advantages:
- Gradual updates
- Can be stable

Disadvantages:
- Training can be very slow

### Large learning rate

```text
0.1
```

Advantages:
- Can converge quickly if appropriate

Disadvantages:
- Can overshoot the minimum
- May cause unstable training

There is no universally correct learning rate.

---

# 4. SGD

**SGD = Stochastic Gradient Descent**

In deep learning, SGD normally means gradient updates calculated using mini-batches rather than the complete dataset.

For a mini-batch:

$$
\theta_{t+1} = \theta_t - \eta g_t
$$

Example:

```text
Dataset = 60,000 images
Batch size = 64

Batch 1 → gradient → update
Batch 2 → gradient → update
Batch 3 → gradient → update
...
```

This makes neural-network training practical.

---

## 5. SGD in PyTorch

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)
```

### `model.parameters()`

Returns the trainable parameters that the optimizer should update.

### `lr`

Learning rate.

---

# 6. SGD with Momentum

Basic SGD uses the current gradient. Momentum also uses information from previous gradients.

A simplified form is:

$$
v_t = \beta v_{t-1} + g_t
$$

$$
\theta_t = \theta_{t-1} - \eta v_t
$$

Momentum can reduce oscillations and accelerate movement in consistent directions.

PyTorch:

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9
)
```

---

# 7. Adam

**Adam = Adaptive Moment Estimation**

Adam combines momentum-like gradient tracking with adaptive parameter updates.

It maintains:

1. First moment — moving average of gradients
2. Second moment — moving average of squared gradients

First moment:

$$
m_t = \beta_1m_{t-1} + (1-\beta_1)g_t
$$

Second moment:

$$
v_t = \beta_2v_{t-1} + (1-\beta_2)g_t^2
$$

Bias correction:

$$
\hat m_t = \frac{m_t}{1-\beta_1^t}
$$

$$
\hat v_t = \frac{v_t}{1-\beta_2^t}
$$

Update:

$$
\theta_t =
\theta_{t-1}
-
\alpha
\frac{\hat m_t}
{\sqrt{\hat v_t}+\epsilon}
$$

You normally do not calculate these manually in PyTorch.

---

# 8. Adam in PyTorch

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

Common Adam defaults:

```text
learning rate = 0.001
β1 = 0.9
β2 = 0.999
epsilon = 1e-8
```

These are defaults, not mandatory values.

---

# 9. Core Difference: SGD vs Adam

### SGD

```text
Gradient
   ↓
Learning Rate
   ↓
Weight Update
```

### Adam

```text
Gradient
   ↓
Moving Average of Gradient
   +
Moving Average of Squared Gradient
   ↓
Adaptive Update
   ↓
Weight Update
```

SGD has a simpler update rule. Adam maintains additional optimizer state and adapts updates using gradient history.

---

# 10. Detailed Comparison

| Feature | SGD | Adam |
|---|---|---|
| Full name | Stochastic Gradient Descent | Adaptive Moment Estimation |
| Basic idea | Gradient-based update | Adaptive gradient-based update |
| Momentum | Optional | Built into the algorithm |
| Adaptive learning rate | No | Yes |
| Gradient history | With momentum, partially | First and second moments |
| Memory usage | Low | Higher |
| Implementation | Simple | More complex |
| Common starting LR | 0.01 | 0.001 |
| Initial convergence | Can be slower | Often faster |
| Hyperparameter sensitivity | Can require more tuning | Often easier to start |
| Generalization | Can work very well | Can work very well |
| Best use | Controlled training / strong baseline | Fast baseline / many deep-learning tasks |

---

# 11. Why Adam Often Converges Faster

Suppose:

```text
Parameter A → large gradients
Parameter B → small gradients
```

SGD uses one global learning rate.

Adam uses gradient statistics to adapt the effective update for different parameters.

Therefore, Adam often reaches a useful solution faster during early training.

However:

> Faster convergence does not automatically mean better final generalization.

---

# 12. Memory Usage

Plain SGD stores relatively little optimizer state:

```text
Parameters
Gradients
```

SGD with momentum adds momentum state:

```text
Parameters
Gradients
Momentum
```

Adam keeps two additional states:

```text
Parameters
Gradients
First moment
Second moment
```

Therefore Adam generally uses more optimizer memory than plain SGD.

---

# 13. Training Stability

SGD can be sensitive to learning rate.

```text
Learning rate too large
        ↓
Large updates
        ↓
Loss oscillates
        ↓
Training becomes unstable
```

Adam adapts updates using gradient statistics, which often makes it easier to get a model training with reasonable starting settings.

Adam can still become unstable if the learning rate is inappropriate.

---

# 14. SGD Training Loop

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

for images, labels in train_loader:

    optimizer.zero_grad()

    outputs = model(images)

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()
```

---

# 15. Adam Training Loop

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

for images, labels in train_loader:

    optimizer.zero_grad()

    outputs = model(images)

    loss = criterion(outputs, labels)

    loss.backward()

    optimizer.step()
```

The training loop is almost identical. The main change is the optimizer.

---

# 16. `zero_grad()`, `backward()`, and `step()`

## `optimizer.zero_grad()`

Clears gradients from the previous iteration.

```python
optimizer.zero_grad()
```

PyTorch accumulates gradients by default.

## `loss.backward()`

Calculates gradients through backpropagation.

```python
loss.backward()
```

## `optimizer.step()`

Updates model parameters.

```python
optimizer.step()
```

Remember:

```text
zero_grad()
    ↓
backward()
    ↓
step()
```

---

# 17. Complete MNIST Example — SGD

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

transform = transforms.ToTensor()

train_dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)


class NeuralNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.network(x)


model = NeuralNetwork().to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9
)

epochs = 5

for epoch in range(epochs):

    total_loss = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)

    print(
        f"Epoch [{epoch + 1}/{epochs}] "
        f"Loss: {avg_loss:.4f}"
    )
```

---

# 18. Complete MNIST Example — Adam

Use the same model and dataset, but change the optimizer:

```python
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)
```

The remaining training loop stays the same.

---

# 19. Fair SGD vs Adam Experiment

Keep these identical:

```text
Dataset
Model architecture
Batch size
Number of epochs
Loss function
Train/validation split
Preprocessing
Random seed
```

Change only:

```text
Optimizer
Learning rate
```

Example:

```text
Experiment A
Optimizer = SGD
Learning rate = 0.01
Momentum = 0.9

Experiment B
Optimizer = Adam
Learning rate = 0.001
```

Record:

```text
Training loss
Validation loss
Training accuracy
Validation accuracy
Training time
```

---

# 20. What to Plot

### Loss curve

```text
X-axis → Epoch
Y-axis → Loss

Compare:
SGD Loss
Adam Loss
```

### Accuracy curve

```text
X-axis → Epoch
Y-axis → Accuracy

Compare:
SGD Accuracy
Adam Accuracy
```

### Training time

Record total training time for each optimizer.

Use your actual results rather than assuming Adam or SGD will always win.

---

# 21. Advantages of SGD

### Advantages

- Simple
- Low memory usage
- Easy to understand
- Can achieve strong generalization
- Works well with learning-rate schedules
- Gives fine control over optimization

### Disadvantages

- Can require more tuning
- Sensitive to learning rate
- Can converge slowly
- Can oscillate without momentum

---

# 22. Advantages of Adam

### Advantages

- Usually easy to get started with
- Often converges quickly
- Adaptive parameter updates
- Handles different gradient scales well
- Often needs less initial tuning

### Disadvantages

- Uses more memory
- More complex internally
- Can generalize differently from SGD
- Still requires learning-rate tuning
- Faster convergence does not guarantee better final performance

---

# 23. When to Use SGD

SGD can be a good choice when:

- Memory usage is important
- You want a simple optimizer
- You want strong control over optimization
- You are doing controlled experiments
- You want to study generalization
- You have time for tuning

Example:

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9
)
```

---

# 24. When to Use Adam

Adam can be a good choice when:

- You want a strong baseline quickly
- You are developing a new neural network
- You want relatively fast initial convergence
- Gradients have different scales
- You are experimenting with architectures

Example:

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

---

# 25. Simple Analogy

Imagine walking down a mountain to find the lowest point.

### SGD

You look at the current slope and decide:

```text
Direction?
Step size?
```

You use one general learning rate.

### Adam

Adam keeps track of previous gradient behavior and adapts the update.

```text
SGD
→ Simple and controlled

Adam
→ Adaptive and often easier to start with
```

---

# 26. Adam Hyperparameters

Example:

```python
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001,
    betas=(0.9, 0.999),
    eps=1e-8,
    weight_decay=0
)
```

### `lr`

Learning rate.

### `betas`

Controls the exponential moving averages.

Default:

```python
betas=(0.9, 0.999)
```

### `eps`

Small value used for numerical stability.

### `weight_decay`

Regularization-related parameter.

---

# 27. SGD Hyperparameters

Example:

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9,
    weight_decay=0
)
```

Important parameters:

- `lr` → learning rate
- `momentum` → momentum factor
- `weight_decay` → regularization
- `nesterov` → enables Nesterov momentum

Example:

```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9,
    nesterov=True
)
```

---

# 28. Optimizer vs Loss Function

These are different.

### Loss function

Measures how wrong the prediction is.

Examples:

```python
nn.CrossEntropyLoss()
nn.MSELoss()
nn.BCELoss()
```

### Optimizer

Uses gradients to update the model.

Examples:

```python
torch.optim.SGD()
torch.optim.Adam()
```

Workflow:

```text
Prediction
    ↓
Loss Function
    ↓
Loss
    ↓
Backpropagation
    ↓
Gradients
    ↓
Optimizer
    ↓
Updated Weights
```

---

# 29. Optimizer vs Learning Rate

The learning rate is a hyperparameter of the optimizer.

```python
torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
```

Here:

```text
Adam  → Optimizer
0.001 → Learning rate
```

---

# 30. Other Optimizers to Know

| Optimizer | Main idea |
|---|---|
| SGD | Basic gradient-based optimization |
| SGD + Momentum | Uses previous gradient direction |
| AdaGrad | Adapts learning rate using accumulated squared gradients |
| RMSprop | Uses moving average of squared gradients |
| Adam | Adaptive optimizer using first and second moments |
| AdamW | Adam with decoupled weight decay |

Useful learning sequence:

```text
SGD
 ↓
SGD + Momentum
 ↓
Adam
 ↓
AdamW
```

---

# 31. Adam vs AdamW

AdamW is very important in modern deep learning, especially Transformer training.

```python
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=0.001,
    weight_decay=0.01
)
```

AdamW decouples weight decay from the adaptive gradient update.

---

# 32. Common Mistakes

### Mistake 1 — Forgetting `zero_grad()`

Incorrect:

```python
loss.backward()
optimizer.step()
```

Use:

```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

### Mistake 2 — Learning rate too high

```python
lr=10
```

May cause unstable training.

### Mistake 3 — Learning rate too low

```python
lr=0.00000001
```

May make training extremely slow.

### Mistake 4 — Unfair optimizer comparison

Do not change the model, dataset, batch size, or preprocessing when comparing optimizers.

### Mistake 5 — Assuming Adam is always better

Adam is often a strong starting point, but no optimizer is universally best.

---

# 33. Quick Revision

```text
Optimizer
    ↓
Updates model parameters

SGD
    ↓
Simple gradient-based update
    ↓
Low memory

SGD + Momentum
    ↓
SGD + previous gradient information

Adam
    ↓
First moment + second moment
    ↓
Adaptive updates
    ↓
Often faster initial convergence
```

### Important formulas

SGD:

$$
\theta_{t+1}=\theta_t-\eta g_t
$$

Adam:

$$
\theta_t =
\theta_{t-1}
-
\alpha
\frac{\hat m_t}
{\sqrt{\hat v_t}+\epsilon}
$$

### Important PyTorch code

```python
# SGD
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01,
    momentum=0.9
)

# Adam
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

# Training
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

---
