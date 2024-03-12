#!/usr/bin/env ruby
input = ARGV[0]
pattern = /hb?tn/
input.scan(pattern) do |match|
    print "#{match}"
end
