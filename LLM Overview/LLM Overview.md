# LLM Overview — Complete Learning Notes


## 1. What is an LLM?

**LLM = Large Language Model**

An LLM is a neural network trained on a very large amount of text to learn patterns in language.

It can perform tasks such as:

- Text generation
- Question answering
- Summarization
- Translation
- Classification
- Code generation
- Information extraction
- Conversation

Examples of LLM families include:

- GPT
- LLaMA
- Mistral
- Falcon

A simple view:

```
Large amount of text
        ↓
    Training
        ↓
   Transformer
        ↓
   LLM Model
        ↓
 User Prompt
        ↓
Generated Response
```

---

# 2. How is an LLM different from a normal ML model?

A traditional ML model might be trained for one specific task.

For example:

```
Input → Spam Classifier → Spam / Not Spam
```

An LLM is much more general:

```
                ┌─ Question Answering
                ├─ Translation
Input Prompt ───┼─ Summarization
                ├─ Coding
                ├─ Text Generation
                └─ Classification
```

The same model can perform many tasks depending on the prompt.

---

# 3. Basic LLM Workflow

At a high level:

```
Text
 ↓
Tokenization
 ↓
Tokens
 ↓
Token IDs
 ↓
Embeddings
 ↓
Transformer
 ↓
Probability Distribution
 ↓
Next Token
 ↓
Next Token
 ↓
Next Token
 ↓
Generated Text
```

This is one of the most important workflows to understand.

---

# 4. What is a Transformer?

Most modern LLMs are based on the **Transformer architecture**.

The Transformer was introduced in the research paper:

> "Attention Is All You Need"
> 

The important idea is **attention**.

Instead of processing words only based on their immediate neighbors, attention allows the model to determine which other tokens are important for understanding the current token.

---

# 5. Why Transformers?

Consider:

```
The cat sat on the mat because it was tired.
```

What does **"it"** refer to?

A Transformer can learn relationships between tokens:

```
it
 ↓
cat
```

Attention helps the model determine which parts of the context are relevant.

---

# 6. Transformer High-Level Architecture

A simplified Transformer:

```
Input Tokens
     ↓
Token Embeddings
     ↓
Positional Information
     ↓
Self-Attention
     ↓
Feed Forward Network
     ↓
Layer Normalization
     ↓
Repeated Transformer Blocks
     ↓
Output
```

An LLM contains many Transformer blocks.

---

# 7. What is a Token?

LLMs don't directly process normal human sentences.

They process **tokens**.

For example:

```
"I love Python"
```

might be split conceptually as:

```
"I"
"love"
"Python"
```

But tokenization can also split words into subword pieces.

For example:

```
unbelievable
```

could be represented as pieces similar to:

```
"un"
"believ"
"able"
```

The exact tokens depend on the tokenizer.

---

# 8. Token IDs

Tokens are converted into numbers.

Example:

```
Text:

I love AI

        ↓

Tokens:

["I", "love", "AI"]

        ↓

Token IDs:

[40, 982, 1245]
```

The actual numbers depend on the tokenizer.

Neural networks work with numerical representations rather than raw text.

---

# 9. Tokenization Example

Using Hugging Face Transformers:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "gpt2"
)

text = "I love artificial intelligence"

tokens = tokenizer.tokenize(text)

print(tokens)
```

Get token IDs:

```python
token_ids = tokenizer.encode(text)

print(token_ids)
```

Decode them back:

```python
decoded = tokenizer.decode(token_ids)

print(decoded)
```

Workflow:

```
Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
Token IDs
```

---

# 10. What are Embeddings?

Token IDs themselves don't contain meaningful semantic information.

The model converts tokens into vectors called **embeddings**.

Conceptually:

```
Token ID
   ↓
Embedding Layer
   ↓
Vector
```

Example:

```
"king"
   ↓
[0.21, -0.43, 0.81, ...]
```

Real embedding vectors contain many dimensions.

Embeddings allow the model to represent relationships between tokens.

---

# 11. Context

**Context** means the information available to the model when generating a response.

Example:

```
User:

Python is a programming language.
It is widely used in AI.

Question:

What is Python?
```

The model uses the previous text as context.

```
Context
   ↓
