# Context

On a large scale, the universe looks uniform both in position and in direction.
Plugging this observation into the Einstein equations yields the Robertson-Walker metric for the geometry of space.
The change of this metric over time is described by the first Friedmann equations, which is the starting point for this document.

$$\left( \frac{ \dot{a} }{ a } \right) ^2 = \frac{ 8 \pi G \rho + \Lambda c^2 }{ 3 } - \frac{ kc^2 }{ a^2 }$$

In this equation the scale factor $a = a(t)$ and the energy density $\rho = \rho(t)$ can vary over time.
The scale factor describes the expansion or contraction of the universe.
It works like this: At time $t_1$, two objects are at rest and are at a great distance $d_1$ from each other.
If the objects are not accelerated, then at time $t_2$ they will be at a distance $d_2 = \frac{ a(t_2) }{ a(t_1) } \cdot d_1$ from each other.

All derivations happen inside the [Lambda-CDM model](https://en.wikipedia.org/wiki/Lambda-CDM_model).
If that model turns out to be wrong, the visualisations may be wrong aswell.

# Evolution of the scale factor

Rearranging a bit, we get:

$$\dot{a}^2 - \frac{ 8 \pi G \rho + \Lambda c^2 }{ 3 } a^2 = -kc^2$$

Notice that the right side is constant. We can replace it with the value of the left side at any time. We choose the current time $t_0 = 13,8 \space Gyr$.
Going forward, the subscript 0 will always denote the current value of some parameter.

$$\dot{a}^2 - \frac{ 8 \pi G \rho + \Lambda c^2 }{ 3 } a^2 = \dot{a}_0^2 - \frac{ 8 \pi G \rho_0 + \Lambda c^2 }{ 3 } a_0^2$$

To make our life easier, we set $a_0 = 1$ and use the Hubble value $H = \frac{ \dot{a} }{ a }$ and the critical density $\rho_{c,0} = \frac{ 3H_0^2 }{ 8 \pi G}$.

$$\dot{a}^2 - \left( H_0^2 \frac{ \rho }{ \rho_{c,0} } + \frac{\Lambda}{3} \right) a^2 = \dot{a}_0^2 - \left( H_0^2 \frac{ \rho_0 }{ \rho _{c,0} } + \frac{\Lambda}{3} \right) a_0^2$$

$$\left( \frac{ \dot{a} }{ a } \right)^2 = H_0^2 \left( \left( 1 - \frac{ \rho_0 }{ \rho _{c,0} } + \frac{\Lambda}{3H_0^2} \right) \frac{ 1 }{ a^2 } + \frac{ \rho }{ \rho _{c,0} } + \frac{\Lambda}{3H_0^2} \right)$$

The energy density has contributions from matter and radiation: $\rho = \rho_M + \rho_R$.
They scale differently with the expansion of the universe.
Matter gets diluted by the additional volume and scales with $a^3$.
Radiation experiences a change of wavelength in addition to dilution and scales with $a^4$.
Now the energy density at an arbitrary time can be written in terms of the current value: $\rho = \frac{\rho_{R,0}}{a^4} + \frac{\rho_{M,0}}{a^3}$

$$\left( \frac{ \dot{a} }{ a } \right)^2 = H_0^2 \left( \left( 1 - \frac{ \rho_{M,0} + \rho_{R,0} }{ \rho_{c,0} } + \frac{\Lambda}{3H_0^2} \right) \frac{ 1 }{ a^2 } + \frac{ \frac{\rho_{R,0}}{a^4} + \frac{\rho_{M,0}}{a^3} }{ \rho _{c,0} } + \frac{\Lambda}{3H_0^2} \right)$$

Now we write $\Omega_x = \frac{\rho_x}{\rho_c}$ for the energy density relative to the critical density.

$$\left( \frac{ \dot{a} }{ a } \right)^2 = H_0^2 \left( \left( 1 - \Omega_{M,0} + \Omega_{R,0} + \frac{\Lambda}{3H_0^2} \right) \frac{ 1 }{ a^2 } + \frac{\Omega_{R,0}}{a^4} + \frac{\Omega_{M,0}}{a^3} + \frac{\Lambda}{3H_0^2} \right)$$

The term \frac{\Lambda}{3H_0^2} acts in a similar way to the energy density, but does not dilute during the expansion of the universe.
This influence is called dark energy.
We write $\Omega_{\Lambda,0}$ for it.

$$\left( \frac{ \dot{a} }{ a } \right)^2 = H_0^2 \left( \left( 1 - \Omega_{M,0} + \Omega_{R,0} + \Omega_{\Lambda,0} \right) \frac{ 1 }{ a^2 } + \frac{\Omega_{R,0}}{a^4} + \frac{\Omega_{M,0}}{a^3} + \Omega_{\Lambda,0} \right)$$

There is also a term that scales with $a^2$.
Only the global curvature of the universe is unaccounted so far and is responsible for this term: $\Omega_{K,0} = 1 - \Omega_{M,0} + \Omega_{R,0} + \Omega_{\Lambda,0}$

$$\left( \frac{ \dot{a} }{ a } \right)^2 = H_0^2 \left( \frac{\Omega_{R,0}}{a^4} + \frac{\Omega_{M,0}}{a^3} + \frac{ \Omega_{K,0} }{ a^2 } + \Omega_{\Lambda,0} \right)$$

$$\dot{a} = H_0 \sqrt{ \frac{\Omega_{R,0}}{a^2} + \frac{\Omega_{M,0}}{a} + \Omega_{K,0} + \Omega_{\Lambda,0} a^2 }$$

This differential equation can not be integrated easily, but the inverse $t(a)$ has a integral form:

$$t(a) = \frac{1}{H_0} \int_0^a{ \frac{ a \text{d} a }{ \sqrt{ \Omega_{R,0} + \Omega_{M,0} a + \Omega_{K,0} a^2 + \Omega_{\Lambda,0} a^4 } } }$$

# Visualisation

The python program ```main.py``` solves the above integral numerically.
Then it produces some plots of the scale factor over time.

Using the scale factor one can calculate the future lightcone of the big bang in [comoving distance](https://en.wikipedia.org/wiki/Comoving_and_proper_distances).

All light rays move along some stretch of this lightcone.
By moving and duplicating this lightcone the causal regions of the universe can be seen.
A final plot shows four causal regions:
- The affectable universe
- The observable universe
- The eventually observable universe
- The ultimately observable universe

In popular accounts the focus lays mainly on the observable universe.
This is understandable, since cosmologists are in a passive role observing events that lie in the unreachable past.
But the affectable universe is the important one.

> The end of our foundation is the knowledge of causes, and secret motions of things; and the enlarging of the bounds of human empire, to the effecting of all things possible.
> - Francis Bacon

We do not yet know which things are effectable, but we now know which things are affectable.

# Thanks

The little python program mainly reproduces some content from the beautiful paper [The Edges of Our Universe](https://arxiv.org/abs/2104.01191) by Toby Ord.
