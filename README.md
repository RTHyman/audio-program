# audio emotion toy

A guide to create an enclosure for a simple python audio program for Raspberry Pi Zero that will play random sounds from different folders depending on the button you press

![enclosure_finished!](/images/enclosure/enclosure_finished.jpg)

# project goal

The initial goal of the project is to provide a simple project that will teach basics of enclosures, LEDs and buttons, soldering, python, and raspberry pi.  The pros of the approach I've taken is that you can create this project using minimal equipment and watercolour paper, not requiring you to do any woodworking or 3d printing for the enclosure. 
The goal of the project itself beyond education is to create a small box that will play short sound clips  which will have 4 different folders with different categories of sound files (wav, mp3, etc)  

In the current design, the setup is to have each color correspond to a different emotion: 

GREEN = FEAR  
RED = ANGRY  
YELLOW = HAPPY   
BLUE = SAD   

This could then be used to spend time with children or anyone else who has challenges or interest in recognizing emotions and trying out the different sounds, and discussing if you think they correspond to the emotion label, and why or why not.  

I also think its a fun concept! Future stretch goals may include:
 - attempts to use machine learning and/or large datasets to provide more audio clips beyond the samples I'm providing here. 
 - 3d printed enclosure for a more sturdy design

# parts list 

I purchased all parts from Adafruit. You could also find cheaper vendors for the same. I reccomend Adafruit especially for people in the early stages of learning, due to better documentation, reliability of parts, and fast shipping in the US. Howver you can save a lot of money using other vendors such as Mouserr or Aliexpress.

