#!/usr/bin/env ruby
input = ARGV[0]
pattern = /^h.n$/
input.scan(pattern) do |match|
    print "#{match}"
end
