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
https://en.wikipedia.org/wiki/Visvalingam–Whyatt_algorithm

## I/O:
- figure out strava API to get segment data
- start with taking in parts of FIT / GPS / GPX files? -> also pick out climbs from entire routes
- core algorithm just takes in dist/elev data
- smooth gps data?


https://pypi.org/project/gpxpy/


## Ok how are we doing this for real
- given an altitude vs distance path
- Smooth Elevation profile (input parameter: how much smoothing?)
- Find peaks in elevation profile data-- using signal analysis (input parameter - how small of a peak to count?)
  - TBD: how do we identify inflections but not peaks? i.e. intermediate flats. This is peaks in 2nd derivative
  - Maybe there is some kind of total score of points of interest involving both?
    - Figure out how to count inflection+peak as the same point, they may not necessarily be exactly the same data point
  - Then, once peak points are determined, simply take h/d for the grade between them
- Develop filter for what counts as a "climb"
  - Maybe slightly different weighting of peak data? 
- Smoothing-like parameters should have a scalar value as well as related to total length of route
- Maybe an alternative approach: find "candidate climb" segments that have both a beginning and an end
  - Has length, flatness, whether they are contained in any other climbs
  - determine whether it is a climb or a slope section

- Maybe split in to two types of analysis:
  - Overall Climb/No-climb (mostly peak-driven)
  - Sections-of-Constant-slope analysis

- Or, modified "midpoint method" that just results in an arbitrary number of segments.
  - Some sort of cost optimization that weights no. of segments vs quality of fit

- Maybe do the midpoint method, and then use that analysis to separate in to larger segments
  - allows more-expensive analysis like determining which group(s) of segments represent longer climbs