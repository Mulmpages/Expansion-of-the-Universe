import matplotlib.pyplot as plt
import math
import numpy as np

hubble_time         = 14.4e9
density_radiation   = 0.000098
density_matter      = 0.308
curvature           = 0
density_dark_energy = 0.692

# Integrand of the integral-formula for t(a) gained from the Friedmann-equation
def integrand(a):
    return  hubble_time * a / math.sqrt(
            density_radiation           +
            density_matter      * a     +
            curvature           * a**2  +
            density_dark_energy * a**4
        )

# Trapezoid approximation of area
def trapez(f, x0, x1):
    rectangle = (x1 - x0) * f(x0)
    triangle =  (x1 - x0) * (f(x1) - f(x0)) / 2
    return rectangle + triangle

# Calculates the Evolution of the scale-factor a(t) by numerical integration using trapezoids
def calc_scale_factor(astart, tmax, increase_factor):
    t = 0
    a = astart
    scale_factor = []
    
    while t < tmax:
        a1 = a
        a2 = a * increase_factor
        a = a2
        t += trapez(integrand, a1, a2)
        scale_factor.append( (t, a) )
    
    return scale_factor

scale_factor = calc_scale_factor(1e-6, 100e9, 1 + 1e-2)

# Plotting
def slice(dict, start, end):
    return {k: v for k, v in dict.items() if start <= k <= end}

def unzip(list_of_pairs):
    return list(zip(*list_of_pairs))

scale_factor_early =  [(t, a) for t, a in scale_factor if t < 50e3]
scale_factor_middle = [(t, a) for t, a in scale_factor if t > 50e3 and t < 10e9]
scale_factor_late =   [(t, a) for t, a in scale_factor if t > 10e9]

x_ticks_lin_all =      dict([(i * 20e9, f'{i * 20} Gyr') for i in range(0, 6)])
x_ticks_lin_early =    dict([(i * 10e3, f'{i * 10} kyr') for i in range(0, 6)])
x_ticks_lin_middle =   dict([(i * 2e9,  f'{i * 2}  Gyr') for i in range(0, 6)])
x_ticks_lin_late =     x_ticks_lin_all

x_ticks_log_All = {
    1e0: '1 yr',
    1e1: '10 yr',
    1e2: '100 yr',
    1e3: '1 kyr',
    1e4: '10 kyr',
    1e5: '100 kyr',
    1e6: '1 Myr',
    1e7: '10 Myr',
    1e8: '100 Myr',
    1e9: '1 Gyr',
    1e10: '10 Gyr',
    1e11: '100 Gyr',
}
x_ticks_log_Early =    slice(x_ticks_log_All, 1e0,  50e3)
x_ticks_log_Middle =   slice(x_ticks_log_All, 50e3, 10e9)
x_ticks_log_Late =     slice(x_ticks_log_All, 10e9, 1e11)

fig, axs = plt.subplots(3, 4, figsize=(15, 10))
fig.suptitle('Evolution of Scale Factor a(t) over Time')
fig.tight_layout(pad=3.0)
plt.get_current_fig_manager().window.state('zoomed')

def myPlot(ax, xs, ys, x_ticks = None, yticks = None):
    ax.plot(xs, ys)
    if x_ticks is not None:
        ax.set_xticks(list(x_ticks.keys()))
        ax.set_xticklabels(list(x_ticks.values()), rotation=90)
    if yticks is not None:
        ax.set_yticks(list(yticks.keys()))
        ax.set_yticklabels(list(yticks.values()))
    ax.grid(True, which='both', axis='both')

# Linear-Linear
axs[0, 0].set_ylabel('Linear-Linear')
axs[0, 0].set_title('Full Picture')
axs[0, 0].set_xscale('linear')
axs[0, 0].set_yscale('linear')
myPlot(axs[0, 0], *unzip(scale_factor), x_ticks_lin_all, None)

axs[0, 1].set_title('Radiation-Dominated Universe')
axs[0, 1].set_xscale('linear')
axs[0, 1].set_yscale('linear')
myPlot(axs[0, 1], *unzip(scale_factor_early), x_ticks_lin_early, None)