[Raspberry Pi Zero W](https://www.adafruit.com/product/3400?gclid=CjwKCAiA7ovTBRAQEiwAo8dPcT7r_diZ0nh_mxDEbGtFlZWElk7pgPRVqEoXtqhEhSXQYM8Y6hEbBBoCS2YQAvD_BwE)  
[Adafruit I2S 3W Stereo Speaker Bonnet for Raspberry Pi - Mini Kit](https://www.adafruit.com/product/3346)  
[Stereo Enclosed Speaker Set - 3W 4 Ohm](https://www.adafruit.com/product/1669) - we will only be using one of the 2 included speakers

[16mm Illuminated Pushbutton - Yellow Momentary](https://www.adafruit.com/product/1441)  
[16mm Illuminated Pushbutton - Red Momentary](https://www.adafruit.com/product/1439)  
[16mm Illuminated Pushbutton - Green Momentary](https://www.adafruit.com/product/1440)   
[16mm Illuminated Pushbutton - Blue Momentary](https://www.adafruit.com/product/1477)  
[Double-Side Prototype PCB Board](https://www.amazon.com/Double-Side-Prototype-Universal-Printed-Circuit/dp/B012YZ2Q3W?th=1)
[Small Alligator Clip Test Lead (set of 12)](https://www.adafruit.com/product/1008) not required but helpful for testing parts 

You will also need
 - Soldering gun - for example [Weller WLC100 40-Watt Soldering Station](https://www.amazon.com/Weller-WLC100-40-Watt-Soldering-Station/dp/B000AS28UC)
 - Solder - for example [Mini Solder spool](https://www.adafruit.com/product/145)
 - Wiring - for example [Stranded-Core Wire Spool - 25ft - 22AWG - Red](https://www.adafruit.com/product/3068)
 - Watercolour paper or other thick stock paper that will provide some durability. Printer paper will not be thick enough for this project. Feel free to get creative in making your enclosure!

# overview of parts

this guide assumes you already have a raspberry pi zero with raspbian setup and male headers attached - the speaker bonnet uses female headers 

[learning guide - Adafruit Speaker Bonnet for Raspberry Pi](https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi/pinouts)
 - note that pins 18, 19, and 21 of the pi are used by the sound bonnet, you cannot use them for any other purpose
 - 3V and 5V and GND at the 'top' of the GPIO are also used by the bonnet

# watercolour paper enclosure

The box enclosure is made using [this origami video](https://youtu.be/R6TUvYCrdvM) watch this for the step by step box creation instructions
See the below reference image for watercolour paper size that I used, and dimenstions  

 - note the cutout is marked as I neglected to make it big enough when I was originally making this
 - you may want to place your raspberry pi over the paper and visually verify the length of the space from the hdmi port to the power/usb ports
 - if you're unsure of this step you can always go back and do it after you've assembled the box
 - the spacing for the buttons (1.75'') from left and right sides is important so that the box can open and close properly, to leave space for other components. The vertical placement of them is not that important.
 - for the size of the holes, place the led/button ring (remove the holder ring) where you want the buttons, then use a pencil to mark the *inside* of the ring, and cut out that hole. You may want to test this on a seperate paper before trying it out on your enclosure
 - once you've made all the needed cuts, and drawn out your intended design go ahead and paint the box with acrylics before you fold and glue the box together. I used 4 sections for 4 different colors / emotion categories.
 - you can use glue sticks and some crazy glue/gorilla glue to get the box to hold per the video above

![enclosure_layout_unpainted!](/images/enclosure/enclosure_layout_unpainted.png)

Once you've gotten the box setup and folded and glued together, there's a few more steps to finish the box
 - create little "tabs" that will hold the raspberry pi zero and spaeker in place. Refer to photo below. These are the height of the box 5'' x 1-1.25'' and I fold them down next to each other and glued it together. Not the prettiest approach but it works. You don't want the tabs too tall because the wires need to be able to go over them. 
 - Alternatively, if you have screws that fit the mounting holes for Raspberry pi and the speaker, you can just mount directly to the bottom of box, and skip the tabs. 
 - I also created a 5.5'' tab to help protect the corner where the box opens and closes
 - the photo below is of the box over 2 years after I created it. It definitely looks a bit messy from all the glue and tinkering, however the box has held up well, I've carried it in my backpack, etc.

![enclosure_inside_tabs!](/images/enclosure/enclosure_inside_tabs.jpg)

# testing wiring and software

Note: It is generally considered good practice to test your wiring and software *before* you assemble your electronics, typically this involves using a breadboard and the raspberry pi zero with jumper cables. Unfortunately due to the factthat you need to solder to attach the speaker bonnet to the leds/buttons, I'm going to skip complete instructions for brevity and because testing all the parts for this project would add a lot more hassle with soldering. However, I will reccomend that you at least test one of the pushbutton led and button capabilities, to better understand how they work.

## testing wiring

For a reference on Raspberry Pi GPIO please see the [official reference here](https://www.raspberrypi.org/documentation/usage/gpio/)

Let's try testing with just one (for example, green) momentary illuminated pushbutton. For each pushbutton, there are 2 sets of contacts, one for the led and one for the button. Per the product page linked above 'There are two contacts for the button and two contacts for the LED, one marked + and one -' and the contacts that are not labeled with + or - are for the button parts. I tested this with alligator clips, but I'm sure you could find another way to test this. I'll walk through testing just the green pushbutton, but you could use the same procedure to test all of them, as long as you're using a valid GPIO pin. Keep in mind I'm using the [BCM scheme](https://pinout.xyz/#) and you can double check your specific BCM mapping using the "pinout" command on the Raspberry Pi terminal.

 - RPi GPIO 5 to + (positive) contact on green momentary pushbutton
 - 220 to 1000 ohm resistor on the - (negative) then connect back to ground pin on RPi
 - RPi GPIO 25 to one side of the button contacts 
 - RPi ground to the other side of the button contacts 
 - in the diagram, the leads connecting directly to pushbutton are the LED, and the leads going out to the side are for the button part. 

![fritzing_led-button!](/fritzing/led-button.png)

## testing python script 

first you should run this command to ensure you have the needed packages 

```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

You can use this script (in the repository as test.py) to test.

```
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) #GREEN B = FEAR 
GPIO.setup(5, GPIO.OUT) #GREEN L = FEAR

try: 
    while True: 
        button_state = GPIO.input(25)
        if button_state == False:
            GPIO.output(5, True)
            print('Button Pressed....')
            time.sleep(0.2)
        else:
            GPIO.output(5, False)
    except:
        GPIO.cleanup()
```




