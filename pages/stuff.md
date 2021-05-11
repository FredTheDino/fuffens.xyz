/// title: About
/// page: about
/// author: Edvard Thörnros
/// template: simple.html
/// first: 2021-05-06
/// last: 2021-05-06

<h1 class="center page-title"> Here's a list of stuff I've made </h1>
Have a browse around and see if you find anything you enjoy!
Some common denominators are: minimizing dependencies, game engines,
and compiled languages. The items are ordered by coolness.

There is one piece of "critique" people like to give me. And that's that I
never finish my game engines. In my mind, they are kinda finished. They've
been taken as far as I think I could take them at the time. I wanted to
explore new and fun ideas and do things in a different way, so I moved on.
I don't want to lock myself up to a project I don't absolutely love,
but I am proud of the achivements I've made.


Not all of them are complete, and some of them are *very* simple.

> Game Engine count: <span class="ge-count">12</span>

## Sylt (2021) - The Jam-Lang
A weakly typed dynamically/statically (I call it strangely typed) programming language
for GameJams. It has built in bindings to the Lingon engine (which I also wrote).
It's written entirely in rust, and was a great introduction to language design and implementation.

I've honestly learnt a lot about program development that I didn't know I didn't know.

<div class="link">
<a href="https://github.com/FredTheDino/sylt-lang">Sylt - GitHub</a><br>
<a href="https://github.com/sornas/lingon">Lingon - GitHub</a><br>
</div>

## Fog (2020) - The competent engine
A slim and straight forward game engine made in C++. It has some interesting
ideas about memory management with allocations being in areas and the like.
It's written in a very "C way" with a metric ton of documentation and tools.
There's a custom comment parser that automatically generates renders HTML
documentation, packaging of assets into easy to port formats and all that
jazz.

It's biggest drawback is Windows support - it's finicky to cross compile.

This is definately one of the projects I'm the most proud of.

<div class="link">
<a href="https://github.com/FredTheDino/Fog">Fog - GitHub</a>
</div>

## Sungod (2021) - The simpler Rand-Crate
A random crate with 0 dependencies and optional stdlib. It's a simple XOR-shift
but it works great for non-cryptographic uses!

<div class="link">
<a href="https://github.com/FredTheDino/sungod">Sungod - GitHub</a><br>
<a href="https://docs.rs/sungod/0.3.1/sungod/">Sungod - Docs</a><br>
</div>

## Raytracer (2020) - A simple raytracer 
A simple raytracer following the book "Ray Tracing in One Weekend" by
<a href="https://www.petershirley.com/home">Peter Shirley</a>.
It was a fun project, and I kinda want to go back and do more with it,
it's one of my smaller projects and it hasn't seen much use.

<img src="static/render.png" />

<div class="link">
<a href="https://github.com/FredTheDino/Raytracer">Raytracer - GitHub</a>
</div>

## MandelbrotEXTREEM (2019) - Mandelbrot rendering on the GPU
A simple program rendering the Mandelbrot-set using GLSL shaders.
It's super fast but suffers from a lot of problems with precision
for zooming.

Quickly cobbled together using my Block engine.

<div class="link">
<a href="https://github.com/FredTheDino/MandelbrotEXTREEM">MandelbrotEXTREEM - GitHub</a>
</div>

<h1 class="center page-title">Game Jam Games</h1>
Through the years I've made a lot of game jam games, all of varying quality.
Note that I haven't made all these games alone, other people have helped and the games would probably not exist without them.
Unfortunately the people vary between games - so I decided not to list them here but they are listed as contributors in the repos.

So here's a list:
 - <a href="https://github.com/FredTheDino/FlightOfTheTruck">Flight Of The Truck (C++ Fog) 2019</a><br>The game I'm the most proud of!
 - <a href="https://github.com/FredTheDino/GhoulDissassembly">Boomstick (C++ Fog) 2020</a><br>I really liked the game design here, also <a href="https://fredthedino.itch.io/boomstick">available on itch on itch</a>.
 - <a href="https://sornas.itch.io/ultimate-fishbee">Ultimate Fishbee (Sylt Lingon) 2021</a><br>A real stress test of the sylt language, a very wacky and fun game.
 - <a href="https://github.com/FredTheDino/Shootie">Shootie (C++ Fog) 2020</a><br>A really solid fighting game - made in 5 hours.
 - <a href="https://github.com/FredTheDino/SGJ2019">Pizzarena (Lua Love) 2019</a><br>A really solid game!
 - <a href="https://github.com/FredTheDino/SpaceCat">SpaceCat (C++ Fog) 2020 (Less involved)</a><br>I was less involved but still makes the list.
 - <a href="https://github.com/FredTheDino/GGJam2019">Cat Shootie Shootie (C++ Block) 2019</a><br>A great first try - I like the ideas but they're not executed super well.

## Honerable mentions
Here's stuff I won't link to but that I've made, they've tought me things but are not as flashy as the other stuff.

 - SMEK, was supposed to be a game but is just a really nice code base.
 - BearsInSpace, I'm really proud of the 3D collision engine I made here. Implanted GJK which was a blast.
