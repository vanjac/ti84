Programs I've written on my TI-84 Plus calculator. This is a mix of TI-Basic, BBC Basic, and [Axe](http://www.ticalc.org/archives/files/fileinfo/456/45659.html).

These are from multiple old backups. I committed each backup in order, so it's possible to see some changes between versions of files.

I'm using [my parse8xp fork](https://github.com/vanjac/parse8xp) to generate text files from the original program files (these are potentially incompatible with Lekensteyn's fork). For BBC Basic programs I wrote my own detokenizer script.

## Programs

Some of the more interesting programs:

- `Axe/Music/AXEMNOTE`: Music notation editor
- `Axe/Life`: Some Game Of Life things. `AXELIFE` supports custom rule codes. There's also programs here for generating a maze and then solving it.
- `Axe/BOXES`: Draw/edit boxes in 3D
- `BASMANDL`: Mandelbrot set generator in Basic
- `DRAW3D 2/DRAW3D`: Allows graphing the function Y1 in 3D (Y1 should be a function of the variables S and T; S, T, and Y1 are graphed as X, Y, and Z)
- `Biology/RNAREAD`: Interpret RNA codons
- `Chemistry/ECONFIG`: Calculate electron configuration for an element

Many programs don't work or are incomplete. There are many examples here of attempts at 3D graphics; only a few of them actually work.
