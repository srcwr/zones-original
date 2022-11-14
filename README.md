# zones
work-in-progress standardized zones for bhoptimer

Pull-requests are welcome.

[home page](https://github.com/srcwr/zones)

[github pages page](https://srcwr.github.io/zones/)

## To use
in `cfg/plugin.shavit-zones.cfg`
```
shavit_zones_usesql "0"
```
in `cfg/plugin.shavit-zones-http.cfg`
```
shavit_zones_http_url "https://srcwr.github.io/zones/{engine}/{map}.json"
```

## other stuff
`cstrike/_.json` originates from the btimes zones table from Solitude, courtesy of Eric ([Github]( https://github.com/ecsr) / [Steam](https://steamcommunity.com/id/-eric))

`cstrike/_.py` is a python file to mostly convert the zones to shavit-zones-http compatible files...
