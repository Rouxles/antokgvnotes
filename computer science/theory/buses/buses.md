# Buses

Buses are the means by which data is transmitted from one part of a computer to another, connecting all major internal components to the CPU and memory.

Buses are limited by their 'width' in bits. This tells us how many bits can be sent by the bus **at the same time**.

The bus that connects the CPU to the memory is called the FSB (Front side bus) or the system bus. CPU cores share L2 and L3 cache across the FSB. They will usually connect to Level 2 cache through the BSB.

The FSB contains 2 types of buses:

1. Address bus - sends information about where data needs to go by sending an address to the memory. The address bus only sends data in one direction - from the CPU to the RAM (there is no need for the CPU to receive any data, so it is uni-directional or simple.)
2. Data bus - this sends data to the memory or receives data from the memory. Data can flow both ways (because data is needed by both CPU and RAM, and this bus sends data.)

---

There are 3 different kinds of buses:

1. Address bus: (see above)
2. Data bus: (see above)
3. Control bus: This bus carries signals relating to the control and condition of all activities within the computer (example: read and write functions). It is unidirectional.
