# GANs — Generative Adversarial Networks

## 1. What is a GAN?

**GAN = Generative Adversarial Network**

A GAN is a type of deep learning model used to **generate new synthetic data** that looks similar to real training data.

For example, if we train a GAN on handwritten digits:

```
Real MNIST Images
       ↓
     GAN
       ↓
New Synthetic Digits
```

The generated images are not copied directly from the dataset. The generator learns patterns from the training data and produces new samples.

GANs can be used for:

- Image generation
- Image-to-image translation
- Synthetic data generation
- Face generation
- Image enhancement
- Style transfer
- Data augmentation

---

# 2. Basic GAN Architecture

A GAN has **two neural networks**:

```
          Random Noise
               │
               ▼
        ┌─────────────┐
        │  Generator  │
        └──────┬──────┘
               │
               ▼
          Fake Image
               │
               ▼
        ┌──────────────┐
Real ──►│ Discriminator│
Image   └──────┬───────┘
               │
               ▼
        Real or Fake?
```

The two networks compete against each other.

### Generator

The **Generator (G)** creates fake data.

```
Random Noise
     ↓
Generator
     ↓
Fake Image
```

### Discriminator

The **Discriminator (D)** tries to determine whether an image is real or generated.

```
Image
 ↓
Discriminator
 ↓
Real / Fake
```

---

# 3. Generator

The Generator's job is:

> Create fake samples that look like real samples.
> 

Example:

```
Random Noise

[0.23, -0.71, 0.45, ...]

       ↓

Generator Neural Network

       ↓

Fake Image
```

Initially, the output may look like random noise.

After training:

```
Random Noise
      ↓
Generator
      ↓
Better Image
      ↓
Better Image
      ↓
Realistic Image
```

---

# 4. Discriminator

The Discriminator is essentially a classifier.

Its job:

> Determine whether an input sample is real or fake.
> 

Example:

```
Real Image
    ↓
Discriminator
    ↓
0.98 → Real
```

Another:

```
Fake Image
    ↓
Discriminator
    ↓
0.07 → Fake
```

Usually:

```
0 → Fake
1 → Real
```

---

# 5. Why "Adversarial"?

The two networks have competing goals.

### Generator

Wants:

```
Discriminator → Real
```

### Discriminator

Wants:

```
Real image → Real
Fake image → Fake
```

Therefore:

```
Generator
    ↕
Competition
    ↕
Discriminator
```

This competition gives GANs their name:

**Generative Adversarial Network**

---

# 6. GAN Training Process

The basic training process is:

```
1. Generate random noise
          ↓
2. Generator creates fake image
          ↓
3. Give real + fake images to discriminator
          ↓
4. Discriminator predicts real/fake
          ↓
5. Calculate discriminator loss
          ↓
6. Update discriminator
          ↓
7. Generate fake image again
          ↓
8. Train generator to fool discriminator
          ↓
9. Repeat
```

This happens many times.

---

# 7. GAN Training Loop

Conceptually:

```
for each epoch:

    Train Discriminator
        ↓
    Real images
        ↓
    Fake images
        ↓
    Calculate D loss
        ↓
    Update D

    Train Generator
        ↓
    Generate fake images
        ↓
    Try to fool D
        ↓
    Calculate G loss
        ↓
    Update G
```

---

# 8. Loss Functions

GANs commonly use **Binary Cross Entropy (BCE)** for the basic GAN implementation.

The discriminator has two goals.

### Real image

```
Expected = 1
```

### Fake image

```
Expected = 0
```

Example:

```python
criterion = nn.BCELoss()
```

---

# 9. Discriminator Loss

Conceptually:

```
D loss =
loss(real images)
+
loss(fake images)
```

The discriminator wants:

```
D(real) → 1
D(fake) → 0
```

---

# 10. Generator Loss

The Generator wants the discriminator to classify generated images as real.

Therefore:

```
Fake image
    ↓
Discriminator
    ↓
Want output = 1
```

So the Generator tries to minimize:

```
Generator loss =
BCE(D(fake), 1)
```

---

# 11. Simple Mathematical Form

The original GAN objective is often written as:

```
min G max D

E[log D(x)] +
E[log(1 - D(G(z)))]
```

Where:

```
G = Generator
D = Discriminator
x = Real data
z = Random noise
```

You don't need to memorize the formula initially. Understand the concept:

> **D learns to distinguish real/fake, while G learns to fool D.**
> 

---

# 12. Random Noise

The Generator doesn't usually receive an image directly.

It receives a random vector called **latent noise**.

Example:

```python
noise = torch.randn(batch_size, latent_dim)
```

Example:

```
latent_dim = 100

Noise:

[0.31, -0.82, 0.14, ..., 0.56]
```

The Generator converts this vector into an image.

```
Noise
  ↓
Generator
  ↓
Image
```

---

# 13. GAN Architecture

A basic GAN:

```
                  Noise
                    │
                    ▼
             ┌─────────────┐
             │  Generator  │
             └──────┬──────┘
                    │
                 Fake Image
                    │
              ┌─────▼─────┐
Real Image ──►│Discriminator│
              └─────┬─────┘
                    │
              Real / Fake
```

