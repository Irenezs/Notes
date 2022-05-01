# Standard Model of Particle Physics
![[Standard Model.jpg]]
## Quarks
### Smaller Scattering
In 1968, a group of physicists conducted an experiment to Rutherford's gold foil experiment, but on nucleons, with a beam of electrons. This yielded similar results, such as deflections of varying angles, proving that nucleons were made of something smaller, which came to be known as quarks, currently accepted to be the smallest indivisible particle.
There are 6 different quarks, although this course only cares about 3:
up: u, down: d, and strange: s. Their properties are below:

Quark|Charge|Baryon Number|Strangeness
---|---|---|---
u|+2/3|+1/3|0
d|-1/3|+1/3|0
s|-1/3|+1/3|-1
Each quark has a counterpart; anti-quarks have essentially the same properties, but just reversed, so anti-up has a charge of -2/3, for example.

Quarks cannot be on their own, due to their fractional properties. 

Quark-based particles are called [[#Hadrons|hadrons]], which can be broken into two separate groups: [[#Mesons|mesons]], containing a quark and antiquark, and [[#Baryons|baryons]], containing 3 quarks or 3 antiquarks.

## Hadrons
### Mesons
- quark / anti-quark pair
- 8 needed to memorise for the course

Meson|Symbol|Quarks|Charge|Strangeness
---|---|---|---|---
Pion +|$\pi^+$|$u\overline{d}$|+1|0
Pion -|$\pi^-$|$\overline{u}d$|-1|0
Pion 0|$\pi^0$|$d\overline{d}$|0|0
Anti-Pion 0|$\pi^0$|$u\overline{u}$|0|0
Kaon +|$K^+$|$u\overline{s}$|+1|+1
Kaon -|$K^-$|$\overline{u}s$|-1|-1
Kaon 0|$K^0$|$d\overline{s}$|0|+1
Anti-Kaon 0|$\overline{K}^0$|$\overline{d}s$|0|-1

### Baryons
- 3 quarks OR 3 anti-quarks
- 4 needed to know for course

Baryon|Symbol|Quarks|Charge|Strangeness|Baryon Number
---|---|---|---|---|---
proton|$p$|$uud$|+1|0|+1
neutron|$n$|$udd$|0|0|+1
anti-proton|$\overline{p}$|$\overline{uud}$|-1|0|-1
anti-neutron|$\overline{n}$|$\overline{udd}$|0|0|-1
## Leptons
- TODO
## Fundamental Forces
There are 4 fundamental forces, gravity, electromagnetic, strong nuclear, and weak nuclear, which each have different ranges and strengths, shown below:

Force|Range|Relative Strength
:---|:---:|---:
Strong Nuclear|~$10^{-15}$m|$1$
Weak Nuclear|~$10^{-18}$m|~$10^{-7}$
Electromagnetic|$\infty$m|~$10^{-2}$
Gravitational|$\infty$m|~$10^{-36}$
### Exchange Particles
Virtual Particles, or Exchange Particles, are what carry the force between two particles. This set of particles are called Bosons, some of which are in the image before [[#Quarks]].

These particles are made from energy that shouldn't exist, which is shockingly possible. This is able to be done because of the Heisenberg Uncertainty Principle, which establishes that a particle of mass-energy $\Delta E$ _can_ exist for time $\Delta t$, as long as $\Delta E\times\Delta t \leq h$.

### Strong Nuclear Force
Causes an attractive or repulsive force between quarks (and by extension hadrons). The bosons related to the strong interaction are the gluon, $g$, and pion, $\pi^{\pm/0}$, where the gluon will be used between quarks and the pion between baryons. The strong interaction acts upon nucleons.

### Weak Nuclear Force
Does not cause a physical force, but makes particles decay. The weak means that it is rare. The bosons related to the weak interaction are the $W^+$,$W^-$, and $Z^0$ bosons. The weak interaction can act on any particle.

### Electromagnetic
Causes an attractive or repulsive force between charges. The boson related to electromagnetism is the virtual photon, $\gamma$. The electromagnetic interaction acts upon charged particles.

### Gravitational
Causes an attractive force between masses. The boson related to gravitation is the graviton, with no symbol. It acts on particles with mass.


# The Photoelectric Effect
## Basics
When light of high enough energy is incident on a metal plate, it was observed that electrons were released from the surface of the plate. When the intensity of light was increased, the number of electrons emitted increased. If the frequency of light was lowered past some threshold, no electrons were emitted.

When this was discovered, light was believed to act as a wave. These observations contradicted this model, as if light acted as a wave, increasing the intensity of light should have increased the energy of the light, and the energy of the light should have released the electrons slowly, rather than instantly.

## Photon
Because of the observations in [[#Basics]], Max Planck had the idea that light could be small packets of energy, which Einstein developed further, giving them the name photons. The energy of a photon was found to be $E=hf$.

## Technical Explanation
Einstein went on to develop the photoelectric effect, and suggested that each photon interacts with a single electron in the metal. The energy of the photon would then be absorbed by the electron, where it uses some to break the bonds keeping it to the metal, then stored the rest as kinetic energy.
$$\text{The formula derived for this is: }hf=\phi+E_k$$
The $\phi$ is the work function of the metal, meaning how much energy is required to remove the electron from the metal.

A key term to learn is the threshold frequency, $f_0$, which is the lowest frequency of photon that can still release an electron. This means the electron will have no kinetic energy. A formula can be found through rearrangement: $$f_0=\frac{\phi}{h}$$
## Graph
If we graph kinetic energy against frequency, we get a graph that describes the formula derived in [[#Technical Explanation]], as shown below: $$y=mx+c \Rightarrow E_k=hf-\phi$$
When plotted, this graph will have a gradient of Planck's constant, and if extrapolated below 0, a y-intercept of the work function: ![[Photoelectric Graph.png|500]]


