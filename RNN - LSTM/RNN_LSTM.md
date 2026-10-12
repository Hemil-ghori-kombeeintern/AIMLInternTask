## 1. Sequential data

Sequential data is data where order matters: text, speech, sensor readings, stock prices, and activity sequences.

## 2. RNN (Recurrent Neural Network)

An RNN processes a sequence one step at a time. It combines the current input with the previous hidden state.

$$
[
h_t = (W_x x_t + W_h h_{t-1} + b_h)
]
$$

- `x_t`: current input vector
- `h_(t-1)`: previous hidden state
- `W_x`, `W_h`: learned weights
- `b_h`: bias
- `h_t`: new hidden state

An output may be calculated as `y_t = W_y h_t + b_y`.

### RNN patterns

- **Many-to-one:** sequence → one label, such as sentiment classification.
- **One-to-many:** one context → sequence generation.
- **Many-to-many:** sequence → multiple labels, such as token labeling.

### Basic RNN limitations

- **Vanishing gradients:** gradients become very small during backpropagation through long sequences.
- **Exploding gradients:** gradients become excessively large; gradient clipping can help.
- **Limited memory:** information may be overwritten in long sequences.
- **Sequential computation:** steps depend on previous states.

## 3. LSTM (Long Short-Term Memory)

LSTM is a gated RNN designed to retain useful information across longer sequences. It has:

- **Hidden state (`h_t`):** current representation passed forward and often used for output.
- **Cell state (`c_t`):** memory pathway that carries information through the sequence.

### Three gates

1. **Forget gate:** decides what old cell-state information to retain.
2. **Input gate:** controls how much new information to write.
3. **Output gate:** controls what information is exposed in the hidden state.

## 4. RNN vs LSTM

| Feature | RNN | LSTM |
| --- | --- | --- |
| State | Hidden state | Hidden and cell states |
| Gates | No LSTM-style gates | Forget, input, output |
| Long dependencies | Often struggles | Generally better at retaining information |
| Parameters | Fewer | More |
| Computation | Simpler | More involved |

LSTM is not always better; model choice depends on data and task.

## 5. PyTorch sequence shapes

With `batch_first=True`, input shape is `(batch_size, sequence_length, input_size)`. Example `(64, 20, 1)` means 64 sequences, 20 time steps, one feature per step.

For a single-layer unidirectional model:

- RNN output: `(batch, sequence, hidden_size)`
- hidden state: `(layers, batch, hidden_size)`
- LSTM also returns a cell state with the hidden-state shape.

## 6. Training workflow

1. `model.train()`
2. `optimizer.zero_grad()`
3. Forward pass: `logits = model(inputs)`
4. Calculate loss: `loss = criterion(logits, labels)`
5. Backpropagate: `loss.backward()`
6. Update weights: `optimizer.step()`

For classification, `nn.CrossEntropyLoss` takes raw logits and integer class labels; do not apply softmax before the loss.

## 7. Applications

- Sentiment analysis and text classification
- Token/sequence labeling
- Speech processing
- Time-series classification and forecasting
- Sensor anomaly detection

Transformers are often preferred for modern large-scale NLP, but RNN/LSTM remain useful for learning sequence modeling and some time-series or resource-constrained tasks.

## 8. Key terms

- **Time step:** one position in a sequence.
- **Hidden state:** recurrent representation carried across steps.
- **Cell state:** LSTM memory pathway.
- **BPTT:** Backpropagation Through Time.
- **Gradient clipping:** limits gradient magnitude to help with exploding gradients.
- **Embedding:** numerical representation of a token.

## 9. Practical experiment

The companion notebook trains RNN and LSTM classifiers on synthetic sensor sequences. Class 1 has a strong spike at a random position; class 0 contains noise only. This demonstrates implementation and evaluation, not that one architecture is universally better.