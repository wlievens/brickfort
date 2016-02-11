# BrickFort

![BrickFort](http://i.imgur.com/5HKYdtv.png)

*BrickFort* is an attempt at implementing a "Procedural Castle" as proposed by the Second Monthly Challenge on [/r/proceduralgeneration](https://www.reddit.com/r/proceduralgeneration)

**Challenge:** https://www.reddit.com/r/proceduralgeneration/comments/3zy53l/monthly_challenge_2_jan_2016_procedural_castle

**WIP:** https://www.reddit.com/r/proceduralgeneration/comments/3zy53l/monthly_challenge_2_jan_2016_procedural_castle/cyqfw4r

**Submission:** https://www.reddit.com/r/proceduralgeneration/comments/45ay7o/brickfort_my_procedural_lego_castle

There will be no interactive demo this time, because the system is not web-based. It generates an **LDR** file which you can open in the **LDRaw** tool suite.

**To you run this, you need to do the following:**

* Install **LDraw** using the all-in-one installer: http://www.ldraw.org/article/104.html
* Run the python script. Modify the seed in the random.seed() call if you want. Some seeds may yield invalid or uninteresting castles.
* Open the `castle.ldr` file in **LDView** and choose a nice viewing angle
* Export the scene to a **POV** file
* Install **POVRay**: http://www.povray.org/download/
* Open `castle.pov` in **POVRay** and tune the options at the top of the file if necessary
* Render!
