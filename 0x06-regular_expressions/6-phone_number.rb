#!/usr/bin/env ruby
input = ARGV[0]
pattern = /^[0-9]{10}$/
input.scan(pattern) do |match|
    print "#{match}"
end