---

# 14. GAN vs Normal Neural Network

A normal classifier:

```
Image
 ↓
Neural Network
 ↓
Class
```

Example:

```
Image → Cat
```

A GAN:

```
Noise
 ↓
Generator
 ↓
New Image
```

So GANs are **generative models**.

---

# 15. DCGAN

**DCGAN = Deep Convolutional Generative Adversarial Network**

Instead of simple fully connected layers, DCGAN uses **Convolutional Neural Networks**.

Generator:

```
Noise
 ↓
Linear
 ↓
Transpose Convolution
 ↓
Transpose Convolution
 ↓
Image
```

Discriminator:

```
Image
 ↓
Convolution
 ↓
Convolution
 ↓
Linear
 ↓
Real/Fake
```

DCGANs are especially useful for image generation.

---

# 16. StyleGAN

**StyleGAN** is a more advanced GAN architecture designed for high-quality image generation.

It introduced techniques for controlling different aspects of generated images.

Conceptually:

```
Latent Code
     ↓
Style Mapping
     ↓
Generator
     ↓
High-quality Image
```

StyleGAN has been widely associated with realistic synthetic face generation.

---

# 17. CycleGAN

**CycleGAN** is designed for **image-to-image translation without requiring paired training images**.

Example:

```
Horse Image
    ↓
CycleGAN
    ↓
Zebra Image
```

Another example:

```
Summer Image
     ↓
CycleGAN
     ↓
Winter Image
```

Concept:

```
Domain A → Domain B
Domain B → Domain A
```

Cycle consistency helps preserve important content.

---

# 18. GAN Comparison

| GAN | Main Idea | Typical Use |
| --- | --- | --- |
| Basic GAN | Basic adversarial generation | Learning GAN concepts |
| DCGAN | CNN-based GAN | Image generation |
| StyleGAN | Style-based generation | High-quality images |
| CycleGAN | Unpaired image translation | Domain conversion |

---

# 19. GAN Problems

GAN training can be difficult.

### Mode Collapse

The Generator produces very similar samples.

```
Noise 1 → Same type of image
Noise 2 → Same type of image
Noise 3 → Same type of image
```

The Generator isn't producing enough diversity.

---

### Training Instability

Generator and Discriminator can become unbalanced.

```
D too strong
   ↓
G receives weak/use-less learning signal
```

or:

```
G improves too quickly
   ↓
D struggles
```

Good GAN training requires balance.

---

### Difficult Evaluation

It's not always easy to determine whether generated images are "good."

Common metrics include:

- Inception Score (IS)
- Fréchet Inception Distance (FID)

For your basic task, visual inspection is enough to understand the concept.

---

# 20. GAN vs VAE vs LLM

You may encounter these later.

| Model | Main Purpose |
| --- | --- |
| GAN | Generate data through adversarial training |
| VAE | Learn probabilistic latent representation and generate data |
| LLM | Generate/process text |
| Diffusion Model | Generate data through iterative denoising |

---

# 21. Complete PyTorch GAN Example

Now let's build a **basic GAN that generates MNIST handwritten digits**.

This is a good beginner project because MNIST is small and easy to work with.

## Step 1 — Install

In Jupyter/Colab:

```python
!pip install torch torchvision matplotlib
```

---

# 22. Import Libraries

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
```

---

# 23. Device

```python
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print(device)
```

If Google Colab GPU is enabled, you may see:

```
cuda
```

Otherwise:

```
cpu
```

---

# 24. Load MNIST Dataset

```python
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(
        (0.5,),
        (0.5,)
    )
])

dataset = datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

dataloader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)
```

---

# 25. Generator

The Generator converts:

```
100-dimensional noise
        ↓
      28×28 image
```

Code:

```python
class Generator(nn.Module):

    def __init__(self, latent_dim=100):

        super().__init__()

        self.model = nn.Sequential(

            nn.Linear(latent_dim, 128),
            nn.ReLU(),

            nn.Linear(128, 256),
            nn.ReLU(),

            nn.Linear(256, 512),
            nn.ReLU(),

            nn.Linear(512, 784),
            nn.Tanh()
        )

    def forward(self, x):

        x = self.model(x)

        return x.view(
            x.size(0),
            1,
            28,
            28
        )
```

---

# 26. Discriminator

The Discriminator receives:

```
28 × 28 image
```

and outputs:

```
0 → Fake
1 → Real
```

```python
class Discriminator(nn.Module):

    def __init__(self):

        super().__init__()

        self.model = nn.Sequential(

            nn.Flatten(),

            nn.Linear(784, 512),
            nn.LeakyReLU(0.2),

            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),

            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x):

        return self.model(x)
```

---

# 27. Create Models

```python
latent_dim = 100

generator = Generator(
    latent_dim
).to(device)

