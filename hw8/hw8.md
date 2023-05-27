# 1.

Contents of `test.net`:

![Bayesian network](/home/rileyb/Pictures/bayesiannetwork1.png)
![D Properties](/home/rileyb/Pictures/d_properties.png)
![T Properties](/home/rileyb/Pictures/t_properties.png)

Disease and false positive probability constraints:

![Disease and false positive probability](/home/rileyb/Pictures/disease_and_false_pos.png)

- Probability of having disease constraint: $\ge$ 0.00894
- False positive constraint: $\le$ 0.00222

![False negative probability](/home/rileyb/Pictures/false_neg.png)

- False negative constraint: $\le$ 0.00597

# 2.

Most likely instantiation given no bark detected but light detected:

![Most likely instantiation](/home/rileyb/Pictures/instantiation_a.png)

- I obtained this answer by opening up the `sambot.net` file generated after
  given the evidence in the `sambot.dat` file, then setting `LightSensor = On`
  and `SoundSensor = Off`.

Most likely instantiation given the family is home and no guests expected:

![Most likely instantiation](/home/rileyb/Pictures/instantiation_b.png)

- I obtained this answer by following the same steps as above but this time
  setting the known variables to be `FamilyHome = Yes` and
  `ExpectingGuests = No`.

For $d\_sep(\text{LightSensor}, Z, \text{SoundSensor})$, we can say $Z =
\{\text{Battery}, \text{FamilyHome}\}$. This is because these nodes are
divergent, so blocking them will require less nodes to be blocked than if we
block nodes further down the line (as more will be required to be blocked due to
the divergent nature). These are also the only two nodes that have both sensors
as descendents. Thus blocking `Battery` and `FamilyHome` is sufficient to make
the sensors d-separable and thus independent given $Z$.

The type of the network:

![Network](/home/rileyb/Pictures/sambotnetwork.png)

is multiply-connected since there exist pairs of nodes with more than one
undirected path between each other (for example you can connect `LightSensor`
and `SoundSensor` taking a path that contains `FamilyHome` or a path that
contains `Battery`).
