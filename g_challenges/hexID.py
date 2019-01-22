# Given a height, width, and hexID, return hexID's adjacent to the given hexID.
# height (top to bottom)
# width (left to right)
# Example -> height 3, width 7
# 1, 2, 3, 4, 5, 6, 7
# 8, 9, 10, 11, 12, 13, 14
# 15, 16, 17, 18, 19, 20, 21


def adjacent_hexes(l, w, hexID):
    # test up here whether given hexID is within range

    if hexID < 1 or hexID > (l * w):
        return

    adjacent = []

    on_top = hexID <= w
    on_bottom = hexID > (l * w) - w
    on_left = hexID % w == 1
    on_right = hexID % w == 0
    even = ((((hexID - 1) % w) + 1) % 2) == 0

    #left
    if hexID - 1 > 0 and hexID - 1 < (l * w) and (hexID - 1) % w != 0:
        adjacent.append(hexID - 1)
    #right
    if hexID + 1 > 0 and hexID + 1 < (l * w) and (hexID + 1) % w != 1:
        adjacent.append(hexID + 1)
    #top
    if not on_top:
        adjacent.append(hexID - w)
    #bottom
    if not on_bottom:
        adjacent.append(hexID + w)
    #top diags - for hexID's not on the very top, and are even
    if hexID not in range(1, w + 1) and even:
        if not on_right:
            adjacent.append(hexID - w + 1)
        if not on_left:
            adjacent.append(hexID - w - 1)

    #bottom diags
    if not on_bottom and not even:
        if not on_left:
            adjacent.append(hexID + w - 1)
        if not on_right:
            adjacent.append(hexID + w + 1)

    return sorted(adjacent)

print(adjacent_hexes(3, 3, 5)) # [ 1, 2, 3, 4, 6, 8]
print(adjacent_hexes(3, 4, 6)) # [1, 2, 3, 5, 7, 10]
print(adjacent_hexes(3, 4, 7)) # [3, 6, 8, 10, 11, 12]
print(adjacent_hexes(3, 7, 4)) # [3, 5, 11]
print(adjacent_hexes(3, 7, 1)) # [2, 8, 9]
print(adjacent_hexes(3, 7, 18)) # [10, 11, 12, 17, 19]