discriminator = Discriminator().to(device)
```

---

# 28. Loss Function

Use Binary Cross Entropy:

```python
criterion = nn.BCELoss()
```

---

# 29. Optimizers

Use Adam:

```python
optimizer_G = optim.Adam(
    generator.parameters(),
    lr=0.0002,
    betas=(0.5, 0.999)
)

optimizer_D = optim.Adam(
    discriminator.parameters(),
    lr=0.0002,
    betas=(0.5, 0.999)
)
```

---

# 30. Training

Set:

```python
epochs = 10
```

Then:

```python
for epoch in range(epochs):

    for real_images, _ in dataloader:

        real_images = real_images.to(device)

        batch_size = real_images.size(0)

        # -------------------------
        # Train Discriminator
        # -------------------------

        real_labels = torch.ones(
            batch_size,
            1,
            device=device
        )

        fake_labels = torch.zeros(
            batch_size,
            1,
            device=device
        )

        optimizer_D.zero_grad()

        # Real images
        real_output = discriminator(
            real_images
        )

        loss_real = criterion(
            real_output,
            real_labels
        )

        # Generate fake images
        noise = torch.randn(
            batch_size,
            latent_dim,
            device=device
        )

        fake_images = generator(noise)

        fake_output = discriminator(
            fake_images.detach()
        )

        loss_fake = criterion(
            fake_output,
            fake_labels
        )

        # Total discriminator loss
        loss_D = loss_real + loss_fake

        loss_D.backward()

        optimizer_D.step()

        # -------------------------
        # Train Generator
        # -------------------------

        optimizer_G.zero_grad()

        noise = torch.randn(
            batch_size,
            latent_dim,
            device=device
        )

        fake_images = generator(noise)

        output = discriminator(
            fake_images
        )

        loss_G = criterion(
            output,
            real_labels
        )

        loss_G.backward()

        optimizer_G.step()

    print(
        f"Epoch [{epoch+1}/{epochs}] "
        f"Loss D: {loss_D.item():.4f}, "
        f"Loss G: {loss_G.item():.4f}"
    )
```

---

# 31. What Happens During Training?

Every iteration:

### Step 1

Take real MNIST images.

```
Real MNIST
    ↓
Discriminator
```

### Step 2

Generate random noise.

```
Noise
 ↓
Generator
 ↓
Fake MNIST
```

### Step 3

Give fake images to discriminator.

```
Fake Image
    ↓
Discriminator
```

### Step 4

Train discriminator.

```
Real → 1
Fake → 0
```

### Step 5

Train generator.

Generator tries:

```
Fake → 1
```

because it wants to fool the discriminator.

---

# 32. Generate New Images

After training:

```python
generator.eval()

noise = torch.randn(
    16,
    latent_dim,
    device=device
)

with torch.no_grad():

    generated_images = generator(
        noise
    ).cpu()
```

---

# 33. Display Generated Images

```python
fig, axes = plt.subplots(
    4,
    4,
    figsize=(8, 8)
)

for i, ax in enumerate(axes.flat):

    ax.imshow(
        generated_images[i].squeeze(),
        cmap="gray"
    )

    ax.axis("off")

plt.tight_layout()
plt.show()
```

You should see generated handwritten digits.

Early training may look like:

```
Noise / blurry shapes
```

After more training:

```
0   1   2   3
4   5   6   7
8   9   0   5
...
```

The exact quality depends on training time, hardware, hyperparameters, and implementation.

---

# 34. Save Generator

You can save the trained Generator:

```python
torch.save(
    generator.state_dict(),
    "generator.pth"
)
```

Load later:

```python
generator.load_state_dict(
    torch.load(
        "generator.pth",
        map_location=device
    )
)
```

---

# 35. Full GAN Workflow

For your notes, remember:

```
MNIST Dataset
      ↓
Real Images
      │
      ├─────────────────────┐
      │                     │
      ▼                     │
Discriminator              │
      ▲                     │
      │                     │
Fake Images                 │
      ▲                     │
      │                     │
Generator ◄──── Noise       │
      │                     │
      └─────────────────────┘
```

Training:

```
Noise
 ↓
Generator
 ↓
Fake Images
 ↓
Discriminator
 ↓
Real / Fake
 ↓
Loss
 ↓
Backpropagation
 ↓
Update Networks
 ↓
Repeat
```

---

---

# 37. Your GAN Deliverable

For your internship task, create:

```
gan-project/
│
├── gan_mnist.ipynb
├── generator.py
├── discriminator.py
├── requirements.txt
├── generated_images/
└── README.md
```

### Most important takeaway

Think of GAN training as a competition:

```
             ┌──────────────┐
             │  Generator   │
             │ "I'll make   │
             │  fake data!" │
             └──────┬───────┘
                    │
                    ▼
                Fake Image
                    │
                    ▼
             ┌──────────────┐
             │Discriminator │
             │ "I'll detect │
             │   the fake!" │
             └──────────────┘
                    │
                    ▼
               Real / Fake

Generator → learns to fool D
Discriminator → learns to detect G
```

As training progresses, **the Generator gets better at creating realistic samples and the Discriminator gets better at detecting them**. That adversarial learning process is the core idea behind GANs.