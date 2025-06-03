import random

# Number of segments to generate
N = 10

# Range for coordinates
MIN_COORD = 0
MAX_COORD = 1000

def generate_segments(n):
    segments = []
    for _ in range(n):
        # Generate random coordinates for segment endpoints
        x1 = random.uniform(MIN_COORD, MAX_COORD)
        y1 = random.uniform(MIN_COORD, MAX_COORD)
        x2 = random.uniform(MIN_COORD, MAX_COORD)
        y2 = random.uniform(MIN_COORD, MAX_COORD)
        
        # Make sure we don't generate a point (when x1=x2 and y1=y2)
        while x1 == x2 and y1 == y2:
            x2 = random.uniform(MIN_COORD, MAX_COORD)
            y2 = random.uniform(MIN_COORD, MAX_COORD)
            
        segments.append((x1, y1, x2, y2))
    return segments

# Generate segments and write to file
segments = generate_segments(N)

with open('geom.txt', 'w') as f:
    # First line contains number of segments
    # Write each segment's coordinates
    f.write("\n".join([",".join([str(round(s, 2)) for s in segment]) for segment in segments]))


print(f"Generated {N} segments and saved to geom.txt") 