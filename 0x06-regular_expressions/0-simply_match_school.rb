#!/usr/bin/env ruby
input = ARGV[0]
pattern = /School/
input.scan(pattern) do |match|
    print "#{match}"
end
