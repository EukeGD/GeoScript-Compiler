GeoScript Compiler
======================
Version: 1.0.0-beta

__There are many guides on how to install view them in ./documents__

What is it?
----------------------
This is a compiler for the GeoScript programming language, on compilation it will create a .gso file then you can load it into a level. GeoScript is a statically typed, object oriented language with fetures similar to C++ and Javascript, it has less keywords to memorise than python and little unpredictable behaviour making it a very easy language to master, view docs for more infomation

How to use
----------------------
Once installed and you have written a simple GeoScript program, enter the terminal and navigate to the folder with your program, ( will be using test.gss as an example )

Execute the following:

    geoscript test.gss -o test.gso

After that you should have a .gso file witch is a compiled geoscript file, if you want to enject that into your geometry dash level run the following,

    geoinject test.gso -m gdlvl -o [ExampleLevel]