axs[0, 2].set_title('Matter-Dominated Universe')
axs[0, 2].set_xscale('linear')
axs[0, 2].set_yscale('linear')
myPlot(axs[0, 2], *unzip(scale_factor_middle), x_ticks_lin_middle, None)

axs[0, 3].set_title('Dark Energy-Dominated Universe')
axs[0, 3].set_xscale('linear')
axs[0, 3].set_yscale('linear')
myPlot(axs[0, 3], *unzip(scale_factor_late), x_ticks_lin_late, None)

# Linear-Log
axs[1, 0].set_ylabel('Linear-Log')
axs[1, 0].set_xscale('linear')
axs[1, 0].set_yscale('log')
myPlot(axs[1, 0], *unzip(scale_factor), x_ticks_lin_all, None)

axs[1, 1].set_xscale('linear')
axs[1, 1].set_yscale('log')
myPlot(axs[1, 1], *unzip(scale_factor_early), x_ticks_lin_early, None)

axs[1, 2].set_xscale('linear')
axs[1, 2].set_yscale('log')
myPlot(axs[1, 2], *unzip(scale_factor_middle), x_ticks_lin_middle, None)

axs[1, 3].set_xscale('linear')
axs[1, 3].set_yscale('log')
axs[1, 3].set_facecolor('mistyrose')
myPlot(axs[1, 3], *unzip(scale_factor_late), x_ticks_lin_late, None)

# Log-Log
axs[2, 0].set_ylabel('Log-Log')
axs[2, 0].set_xscale('log')
axs[2, 0].set_yscale('log')
myPlot(axs[2, 0], *unzip(scale_factor), x_ticks_log_All, None)

axs[2, 1].set_xscale('log')
axs[2, 1].set_yscale('log')
axs[2, 1].set_facecolor('mistyrose')
myPlot(axs[2, 1], *unzip(scale_factor_early), x_ticks_log_Early, None)

axs[2, 2].set_xscale('log')
axs[2, 2].set_yscale('log')
axs[2, 2].set_facecolor('mistyrose')
myPlot(axs[2, 2], *unzip(scale_factor_middle), x_ticks_log_Middle, None)

axs[2, 3].set_xscale('log')
axs[2, 3].set_yscale('log')
myPlot(axs[2, 3], *unzip(scale_factor_late), x_ticks_log_Late, None)

plt.show()


# Calculate Lightcone in comoving coordinates
speed_of_light = 1

def comoving_distance(times, scale_factors, proper_speeds):
    distance = 0
    result = [(times[0], distance)]
    for i in range(1, len(times)):
        dt = times[i] - times[i - 1]
        distance += proper_speeds[i] / scale_factors[i] * dt
        result.append( (distance, times[i]) )
    return result

lightcone_radius = comoving_distance(*unzip(scale_factor), [speed_of_light for _ in scale_factor])
lightcone_radius_R = [(-d, t) for d, t in reversed(lightcone_radius)]
lightcone = lightcone_radius_R + lightcone_radius

# Plotting
lightcone_xticks = [i * 5e9 for i in range(-13, 14)]
lightcone_xticklabels = [f'{i * 5} Glyr' for i in range(-13, 14)]
lightcone_yticks = [i * 5e9 for i in range(0, 20)]
lightcone_yticklabels = [f'{i * 5} Gyr' for i in range(0, 20)]

def plot_lightcone(ax):
    ax.set_xticks(lightcone_xticks)
    ax.set_xticklabels(lightcone_xticklabels, rotation=90)
    ax.set_yticks(lightcone_yticks)
    ax.set_yticklabels(lightcone_yticklabels)
    ax.grid(True, which='both', axis='both')

fig, ax = plt.subplots()
fig.suptitle('Comoving Lightcone')
plt.get_current_fig_manager().window.state('zoomed')
ax.plot(*unzip(lightcone))
plot_lightcone(ax)
ax.set_xlabel('Comoving Distance')
ax.set_ylabel('Time')
plt.show()


# Print important values
current_time = 13.8e9
current_lightcone_distance = None
maximum_lightcone_distance = lightcone_radius[-1][0]
for d, t in lightcone_radius:
    if t > current_time:
        current_lightcone_distance = d
        break
remaining_lightcone_distance = maximum_lightcone_distance - current_lightcone_distance

