Optical elements that make up an instrument
===========================================

A simulation is defined by creating objects for all optical elements such as mirrors and gratings and
sorting these optical elements in the order in which a photon encounters them. Marxs works under the
assumption that the order of elements is fixed. A photon does not have to interact with each element
(e.g. it can miss a grating, but still be detected by another focal plane instrument), but under no circumstance will a photon ever go back
to an element it already passed.

There are ways to describe layouts where photons split between different paths, such as in the
design of XMM-Newton where some photons pass the gratings and get reflected into the RGS detectors,
while others continue on their path without ever encountering a grating until they hit the imaging
detectors. Such complex setups are described in :ref:`complexgeometry`.


.. _args for optical elements:

Define an optical element for the simulation
--------------------------------------------
All optical elements have to be derived from :obj:`marxs.optics.base.OpticalElement` and they all share a common interface. 

Optical elements are generated with the following keywords:

- Optical elements are placed in 3-d space with the ``pos4d`` keyward, or the ``zoom``, ``orientation`` and ``position`` keywords as explained in :ref:`coordsys`:

  >>> from marxs.optics import FlatDetector
  >>> det1 = FlatDetector(position=[5., 1., 0.], zoom=[1, 50.2, 50.2], pixsize=0.1)  
  
- Optical elements can have a name:

  >>> from marxs.optics import FlatDetector
  >>> det1 = FlatDetector(name='back-illuminated CCD No 1')

- Individual optical elements might add more keywords (e.g. the pixel size for a detector or the filename of a parameter file); those are listed below for the individual optical elements. Here is an example for a detector:

  >>> from marxs.optics import FlatDetector
  >>> det1 = FlatDetector(pixsize=0.04)



List of optical elements provided by marxs
------------------------------------------
Note that elements which generate photons (astropysical sources or lab sources) are not listed here. See :ref:`sources`.
For convenience the following elements can be imported directly from `marxs.optics` such as:

    >>> from marxs.optics import Baffle

This short from is recommended over the long form:

    >>> from marxs.optics.baffle import Baffle

.. _sect-apertures:
    
Entrance apertures
^^^^^^^^^^^^^^^^^^

For astrophysical sources, we assume that the rays are parallel when they reach the experiement. The direction of the photons is given by the location of the source on the sky and the pointing model, but we still need to select which of the parallel rays we select for the simulation. This is done by an optical element that we call an "aperture" in Marxs. In the case of the `~marxs.optics.MarxMirror` this fuctionality is already included in the code that describes the mirror. For designs that do not use the `~marxs.optics.MarxMirror` the following entrance apertures are included in Marxs:

- `marxs.optics.RectangleAperture`
- `marxs.optics.CircleAperture`


General optical elements
^^^^^^^^^^^^^^^^^^^^^^^^

   
-   `marxs.optics.Baffle`
-   `marxs.optics.PerfectLens`
-   `marxs.optics.ThinLens`
-   `marxs.optics.MarxMirror`
-   `marxs.optics.RadialMirrorScatter`
-   `marxs.optics.GlobalEnergyFilter`
-   `marxs.optics.EnergyFilter`
-   `marxs.optics.FlatDetector`
-   `marxs.optics.MultiLayerMirror`



Diffraction gratings
^^^^^^^^^^^^^^^^^^^^
The gratings implemented in marxs solve the diffration equation, but not Maxwell's equations. Thus, they cannot determine the probability for a photon to be diffracted into a particular order. Instead, gratings accept a keyword ``order_selector`` that expects a function (or other callable) that assigngs each diffrated photon to a gratings order. For example, the following code makes a grating where the photons are distributed with equal probability in all orders from -2 to 2:

   >>> from marxs.optics import FlatGrating, uniform_efficiency_factory
   >>> select_ord = uniform_efficiency_factory(2)
   >>> mygrating = FlatGrating(d=0.002, order_selector=select_ord)

The grating module contains different classes for gratings and also different pre-defined ``order_selector`` function. Use the code in those functions as a template to define your own ``order_selector``.
   
- `marxs.optics.FlatGrating`
- `marxs.optics.CATGrating`
- `marxs.optics.constant_order_factory`
- `marxs.optics.uniform_efficiency_factory`
- `marxs.optics.EfficiencyFile`
	       
.. _complexgeometry:

Complex designs
---------------

Most optical elements only change rays that intersect them (`~marxs.optics.Baffle` is an exception - it set the probability of all photons that do **not** intersect the central hole to 0.). Thus, any complex experiement can just be constructed as a list of optical elements, even if many photons only interact with some of those elements.

Marxs offers three classes to make handling complext designs more comfortable:
`~marxs.simulator.Sequence`, `~marxs.simulator.Parallel`, and `~marxs.optics.FlatStack`:

The class `~marxs.simulator.Sequence` can be used to group several optical elements. There are two use cases:

- Group several optical elements that are passed by each photon in sequence.
- Group several different parallel elements, e.g. a CCD detector and a proportional counter that are both mounted in the focal plane.

In contrast, `~marxs.simulator.Parallel` is meant for designs with identical elements, e.g. a camera consisting of four CCD chips.
  
`~marxs.optics.FlatStack` is a special case of the `~marxs.simulator.Sequence` where several flat optical elements are passed by the photons in sequence and all elements are so close to each other, that this can be treated as a single interaction. An example is contamination on a CCD detector, which can be modeled as a Sequence of an `~marxs.optics.EnergyFilter` and a `~marxs.optics.FlatDetector`.


Reference / API
---------------
.. automodapi:: marxs.optics

.. automodapi:: marxs.simulator
