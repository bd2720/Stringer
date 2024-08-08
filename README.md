# Stringer
A tale of two strings.
## Goal of the game
Given a staring word (string), final word, and operations with costs, can you find the cheapest path from the starting word to the target?
## Operations
There are six different operations, each with an associated cost. Each turn, you can perform one of the operations on your current string to try and get it closer to the target string. Intermediate strings are NOT required to be valid words. Some operations are more direct than others, but it pays to be creative; fewer moves do not always equate to a lower cost!
### 1. Reverse - `reverse`
- Reverses the letters of the string.
-  `pots ==(reverse)==> stop`
- Cost: 3
### 2. Swap: `swap <pos_a> <pos_b>`
- Swaps the letters at `<pos_a>` and `<pos_b>` (the first letter on the left is at position 1).
- `slain ==(swap 2 5)==> snail`
- Cost: 1
### 3. Shift: `shift <n>`
- Shifts each letter to the right `<n>` spaces (can be negative). Letters that shift past the end of the word wrap back around to the beginning.
- `sever ==(shift 3)==> verse`
- Cost: 2
### 4. Change: `change <pos_a> <n>`
- Increments the letter at `<pos_a>` by `<n>` letters (can be negative).
- `spoke ==(change 4 7)==> spore`
- Cost: 4
### 5. Add: `add <pos_a>`
- Duplicates the letter at `<pos_a>`.
- `rots ==(add 2)==> roots`
- Cost: 3
### 6. Remove: `remove <pos_a>`
- Removes the letter at `<pos_a>`
- `proud ==(remove 4)==> prod`
- Cost: 2