print(f'Current Time: {current_time / 1e9} Gyr')
print(f'Current Lightcone Size: {current_lightcone_distance / 1e9} Glyr')
print(f'Maximum Lightcone Size: {maximum_lightcone_distance / 1e9} Glyr')
print(f'Remaining Lightcone Size: {remaining_lightcone_distance / 1e9} Glyr')


# Show the different horizons
def color_intersection(ax, curve1, curve2, color, above=True):
    curve1_x, curve1_y = unzip(curve1)
    curve2_x, curve2_y = unzip(curve2)

    x = np.linspace(min(curve1_x), max(curve2_x), 1000)
    y = np.linspace(min(curve1_y), max(curve2_y), 1000)
    X, Y = np.meshgrid(x, y)

    interp_curve_1 = np.interp(X[0], curve1_x, curve1_y)
    interp_curve_2 = np.interp(X[0], curve2_x, curve2_y)

    if above:
        mask = (Y > interp_curve_1) & (Y > interp_curve_2)
    else:
        mask = (Y < interp_curve_1) & (Y < interp_curve_2)

    ax.contourf(X, Y, mask, levels=[0.5, 1], colors=[color], alpha=0.5)

fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('The Horizons of the Universe')
fig.tight_layout(pad=3.0)
plt.get_current_fig_manager().window.state('zoomed')

# Affectable Universe
affectable_universe_1 = [(d - current_lightcone_distance, t) for d, t in lightcone_radius]
affectable_universe_2 = [(d + current_lightcone_distance, t) for d, t in lightcone_radius_R]
axs[0, 0].plot(*unzip(affectable_universe_1), color = 'gray')
axs[0, 0].plot(*unzip(affectable_universe_2), color = 'gray')
color_intersection(axs[0, 0], affectable_universe_1, affectable_universe_2, 'lightblue', above=True)
axs[0, 0].set_title('Affectable Universe')
plot_lightcone(axs[0, 0])

# Observable Universe
observable_universe_1 = [(d - current_lightcone_distance, t) for d, t in lightcone_radius]
observable_universe_2 = [(d + current_lightcone_distance, t) for d, t in lightcone_radius_R]
axs[0, 1].plot(*unzip(observable_universe_1), color = 'gray')
axs[0, 1].plot(*unzip(observable_universe_2), color = 'gray')
color_intersection(axs[0, 1], observable_universe_1, observable_universe_2, 'lightblue', above=False)
axs[0, 1].set_title('Observable Universe')
plot_lightcone(axs[0, 1])

# Eventually Observable Universe
eventually_observable_universe_1 = [(d - maximum_lightcone_distance, t) for d, t in lightcone_radius]
eventually_observable_universe_2 = [(d + maximum_lightcone_distance, t) for d, t in lightcone_radius_R]
axs[1, 0].plot(*unzip(eventually_observable_universe_1), color = 'gray')
axs[1, 0].plot(*unzip(eventually_observable_universe_2), color = 'gray')
color_intersection(axs[1, 0], eventually_observable_universe_1, eventually_observable_universe_2, 'lightblue', above=False)
axs[1, 0].set_title('Eventually Observable Universe')
plot_lightcone(axs[1, 0])

# Ultimately Observable Universe
axs[1, 1].plot(*unzip(affectable_universe_1), color = 'gray', linestyle='--')
axs[1, 1].plot(*unzip(affectable_universe_2), color = 'gray', linestyle='--')
ultimately_observable_universe_1 = [(d - maximum_lightcone_distance - remaining_lightcone_distance, t) for d, t in lightcone_radius]
ultimately_observable_universe_2 = [(d + maximum_lightcone_distance + remaining_lightcone_distance, t) for d, t in lightcone_radius_R]
axs[1, 1].plot(*unzip(ultimately_observable_universe_1), color = 'gray')
axs[1, 1].plot(*unzip(ultimately_observable_universe_2), color = 'gray')
color_intersection(axs[1, 1], ultimately_observable_universe_1, ultimately_observable_universe_2, 'lightblue', above=False)
axs[1, 1].set_title('Ultimately Observable Universe')
plot_lightcone(axs[1, 1])

plt.show()