Transformer
   ↓
Prediction
```

---

# 12. Context Window

An LLM can only process a certain amount of tokens at once.

This is called the **context window**.

Conceptually:

```
Context Window
┌──────────────────────────┐
│ Previous conversation    │
│ Documents                │
│ User prompt              │
│ Instructions             │
└──────────────────────────┘
```

If the input exceeds the model's supported context length, the application must handle it through techniques such as truncation or chunking.

This becomes especially important later when you learn **RAG**.

---

# 13. Self-Attention ⭐⭐⭐

Self-attention allows tokens to consider other tokens in the sequence.

Example:

```
The dog chased the ball because it was excited.
```

When processing:

```
"it"
```

the model can learn to pay attention to relevant earlier tokens.

Conceptually:

```
it
 ↓
dog
 ↓
attention relationship
```

This allows the model to capture relationships across the sequence.

---

# 14. Attention Example

Imagine:

```
The student opened the book because it was interesting.
```

Attention helps the model learn relationships such as:

```
"it" → "book"
```

The exact internal attention patterns are much more complex, but this is the basic intuition.

---

# 15. Feed Forward Network

Transformer blocks also contain feed-forward neural networks.

Simplified:

```
Attention
   ↓
Feed Forward Network
   ↓
Next Transformer Block
```

The feed-forward portion performs learned transformations on the representations.

This connects nicely with your previous MLP knowledge.

---

# 16. Transformer Block

A simplified Transformer block:

```
Input
  ↓
Self-Attention
  ↓
Add & Norm
  ↓
Feed Forward Network
  ↓
Add & Norm
  ↓
Output
```

An LLM contains many such blocks.

```
Input
 ↓
Block 1
 ↓
Block 2
 ↓
Block 3
 ↓
...
 ↓
Block N
 ↓
Output
```

---

# 17. GPT

**GPT = Generative Pre-trained Transformer**

GPT models are Transformer-based generative language models.

The GPT approach is based primarily on the **decoder-style Transformer architecture**.

Basic idea:

```
Prompt
  ↓
Tokens
  ↓
Transformer
  ↓
Next-token prediction
  ↓
Generated text
```

Examples of GPT-family models include various generations of GPT models.

---

# 18. How GPT Generates Text

Suppose the prompt is:

```
The sky is
```

The model predicts probabilities for possible next tokens:

```
blue      → 0.70
beautiful → 0.10
dark      → 0.05
...
```

It selects a token according to the model's decoding strategy.

Then:

```
The sky is blue
```

Now it predicts the next token again.

```
The sky is blue ...
```

This continues until generation stops.

---

# 19. Autoregressive Generation ⭐⭐⭐

GPT-style generation is **autoregressive**.

That means:

```
Previous tokens
      ↓
Predict next token
      ↓
Add token to sequence
      ↓
Predict next token
      ↓
Repeat
```

Example:

```
Input:

The weather is

Step 1:
The weather is → good

Step 2:
The weather is good → today

Step 3:
The weather is good today → .
```

---

# 20. LLaMA

**LLaMA** is a family of large language models developed by Meta.

LLaMA models are also based on Transformer architectures and are designed for efficient language modeling.

The LLaMA family has been widely used for:

- Research
- Local inference
- Fine-tuning
- Chat applications
- Generative AI applications

One important distinction:

**LLaMA is a model family**, while GPT is also a model family.

They can use similar fundamental Transformer concepts while differing in architecture details, training choices, model sizes, licensing, and intended usage.

---

# 21. Mistral

**Mistral** is a family of language models developed by Mistral AI.

Mistral models are known for focusing on:

- Strong performance
- Efficient inference
- Different model sizes
- Open-weight models in parts of the ecosystem
- Efficient Transformer techniques

Examples include model families such as:

```
Mistral
Mixtral
```

---

# 22. Falcon

**Falcon** is a family of large language models developed by the Technology Innovation Institute (TII).

Falcon models have been used for:

- Text generation
- Research
- Chat applications
- Local/self-hosted experimentation

Like GPT, LLaMA, and Mistral, Falcon models are based on Transformer-style architectures.

---

# 23. GPT vs LLaMA vs Mistral vs Falcon

At a high level:

| Model Family | Organization | Architecture | Common Usage |
| --- | --- | --- | --- |
| GPT | OpenAI | Transformer-based | General-purpose generation |
| LLaMA | Meta | Transformer-based | Research, local inference, fine-tuning |
| Mistral | Mistral AI | Transformer-based | Efficient LLM applications |
| Falcon | TII | Transformer-based | Research and generative AI |

Don't memorize individual model specifications yet.

For your current Jira task, understand:

> **These are different LLM families built around Transformer-based language modeling, with differences in model architecture details, training, sizes, licensing/access, and intended usage.**
> 

---

# 24. Pre-trained Model

A **pre-trained model** has already been trained on a large dataset.

Example:

```
Large text dataset
       ↓
