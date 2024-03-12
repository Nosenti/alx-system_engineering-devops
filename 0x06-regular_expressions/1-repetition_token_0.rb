#!/usr/bin/env ruby
input = ARGV[0]
pattern = /hbtt{1,4}n/
input.scan(pattern) do |match|
    print "#{match}"
end
