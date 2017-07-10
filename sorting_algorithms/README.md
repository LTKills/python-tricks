# Sorting Algorithms

## Usage
- Give ```run.sh``` permission to execute with ```sudo chmod +x run.sh```
- Run ```./run.sh [elements in max vector] [progression step]```

The sorting algorithms available are:
- shell
- quick
- merge
- bubble
- insertion
- selection

Obs.: [elements in max vector] stands for the maximum vector size tested.
[progression step] stands for the increased size of the vector. For example:
```./run.sh 100 10 all``` runs the code for all the sorting algorithms with
vectors of size 0, 10, 20, 30, ..., 100. (10 is the progression step).


**Warning:** Do not run bubble with more than 10^4 elements in the vector
as it could create processes that take forever to end and you will have
to kill them manually (to be implemented).

## Licensing

    Copyright (C) 2017  Gabriel Cruz

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