Pre-training
       ↓
Pre-trained LLM
```

You can then use the model for inference.

---

# 25. Instruction-Tuned Model

A pre-trained model may be further trained to better follow human instructions.

```
Pre-training
     ↓
Base Model
     ↓
Instruction Tuning
     ↓
Instruction-following Model
```

For example:

```
User:
Summarize this paragraph.

Instruction-tuned model:
Provides a summary.
```

Instead of simply continuing text.

---

# 26. Base Model vs Instruction Model

### Base model

Primarily trained for language modeling / next-token prediction.

Example:

```
Complete this:

Python is a
```

Possible continuation:

```
programming language...
```

### Instruction-tuned model

Optimized to respond to instructions.

```
Explain Python in simple terms.
```

It is trained to follow the instruction and produce a useful answer.

---

# 27. Pre-training

Pre-training is the large-scale initial training stage.

A simplified objective for a GPT-style model is:

```
Given previous tokens:

"The capital of France is"

Predict:

"Paris"
```

The model performs this task over huge amounts of text.

During training:

```
Text
 ↓
Tokens
 ↓
Model
 ↓
Prediction
 ↓
Loss
 ↓
Backpropagation
 ↓
Optimizer
 ↓
Updated parameters
```

Notice how this connects directly to your **MLP + Backpropagation** topic.

---

# 28. LLM Training Connection to What You Learned

You learned:

```
Forward
 ↓
Loss
 ↓
Backward
 ↓
Gradient
 ↓
Optimizer
```

LLMs also follow this basic learning cycle.

Conceptually:

```
Training Text
     ↓
Tokenization
     ↓
Transformer
     ↓
Next-token Prediction
     ↓
Loss
     ↓
Backpropagation
     ↓
Gradient
     ↓
Optimizer
     ↓
Updated Parameters
```

The difference is the **scale and architecture**.

---

# 29. Parameters

Parameters are the learned values inside the neural network.

Examples:

```
Weights
Biases
```

A large LLM can contain billions of parameters.

For example:

```
1B parameters
7B parameters
13B parameters
70B parameters
...
```

`B` means billion.

More parameters generally means a larger model, but **larger does not automatically mean better for every task**.

---

# 30. Inference

**Inference** means using a trained model to generate predictions.

Training:

```
Data
 ↓
Model
 ↓
Loss
 ↓
Backpropagation
 ↓
Update
```

Inference:

```
Prompt
 ↓
Model
 ↓
Prediction
```

There is no parameter update during normal inference.

---

# 31. Training vs Inference

| Training | Inference |
| --- | --- |
| Learns parameters | Uses learned parameters |
| Requires gradients | Usually no gradients |
| Uses optimizer | No optimizer update |
| Computationally expensive | Usually cheaper |
| Uses training data | Uses user/application input |

---

# 32. Text Generation

A simple Hugging Face example:

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

result = generator(
    "Artificial intelligence is",
    max_new_tokens=30
)

print(result[0]["generated_text"])
```

Conceptually:

```
Prompt
 ↓
Tokenizer
 ↓
GPT-2
 ↓
Next-token prediction
 ↓
Generated text
```

---

# 33. What is `max_new_tokens`?

```python
max_new_tokens=30
```

controls approximately how many new tokens the model is allowed to generate.

For example:

```python
generator(
    "Python is",
    max_new_tokens=20
)
```

---

# 34. Temperature

Temperature controls the randomness of token selection during generation.

Conceptually:

