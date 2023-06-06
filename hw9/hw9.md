# 1.

$P(A=t) = \frac{11}{22}$

$ENT(A) = -0.5\log_2(0.5) - 0.5\log_2(0.5) = 1$

$P(B=t) = \frac{14}{22}$

$ENT(B) = -0.\overline{36} \log_2(0.\overline{36}) - 0.\overline{63}
\log_2(0.\overline{63}) \approx 0.9457$

$P(C=t) = \frac{7}{22}$

$ENT(C) = -0.3\overline{18} \log_2(0.3\overline{18}) - 0.6\overline{81}
\log_2(0.6\overline{81}) \approx 0.9024$

We need a place to start, and we can choose $A$ since it has the highest
entropy, and thus we can have a higher possible loss in entropy (information
gain) if we start here.

Branching off of $A=t$ we have:

$ENT(C\mid A=t) = -0.\overline{36} \log_2(0.\overline{36}) - 0.\overline{63}
\log_2(0.\overline{63}) \approx 0.9457$

$ENT(B\mid A=t) = -0.\overline{36} \log_2(0.\overline{36}) - 0.\overline{63}
\log_2(0.\overline{63}) \approx 0.9457$

These entropies are the same, meaning our information gain is the same, so we
will just choose $B$ next because it simplifies the decision tree.

With $A=f$ we have:

$ENT(C\mid A=f) = -0.\overline{72} \log_2(0.\overline{72}) - 0.\overline{27}
\log_2(0.\overline{27}) \approx 0.8454$

$ENT(B\mid A=f) = -0.\overline{36} \log_2(0.\overline{36}) - 0.\overline{63}
\log_2(0.\overline{63}) \approx 0.9457$

Now we have a greater information gain by choosing $C$ (it has a lower
conditional entropy) so this is our most discriminating attribute when $A=f$.

```mermaid
flowchart TD

A((A)) --> |false|C((C))
A --> |true|B((B))
B --> |false|G[D = No]
B --> |true|F[D = Yes]
C --> |false|D[D = No]
C --> |true|E[D = Yes]
```

# 2.

We want to find $(A \lor \lnot B) \oplus (\lnot C \lor D)$ using the following
neural network:

```dot
digraph G {

rankdir=LR
splines=line

node [fixedsize=true, label=""];

subgraph cluster_0 {
  color=white;
  node [style=solid,color=black, shape=circle];
  x1 [label="A"] x2 [label="B"] x3 [label="C"] x4 [label="D"];
  label = "Layer 1 (Input layer)";
}

subgraph cluster_1 {
  color=white;
  node [style=solid,color=purple, shape=circle];
  a12 a22 a32 a42;
  label = "Layer 2 (hidden layer)";
}

subgraph cluster_2 {
  color=white;
  node [style=solid,color=seagreen2, shape=circle];
  O;
  label="Layer 3 (output layer)";
}

x1 -> a12;
x1 -> a22;
x1 -> a32;
x1 -> a42;
x2 -> a12;
x2 -> a22;
x2 -> a32;
x2 -> a42;
x3 -> a12;
x3 -> a22;
x3 -> a32;
x3 -> a42;
x4 -> a12;
x4 -> a22;
x4 -> a32;
x4 -> a42;

a12 -> O
a22 -> O
a32 -> O
a42 -> O
}
```

<br />

We will denote inputs as `true = 1` and `false = 0`.

First we will simplify the original equation using $x \oplus y = (\overline{x}
\land y) \lor (x \land \overline{y})$.

$$(A \lor \lnot B) \oplus (\lnot C \lor D)$$

$$= (\overline{(A \lor \lnot B)} \land (\lnot C \lor D)) \lor ((A \lor \lnot B)
\land \overline{(\lnot C \lor D)})$$

$$ = ((\lnot A \land B) \land (\lnot C \lor D)) \lor ((A \lor \lnot B) \land (C
\land \lnot D))$$

$$= (\lnot A \land B \land \lnot C) \lor (\lnot A \land B \land D) \lor (A \land
C \land \lnot D) \lor (\lnot B \land C \land \lnot D)$$

Now we can generate a neural network. We assign each hidden layer node to a term
where each input to the node is given a weight of 1 if the variable in that term
is positive, and a weight of -1 if the variable is negated. We will use blue to
denote a weight of 1 and red to denote a weight of -1.

```dot
digraph G {

rankdir=LR
splines=line

node [fixedsize=true, label=""];
edge [color="blue"]

subgraph cluster_0 {
  color=white;
  node [style=solid,color=black, shape=circle];
  x1 [label="A"] x2 [label="B"] x3 [label="C"] x4 [label="D"];
  label = "Layer 1 (Input layer)";
}

subgraph cluster_1 {
  color=white;
  node [style=solid,color=purple, shape=circle];
  a12 a22 a32 a42;
  label = "Layer 2 (hidden layer)";
}

subgraph cluster_2 {
  color=white;
  node [style=solid,color=seagreen2, shape=circle];
  O;
  label="Layer 3 (output layer)";
}

x1 -> a12 [color="red"];
x1 -> a22 [color="red"];
x1 -> a32
x2 -> a12
x2 -> a22;
x2 -> a42 [color="red"];
x3 -> a12 [color="red"];
x3 -> a32;
x3 -> a42;
x4 -> a22;
x4 -> a32 [color="red"];
x4 -> a42 [color="red"];

a12 -> O [color="black"]
a22 -> O [color="black"]
a32 -> O [color="black"]
a42 -> O [color="black"]
}
```

<br />

So this is our network so far. Since each term is a set of literals connected
with conjunctions (`AND`), we need each hidden layer node to output 1 only if
all given inputs are `true`. This happens if and only if the sum of the given
weights is equal to the amount of positive variable inputs. This is because the
hidden layer nodes use the step function, which is 1 when the sum of the inputs
are above or equal to the threshold, and 0 otherwise. The terms themselves are
positive (not negated) so we will just keep their output weights at 1 and the
output node threshold will be 1 since we only need 1 of the hidden layer nodes
to evaluate to `true` (the terms are connected with disjunctions (`OR`)). Our
finished network looks like this:

```dot
digraph G {

rankdir=LR
splines=line

node [fixedsize=true, label=""];
edge [color="blue"]

subgraph cluster_0 {
  color=white;
  node [style=solid,color=black, shape=circle];
  x1 [label="A"] x2 [label="B"] x3 [label="C"] x4 [label="D"];
  label = "Layer 1 (Input layer)";
}

subgraph cluster_1 {
  color=white;
  node [style=solid,color=purple, shape=circle];
  a12 [label="1"] a22 [label="2"] a32 [label="2"] a42 [label="1"];
  label = "Layer 2 (hidden layer)";
}

subgraph cluster_2 {
  color=white;
  node [style=solid,color=seagreen2, shape=circle];
  O [label="1"];
  label="Layer 3 (output layer)";
}

x1 -> a12 [color="red"];
x1 -> a22 [color="red"];
x1 -> a32
x2 -> a12
x2 -> a22;
x2 -> a42 [color="red"];
x3 -> a12 [color="red"];
x3 -> a32;
x3 -> a42;
x4 -> a22;
x4 -> a32 [color="red"];
x4 -> a42 [color="red"];

a12 -> O
a22 -> O
a32 -> O
a42 -> O
}
```
