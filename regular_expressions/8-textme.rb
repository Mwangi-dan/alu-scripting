#!/usr/bin/env ruby
puts ARGV[0].scan(/find:([\d\w+]*).*to:([\d\w+]*.*flags:([\d:\-]*))/).join