```
Low temperature
→ More predictable

High temperature
→ More varied/random
```

Example:

```python
generator(
    "AI is",
    max_new_tokens=30,
    temperature=0.7
)
```

The exact behavior also depends on the decoding configuration.

---

# 35. Greedy Decoding

Greedy decoding selects the highest-probability next token.

Conceptually:

```
Token probabilities:

A → 0.10
B → 0.20
C → 0.70

Choose C
```

It is simple but can produce less varied text.

---

# 36. Sampling

Instead of always choosing the highest-probability token, sampling can choose among possible tokens according to their probabilities.

```
Token A → 10%
Token B → 20%
Token C → 70%
```

The model samples from the distribution.

This can produce more varied outputs.

---

# 37. Top-K

Top-K sampling keeps only the top K candidates.

Example:

```
K = 3
```

The model considers only the three highest-probability tokens before sampling.

---

# 38. Top-P

Top-P sampling selects from the smallest group of tokens whose cumulative probability reaches a chosen threshold.

Example:

```
top_p = 0.9
```

This dynamically changes how many candidate tokens are considered.

For your current task, understand these concepts at a high level rather than memorizing decoding mathematics.

---

# 39. Hugging Face

**Hugging Face** provides tools and model repositories that make it easier to work with many pre-trained models.

Important library:

```bash
pip install transformers
```

Common workflow:

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)
```

---

# 40. Simple LLM Experiment

You can practice this in Jupyter/Colab.

```python
!pip install transformers torch
```

Then:

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)
```

Generate:

```python
prompt = "Machine learning is"

result = generator(
    prompt,
    max_new_tokens=40
)

print(result[0]["generated_text"])
```

Try different prompts:

```python
prompts = [
    "Artificial intelligence is",
    "Python is useful for",
    "The future of technology is"
]

for prompt in prompts:

    result = generator(
        prompt,
        max_new_tokens=30
    )

    print(result[0]["generated_text"])
    print("-" * 50)
```

---

# 41. Loading a Model Directly

You can also use:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(model_name)
```

Tokenize:

```python
inputs = tokenizer(
    "Artificial intelligence is",
    return_tensors="pt"
)
```

Generate:

```python
outputs = model.generate(
    **inputs,
    max_new_tokens=30
)
```

Decode:

```python
text = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print(text)
```

This gives you a better understanding of what the `pipeline()` abstraction is doing for you.

---

# 42. Pipeline vs Direct Model Usage

### Pipeline

Easy:

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)
```

Good for:

- Learning
- Prototyping
- Quick experiments

### Direct model/tokenizer

More control:

```python
tokenizer = AutoTokenizer.from_pretrained(...)
model = AutoModelForCausalLM.from_pretrained(...)
```

Good for:

- Custom workflows
- Understanding internals
- More control over generation
- Production experimentation

---

# 43. What is a Causal Language Model?

A causal language model predicts the next token based on previous tokens.

```
The
 ↓
The cat
 ↓
The cat is
 ↓
The cat is sleeping
```

At each step:

```
Previous tokens
      ↓
Predict next token
```

GPT-style models are commonly associated with causal language modeling.

---

# 44. LLM Mental Model

Keep this diagram in your notes:

```
                    LLM

                     │
                     ▼
                  Prompt
                     │
                     ▼
                Tokenization
                     │
                     ▼
                  Token IDs
                     │
                     ▼
                Embeddings
                     │
                     ▼
              Transformer Blocks
                     │
              ┌──────┴──────┐
              │             │
          Attention      Feed Forward
              │             │
              └──────┬──────┘
                     │
                     ▼
              Next-token scores
                     │
                     ▼
              Decoding/Sampling
                     │
                     ▼
              Next Token
                     │
                     ▼
              Repeat Generation
                     │
                     ▼
                Final Text
```

---

# 45. Most Important Differences

### Traditional ML

```
Input
 ↓
Features
 ↓
ML Model
 ↓
Prediction
```

### Deep Neural Network

```
Input
 ↓
Layers
 ↓
Activations
 ↓
Prediction
```

### LLM

```
Text
 ↓
Tokens
 ↓
Embeddings
 ↓
Transformer
 ↓
Next-token probabilities
 ↓
Generated text
```
