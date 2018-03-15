def CTPPSTrackingStripLayout(i, p, *rows): i["00 Shift/CTPPS/TrackingStrip/" + p] = DQMItem(layout=rows)
def CTPPSTrackingPixelLayout(i, p, *rows): i["00 Shift/CTPPS/TrackingPixel/" + p] = DQMItem(layout=rows)

stations = [ "sector 45/station 210", "sector 56/station 210" ]
units = [ "nr", "fr" ]

sectors = [ "sector 45", "sector 56" ]
pixstations = [ "sector 45/station 220/", "sector 56/station 220/" ]
pix_planes  = [ "0","1","2" ]
pix_planes2 = [ "3","4","5" ]


# layouts with no overlays
for plot in [ "active planes", "vfats with any problem", "track XY profile" ]:
  rows = list()
  for station in stations:
    row = list()
    for unit in units:
      row.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot)
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot, *rows)


# layouts with overlays
for plot in [ "planes contributing to fit" ]:
  rows = list()
  for station in stations:
    row = list()
    for unit in units:
      hist_u = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " U"
      hist_v = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " V"
      row.append( { "path" : hist_u, "overlays" : [ hist_v ] } )
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot + " UV", *rows)


# per-BX plots
for suffix in [ " (short)" ]:
  plot_list = list()
  for station in stations:
    for unit in units:
      plot_list.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/activity per BX" + suffix)

  base_plot = "CTPPS/events per BX" + suffix
  CTPPSTrackingStripLayout(dqmitems, "activity per BX" + suffix, [ { "path" : base_plot, "overlays" : plot_list } ])

###
# 	CTPPS Pixel
###

for plot in ["ROCs_hits_multiplicity_per_event vs LS","number of fired planes per event"]:
  rows = list()
  for station in pixstations:
    row = list()
    row.append("CTPPS/TrackingPixel/"+station+"fr_hr/"+plot)
    rows.append(row)

  CTPPSTrackingPixelLayout(dqmitems, plot, *rows)

for plot in ["hits position"]:
  for sector in sectors:
    rows = list()
    row = list()
    for plane in pix_planes:
      row.append("CTPPS/TrackingPixel/"+sector+"/station 220/fr_hr/plane_"+plane+"/"+plot)
    rows.append(row)

    row = list()
    for plane in pix_planes2:
      row.append("CTPPS/TrackingPixel/"+sector+"/station 220/fr_hr/plane_"+plane+"/"+plot)
    rows.append(row)

    CTPPSTrackingPixelLayout(dqmitems, plot+":" +sector+" station 220_fr_hr", *rows)

