#!/usr/bin/env ruby
input = ARGV[0]
pattern = /hbt{1,4}n/
input.scan(pattern) do |match|
    print "#{match}"
end
