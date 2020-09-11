{
  "targets": [
    {
      "target_name": "milter",
      "sources": [ "src/envelope.cc", "src/events.cc", "src/milter.cc" ],
      "include_dirs": [ "/usr/include/libmilter" , "<!(node -e \"require('nan')\")" ],
      "cflags": [ "-g -Wall" ],
      "cflags!": [ "-O3" ],
      "ldflags": [ "-L/usr/lib/libmilter" ],
      "libraries" : [ "-lmilter" ]
    }
  ]
}
