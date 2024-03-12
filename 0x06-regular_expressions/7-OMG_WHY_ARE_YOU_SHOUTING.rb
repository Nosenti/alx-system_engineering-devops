#!/usr/bin/env ruby
input = ARGV[0]
pattern = /[A-Z]/
input.scan(pattern) do |match|
    print "#{match}"
end
