# pi-bci
What is is: a Low-Cost Brain Computer Interface hardware design and code templates library. 

BCI (brain/computer interface) hardware is expensive and manufacturing is focused on medical and research applications where $2000 is an accepable price to pay for materials. pi-bci aims to get the component costs at ~$100 and make it relatively easy for students and hobbyists to play with brain computer interfaces using EEGs etc. It's also quite annoying to have to be tethered to cables all the time. The goal of this project is to come up with a low cost bill of materials (BOM) and instructions to create a viable BCI device. 

How to build a wireless $TBD BCI rig:

1. Raspberry Pi (any model is acceptable, but the 'pico w' chip is suggested due to form factor, low cost, availability without markup, and GPIO connectivity. The pico is a ~$5 chip that is deisgned for IOT workflows. It is not a full computer but can run python code via the embeddd interpereter. 

![image](https://user-images.githubusercontent.com/9088829/192466800-c7a89785-c4de-4f39-bd95-cadee2bfc9b1.png)















![image](https://user-images.githubusercontent.com/9088829/192192970-a89ca12e-e627-48a5-bffa-85387f06fcc9.png)

All pins that have “GPIO” in the name can be programmed in the os. We will use these with the ground and voltage pins to implement the designs. 

