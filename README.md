# catshark
## Language spec
There are two accumulators, `A` and `B`.

The program is wrapped in an infinite loop.
|Command | Behavior|
|:--:|:--:|
|`i` | Increment `A`. |
|`d` | If `A != 0`, decrement `A`. Else, skip next instruction. |
|`s` | Swap `A` and `B`. |
|`o` | Print contents of both `A` and `B`. |

This interpreter also supports a debugging command, `h`, which halts the program.
