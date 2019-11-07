# CrashPrediction

## Step 1. Data clean and Features transformation
1.1 

- [ ] Crash ID  -->  
- [ ] Adjusted Average Daily Traffic Amount         --> (No Data, 62579)
- [ ] Commercial Motor Vehicle Flag                 --> (No, Yes) ==> (0, 1)
- [ ] Crash Death Count                             --> (0,1,2,...) ==> int
- [ ] Crash Time                                    --> (2329, 1033) --> 1./(24*12) float, consider 5 min as an unit
- [ ] Crash Total Injury Count                      --> (0, 1, 2, ..) ==> int
- [ ] Curve Degrees                                 --> (0, 1, 2, 3, 4) ==> ???
- [ ] Curve Type                                    --> (No Data, N) ==> ???
- [ ] Day of Week                                   --> (Monday, Tue...) ==> (0, 1, 2,...) ==> (0, 1/7, ...6/7)???
- [ ] Inside Shoulder Width on Divided Highway      --> (No Data, Null, 0, 10, 11, 16) ==> ???
- [ ] Latitude                                      --> (32.6628643, No Data) ==> keep it original
- [ ] Light Condition                               --> (1-Daylight, 3, Dark-lighted, 99-unknown) ==> (0, 1, 2, 3, 99)
- [ ] Longitude
- [x] Manner of Collision                           --> ()
- [ ] Number of Lanes                               --> (No Data, 4, 6, 7, 8,) ==> Integer
- [x] Object Struck                                 --> ???
- [ ] Outside Shoulder Width on Divided Highway     --> (No Data, 0, 10, ) ==> int or float?
- [x] Property Damages                              --> (None, Guard Rail, Utility Pol...) ==> ?
- [ ] Road Class                                    --> (City Street, Interstate, US & State highways) ==> (1, 2, 3)
- [x] Street Name
- [x] Street Number
- [ ] Surface Condition                             --> (1-Dry, 6-ICE, 99-UNKNOWN)
- [ ] Weather Condition                             --> (1-clear, 2-cloudy,...)
- [ ] Diver Alcohol Result                          --> (No Data, 1-POSITIVE, 1)

