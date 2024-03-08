"Climb analyzer"  -> Take in distance/elevation data of a bike climb and simplify it in to "X mi at X%" segments
http://lowkeyhillclimbs.com/2014/week5/profile.html

overall objective: describe an elevation profile with an appropriate amount of "X mi at X%" descriptors
   main question is: what does "X mi at X%" mean? 
      should it explicitly represent the average grade, 
      some other measure (maybe the mode-ish grade over a pitch?)
      or weighted-average slope?  (steeper counts for more?)

additionally: evaluate/compare climbs in "X ft elevation above X% grade" fashion for comparison, and generate plots

additional stats for climb:
max grade (over x ft)
total elevation gain
average grade; average grade of climbing; average grade of climbs

- probably need the ability to tune the output for more/less steps.  score = (correlation with data vs simplicity of path)
- option to split by miles/kms instead of inflection points
- analyze entire routes
- pitfalls:  steadily increasing grades (Alpine Rd), false flats, dips up/down at endpoints
- do we enforce the path as continuous?   or, maybe make the entire path and then exclude/ignore shortest pieces  (ignore transitions between pieces?)
- possible algorithm: start assuming single line connecting start/end; separate the segment at the point furthest from the path; repeat until score is minimized 
- another algorithm: use (smoothed?) second derivative of data to find inflection points
- another: find plateaus/flats in grade vs distance data (maximize distance covered while minimizing variance) -- equivalent to finding long consistent slopes
  or maybe use "slope plateau" method, then fill in/link the gaps?  


## Algorithm notes
https://en.wikipedia.org/wiki/Smoothing
https://en.wikipedia.org/wiki/Random_sample_consensus0
https://stackoverflow.com/questions/13691775/python-pinpointing-the-linear-part-of-a-slope
https://en.wikipedia.org/wiki/Ramer–Douglas–Peucker_algorithm -> this is the midpoint method

## I/O:
- figure out strava API to get segment data
- start with taking in parts of FIT / GPS / GPX files? -> also pick out climbs from entire routes
- core algorithm just takes in dist/elev data
- smooth gps data?


https://pypi.org/project/gpxpy/